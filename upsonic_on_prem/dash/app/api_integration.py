#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import ast


from rich.console import Console

console = Console()


from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet


load_dotenv(dotenv_path=".env")

api_url = "http://localhost:3000"


class API_Integration:
    def _log(self, message):
        console.log(message)

    def __enter__(self):
        return self  # pragma: no cover

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # pragma: no cover

    def __init__(self, admin_key):
        import requests
        from requests.auth import HTTPBasicAuth

        self.requests = requests
        self.HTTPBasicAuth = HTTPBasicAuth

        self.api_url = api_url
        self.password = admin_key

        if self.status == True:
            self._log(
                f"[bold green]Upsonic[bold green] active",
            )
        else:
            self._log(
                f"[bold red]Upsonic[bold red] is down",
            )
    @staticmethod
    def create_access_key():
        return (
            "ACK_"
            + (
                ((Fernet.generate_key()).decode())
                .replace("-", "")
                .replace("_", "")
                .replace("=", "")
            )[:60]
        )

    def _send_request(self, method, endpoint, data=None, make_json=True):
        try:
            response = self.requests.request(
                method,
                self.api_url + endpoint,
                data=data,
                auth=self.HTTPBasicAuth("", self.password),
                verify=False,
            )
            try:
                result = None
                if not make_json:
                    result = response.text
                else:
                    result = json.loads(response.text)
                    if result["status"] == False:
                        self._log(
                            f"[bold red]Error: {endpoint}",
                        )
                    else:
                        result = result["result"]

                return result
            except:  # pragma: no cover
                print(f"Error on '{self.api_url + endpoint}': ", response.text)
                return [None]  # pragma: no cover
        except:
            print("Error: Remote is down")
            return [None]

    @property
    def status(self):
        return self._send_request("GET", "/status")

    @property
    def users(self):
        return self._send_request("GET", "/get_users")

    @property
    def users_keys(self):
        return self._send_request("GET", "/get_users_keys")


    @property
    def admins(self):
        return self._send_request("GET", "/get_admins")

    @property
    def total_size(self):
        return self._send_request("GET", "/total_size")

    @property
    def all_scopes(self):
        result = self._send_request("GET", "/get_all_scopes")
        print(result)
        return result if result != [None] else []

    @property
    def top_scopes(self):
        all_scopes = self.all_scopes
        result = []

        for i in all_scopes:
            if "." in i:
                result.append(i.split(".")[0])

        result = list(set(result))
        result.sort()

        return result

    @property
    def sub_based_all_scopes(self):
        return self.sub_based_all_scopes_()

    def sub_based_all_scopes_(self, prefix=None):

        all_scopes = self.all_scopes

        def group_by_top_level_recursive(function_list):
            grouped_dict = {}

            for function_name in function_list:
                parts = function_name.split('.')
                current_dict = grouped_dict

                for part in parts:
                    if part not in current_dict:
                        current_dict[part] = {}
                    current_dict = current_dict[part]

            return grouped_dict
        grouped = group_by_top_level_recursive(all_scopes)
        result = grouped

        def add_top_level_names(dictionary, parent_name=''):
            result = {}
            for key, value in dictionary.items():
                current_name = f"{parent_name}.{key}" if parent_name else key
                if isinstance(value, dict):
                    result[current_name] = add_top_level_names(value, current_name)
                else:
                    result[current_name] = value
            return result

        result = add_top_level_names(result)

        def extract_key(dictionary, target_key):
            if target_key in dictionary:
                return {target_key: dictionary[target_key]}

            for key, value in dictionary.items():
                if isinstance(value, dict):
                    result = extract_key(value, target_key)
                    if result:
                        return result

            return None

        if prefix != None:
                result = extract_key(result, prefix)

        def replace_empty_with_false(dictionary):
            for key, value in dictionary.items():
                if isinstance(value, dict):
                    if not value:
                        dictionary[key] = False
                    else:
                        replace_empty_with_false(value)
            return dictionary

        # Your example dictionary
        result = replace_empty_with_false(result)

        return result

    def subs_of_scope(self, prefix):
        sub_scopes_general_list = self.sub_based_all_scopes_(prefix)

        def match_prefix(dictionary, prefix):
            for key, value in dictionary.items():
                if key == prefix:
                    return value
                else:
                    if value != False:
                        return match_prefix(value, prefix)
            return None

        result = match_prefix(sub_scopes_general_list, prefix)
        print(result)
        return result
    def get_code(self, scope):
        data = {"scope": scope}
        return self._send_request("POST", "/get_code_of_scope", data=data)

    def get_documentation(self, scope):
        data = {"scope": scope}
        return self._send_request("POST", "/get_document_of_scope", data=data)

    def create_documentation(self, scope):
        data = {"scope": scope}
        return self._send_request(
            "POST", "/create_document_of_scope", data=data
        )



    def get_users(self):
        users = self.users_keys
        print(users)
        result = []
        for i in users:
            the_name = self.get_name(i)
            if the_name == None:
                the_name = "Robust Admin"
            result.append([the_name, self.is_enabed_user(i), self.is_admin(i), i])

        # sort
        result.sort(key=lambda x: x[0])
        return result



    def add_user(self, key):
        data = {"key": key}
        return self._send_request("POST", "/add_user", data=data)

    def set_name(self, key, name):
        data = {"key": key, "name": name}
        return self._send_request("POST", "/set_name", data=data)

    def get_name(self, key):
        data = {"key": key}
        return self._send_request("POST", "/get_name", data=data)

    def delete_user(self, key):
        data = {"key": key}
        return self._send_request("POST", "/delete_user", data=data)

    def disable_user(self, key):
        data = {"key": key}
        return self._send_request("POST", "/disable_user", data=data)

    def enable_user(self, key):
        data = {"key": key}
        return self._send_request("POST", "/enable_user", data=data)

    def is_enabed_user(self, key):
        data = {"key": key}
        return self._send_request("POST", "/is_enabled_user", data=data)

    def is_admin(self, key):
        data = {"key": key}
        return self._send_request("POST", "/is_admin", data=data)

    def enable_admin(self, key):
        data = {"key": key}
        return self._send_request("POST", "/enable_admin", data=data)

    def disable_admin(self, key):
        data = {"key": key}
        return self._send_request("POST", "/disable_admin", data=data)
