import time

import redis
import random
import os
import traceback
import json

from upsonic_on_prem.api.utils import storage

from upsonic_on_prem.api.utils.configs import admin_key



class AccessKey:
    def __init__(self, key):
        self.key = key

        self.robust_allowed = [
            self.key+":events"
        ]

    def set_robust(self, robust):
        return self._set(self.key + ":robust", robust)

    @property
    def robust(self):
        return self._get(self.key + ":robust") == True


    def _set(self, key, value):
        if self.robust:
            if key not in self.robust_allowed:
                return False

        return storage.set(key, value)

    def _get(self, key):
        return storage.get(key)

    def _delete(self, key):
        if self.robust:
            return False

        return storage.delete(key)

    def _keys(self):
        if self.robust:
            return False

        return storage.keys()


    def enable(self):
        self._set(self.key + ":enable", True)
    def disable(self):
        self._set(self.key + ":enable", False)
    @property
    def is_enable(self):

        return self._get(self.key + ":enable") == True

    def set_is_admin(self, is_admin):
        return self._set(self.key + ":is_admin", is_admin)
    @property
    def is_admin(self):
        return self._get(self.key + ":is_admin") == True

    @staticmethod
    def get_admins():
        keys = storage.keys()
        admins = []
        for i in keys:
            if i.endswith(":is_admin") and storage.get(i):
                admins.append(i[:-9])

        return admins

    @staticmethod
    def get_users():
        keys = storage.keys()
        users = []
        for i in keys:
            if i.endswith(":enable"):
                users.append(AccessKey(i[:-7]).name)

        return users

    @staticmethod
    def get_users_keys():
        keys = storage.keys()
        users = []
        for i in keys:
            if i.endswith(":enable"):
                users.append(i[:-7])

        return users

    @staticmethod
    def get_len_of_users():
        users = AccessKey.get_users()
        return len(users)

    @staticmethod
    def get_len_of_admins():
        admins = AccessKey.get_admins()
        return len(admins)

    @property
    def name(self):

        return self._get(self.key + ":name")


    def scopes_write_clear(self):
        return self._set(self.key + ":scopes_write", [])


    def scopes_read_clear(self):
        return self._set(self.key + ":scopes_read", [])



    @property
    def scopes_write(self):

        return self._get(self.key + ":scopes_write") or []
        
    @property
    def scopes_read(self):
        return self._get(self.key + ":scopes_read") or []

    @property
    def events(self):
       
        from_db = self._get(self.key + ":events")

        if from_db == None:
            return {}
        return from_db

    def event(self, event, target, detail, scope_target=False, meta={}):
        currently = self.events
        the_time = str(time.time()) + "_" + str(random.randint(0, 100000))
        the_event = {"event": event, "target":target, "detail":detail}
        the_event["scope_target"] = scope_target
        the_event["meta"] = meta
        currently[the_time] = the_event


        self._set(self.key + ":events", currently)

    def get_last_x_events(self, x):
        # get last x element of dict but return should be a dict
        all_events = self.events


        last_x_events = {}
        for i in list(all_events.keys())[-x:]:
            last_x_events[i] = all_events[i]

        last_x_events = dict(reversed(list(last_x_events.items())))

        return last_x_events
    def set_name(self, name):

        return self._set(self.key + ":name", name)
    
    def set_scope_write(self, scope):
        currently_list = self.scopes_write
        currently_list.append(scope)
        return self._set(self.key + ":scopes_write", currently_list)
    
    def set_scope_read(self, scope):
        currently_list = self.scopes_read
        currently_list.append(scope)
        return self._set(self.key + ":scopes_read", currently_list)


    def delete_scope_write(self, scope):
        currently_list = self.scopes_write
        currently_list.remove(scope)
        return self._set(self.key + ":scopes_write", currently_list)

    def delete_scope_read(self, scope):
        currently_list = self.scopes_read
        currently_list.remove(scope)
        return self._set(self.key + ":scopes_read", currently_list)


    
    def delete(self):
        self._delete(self.key + ":name")
        self._delete(self.key + ":scopes_write")
        self._delete(self.key + ":scopes_read")
        self._delete(self.key + ":is_admin")
        self._delete(self.key + ":enable")
        self._delete(self.key + ":robust")
        self._delete(self.key + ":events")
        self._delete(self.key + ":openai_api_key")


    

    def can_access_write(self, scope):
        all_scopes = self.scopes_write
        
        control = False

        for i in all_scopes:
            if scope == i:
                control = True
                break
            elif scope.startswith(i[:-1]) and i.endswith("*"):
                control = True
                break

        return control

    def can_access_read(self, scope, custom_scopes_read=None):
        all_scopes = self.scopes_read if custom_scopes_read is None else custom_scopes_read
        
        control = False

        for i in all_scopes:
            if scope == i:
                control = True
                break
            elif scope.startswith(i[:-1]) and i.endswith("*"):
                control = True
                break

        return control

if admin_key is not None:
    the_admin = AccessKey(admin_key)

    the_admin.enable()

    the_admin.set_is_admin(True)
    the_admin.set_robust(True)
