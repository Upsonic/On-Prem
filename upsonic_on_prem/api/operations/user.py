import hashlib
from upsonic_on_prem.api import app

from upsonic_on_prem.api.urls import *

from upsonic_on_prem.utils import storage, storage_2, storage_4, AccessKey, Scope, AI

from upsonic_on_prem.utils.configs import openai_api_key

from flask import jsonify
from flask import request

import time


@app.route(dump_url, methods=["POST"])
def dump():
    scope = request.form.get("scope")
    data = request.form.get("data")

    the_scope = Scope(scope)

    return jsonify(
        {"status": True, "result": the_scope.dump(data, AccessKey(request.authorization.password), pass_str=True)})


@app.route(dump_code_url, methods=["POST"])
def dump_code():
    scope = request.form.get("scope")
    code = request.form.get("code")

    the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.set_code(code)})


@app.route(dump_type_url, methods=["POST"])
def dump_type():
    scope = request.form.get("scope")
    type = request.form.get("type")

    the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.set_type(type)})



@app.route(load_url, methods=["POST"])
def load():
    scope = request.form.get("scope")

    return jsonify({"status": True, "result": Scope(scope).source})


@app.route(get_read_scopes_of_me_url, methods=["get"])
def get_read_scopes_of_me():
    return jsonify({"status": True, "result": AccessKey(request.authorization.password).scopes_read})


@app.route(get_write_scopes_of_me_url, methods=["get"])
def get_write_scopes_of_me():
    return jsonify({"status": True, "result": AccessKey(request.authorization.password).scopes_write})


@app.route(get_document_of_scope_url, methods=["POST"])
def get_document_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.documentation})


@app.route(get_requirements_of_scope_url, methods=["POST"])
def get_requirements_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.requirements})



@app.route(get_settings_of_scope_url, methods=["POST"])
def get_settings_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.settings})





@app.route(get_time_complexity_of_scope_url, methods=["POST"])
def get_time_complexity_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.time_complexity})






@app.route(get_mistakes_of_scope_url, methods=["POST"])
def get_mistakes_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.mistakes})




@app.route(get_required_test_types_of_scope_url, methods=["POST"])
def get_required_test_types_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.required_test_types})



@app.route(get_tags_of_scope_url, methods=["POST"])
def get_tags_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.tags})

    scope = request.form.get("scope")


@app.route(get_security_analysis_of_scope_url, methods=["POST"])
def get_security_analysis_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.security_analysis})





@app.route(get_code_of_scope_url, methods=["POST"])
def get_code_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.code})

@app.route(get_dump_user_of_scope_url, methods=["POST"])
def get_dump_user_of_scope():
    dump = request.form.get("dump")
    object = Scope.get_dump(dump)
    return jsonify({"status": True, "result": object.user})


@app.route(get_version_user_of_scope_url, methods=["POST"])
def get_version_user_of_scope():
    version = request.form.get("version")
    object = Scope.get_version(version)
    return jsonify({"status": True, "result": object.user})


@app.route(get_version_code_of_scope_url, methods=["POST"])
def get_version_code_of_scope():
    version = request.form.get("version")
    object = Scope.get_version(version)
    return jsonify({"status": True, "result": object.code})

documentation_tasks = []

@app.route(create_document_of_scope_url, methods=["POST"])
def create_document_of_scope():
    global documentation_tasks

    scope = request.form.get("scope")
    version = request.form.get("version")
    task_name = scope
    if version != None:
        task_name = scope+":"+version
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    if not task_name in documentation_tasks:
        documentation_tasks.append(task_name)
        try:
            work = the_scope.create_documentation()
        except:
            pass
        try:
            documentation_tasks.remove(task_name)
        except:
            pass
    else:
        while task_name in documentation_tasks:
            time.sleep(1)
        work = the_scope.documentation
    return jsonify({"status": True, "result": work})

@app.route(create_time_complexity_of_scope_url, methods=["POST"])
def create_time_complexity_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.create_time_complexity()})




@app.route(create_mistakes_of_scope_url, methods=["POST"])
def create_mistakes_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.create_mistakes()})

@app.route(create_required_test_types_of_scope_url, methods=["POST"])
def create_required_test_types_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.create_required_test_types()})


@app.route(create_tags_of_scope_url, methods=["POST"])
def create_tags_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)
    return jsonify({"status": True, "result": the_scope.create_tags()})


@app.route(create_security_analysis_of_scope_url, methods=["POST"])
def create_security_analysis_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.create_security_analysis()})






@app.route(create_document_of_scope_url_old, methods=["POST"])
def create_document_of_scope_old():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.create_documentation_old()})

@app.route(get_type_of_scope_url, methods=["POST"])
def get_type_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.type})




@app.route(get_python_version_of_scope_url, methods=["POST"])
def get_python_version_of_scope():
    scope = request.form.get("scope")
    version = request.form.get("version")
    if version != None:
        the_scope = Scope.get_version(scope+":"+version)
    else:
        the_scope = Scope(scope)

    
    return jsonify({"status": True, "result": the_scope.python_version})



@app.route(get_all_scopes_user_url, methods=["get"])
def get_all_scopes_user():
    user = AccessKey(request.authorization.password)
    return jsonify({"status": True, "result": Scope.get_all_scopes_name(user)})


@app.route(delete_scope_url, methods=["POST"])
def delete_scope():
    scope = request.form.get("scope")
    object = Scope(scope)
    return jsonify({"status": True, "result": object.delete()})

@app.route(delete_version_url, methods=["POST"])
def delete_version():
    version = request.form.get("version")
    object = Scope.delete_version(version)
    return jsonify({"status": True, "result": object})


@app.route(get_dump_history_url, methods=["POST"])
def get_dump_history():
    scope = request.form.get("scope")
    object = Scope(scope)
    return jsonify({"status": True, "result": object.dump_history})


@app.route(get_version_history_url, methods=["POST"])
def get_version_history():
    scope = request.form.get("scope")
    object = Scope(scope)
    
    return jsonify({"status": True, "result": object.version_history})


@app.route(get_module_version_history_url, methods=["POST"])
def get_module_version_history():
    top_library = request.form.get("top_library")
    user = AccessKey(request.authorization.password)


    all_scopes_response = Scope.get_all_scopes_name_prefix(user, top_library)

    all_possible_versions = []
    for each_scope in all_scopes_response:
        scope_versions = Scope(each_scope).version_history
        for each_version in scope_versions:
            if each_version not in all_possible_versions:
                all_possible_versions.append(each_version.split(":")[1])

    return jsonify({"status": True, "result": all_possible_versions})



@app.route(load_specific_dump_url, methods=["POST"])
def load_specific_dump():
    dump_id = request.form.get("dump_id")
    object = Scope.get_dump(dump_id)
    return jsonify({"status": True, "result": object.source})

@app.route(load_specific_version_url, methods=["POST"])
def load_specific_version():
    version = request.form.get("version")
    object = Scope.get_version(version)
    return jsonify({"status": True, "result": object.source})


@app.route(get_all_scopes_name_prefix_url, methods=["POST"])
def get_all_scopes_name_prefix():
    user = AccessKey(request.authorization.password)
    prefix = request.form.get("prefix")
    return jsonify({"status": True, "result": Scope.get_all_scopes_name_prefix(user, prefix)})


@app.route(create_version_url, methods=["POST"])
def create_version():
    user = AccessKey(request.authorization.password)
    version = request.form.get("version")
    scope = request.form.get("scope")
    object = Scope(scope)
    return jsonify({"status": True, "result": object.create_version(version, user)})

@app.route(dump_requirements_url, methods=["POST"])
def dump_requirements():
    scope = request.form.get("scope")
    settings = request.form.get("requirements")

    the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.set_requirements(settings)})

@app.route(dump_settings_url, methods=["POST"])
def dump_settings():
    scope = request.form.get("scope")
    settings = request.form.get("settings")

    the_settings = {}
    for key,value in request.form.items():
        if key != "scope":
            the_settings[key] = value

    the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.set_settings(the_settings)})




@app.route(dump_python_version_url, methods=["POST"])
def dump_python_version():
    scope = request.form.get("scope")
    python_version = request.form.get("python_version")

    the_scope = Scope(scope)

    return jsonify({"status": True, "result": the_scope.set_python_version(python_version)})




@app.route(search_by_documentation_url, methods=["POST"])
def search_by_documentation():
    question = request.form.get("question")
    min_score = float(request.form.get("min_score", 0))
    how_many_result = int(request.form.get("how_many_result", 10))

    user = AccessKey(request.authorization.password)
    scopes = Scope.get_all_scopes_with_documentation()

    the_read_scopes = user.scopes_read

    if len(scopes) == 0:
        return jsonify({"status": False, "result": "No scope has documentation"})

    results = AI.search_by_documentation(scopes, question, min_score, how_many_result)

    # Remove the results that not able to access by the user 
    access_control_list = []
    for result in results:
        if result[0] in the_read_scopes or user.is_admin:
            access_control_list.append(result)

    return jsonify({"status": True, "result": access_control_list})




@app.route(ai_completion_url, methods=["POST"])
def ai_completion():
    message = request.form.get("message")
    model = request.form.get("model")
    result = None
    if model != None:
        result = AI.completion(message, model)
    else:
        result = AI.default_completion(message)
    return jsonify({"status": True, "result": result})


@app.route(get_default_ai_model, methods=["get"])
def get_default_ai_model():
    return jsonify({"status": True, "result": AI.default_model})


@app.route(create_readme_url, methods=["POST"])
def create_readme():
    global documentation_tasks
    top_library = request.form.get("top_library")
    version = request.form.get("version")


    all_scopes_response = Scope.get_all_scopes_name_prefix(AccessKey(request.authorization.password), top_library)
    all_scopes = []
    for each_scope in all_scopes_response:
        if version != None:
            the_version_history_response = Scope(each_scope).version_history
            the_version_history = []
            for element in the_version_history_response:
                the_version_history.append(element.replace(each_scope+":", ""))
            if version in the_version_history:
                all_scopes.append(each_scope)
        else:
            all_scopes.append(each_scope)

    # order by alphabetical
    all_scopes.sort()

    result = f"{top_library}"
    for i in all_scopes:
        result += i + "\n"
    


    summary_list = ""
    for each_scope in all_scopes:
            task_name = each_scope
            if version == None:
                the_scope = Scope(each_scope)
            else:
                task_name = each_scope+":"+version
                the_scope = Scope.get_version(each_scope+":"+version)

            while task_name in documentation_tasks:
                time.sleep(1)    

            if the_scope.documentation == None:
                documentation_tasks.append(task_name)
                the_scope.create_documentation()
                try:
                    documentation_tasks.remove(task_name)
                except:
                    pass


            summary_list += each_scope +" - " + str(the_scope.type) + "\n"
            summary_list += str(the_scope.documentation) + "\n\n"


    print("SUMMARY LIST: ", summary_list)

    #Create sha256 hash of the result
    sha256 = hashlib.sha256((summary_list+top_library).encode()).hexdigest()

    result = AI.generate_readme(top_library, summary_list)

    storage_4.set(sha256, result)

    return jsonify({"status": True, "result": result})

@app.route(get_readme_url, methods=["POST"])
def get_readme():
    top_library = request.form.get("top_library")
    version = request.form.get("version")
    all_scopes_response = Scope.get_all_scopes_name_prefix(AccessKey(request.authorization.password), top_library)
    all_scopes = []
    for each_scope in all_scopes_response:
        if version != None:
            the_version_history_response = Scope(each_scope).version_history
            the_version_history = []
            for element in the_version_history_response:
                the_version_history.append(element.replace(each_scope+":", ""))
            if version in the_version_history:
                all_scopes.append(each_scope)
        else:
            all_scopes.append(each_scope)
    
    print("ALL SCOPES: ", all_scopes)

    # order by alphabetical
    all_scopes.sort()

    result = f"{top_library}"
    for i in all_scopes:
        result += i + "\n"

    summary_list = ""
    for each_scope in all_scopes:
            task_name = each_scope
            if version == None:
                the_scope = Scope(each_scope)
            else:
                task_name = each_scope+":"+version
                the_scope = Scope.get_version(each_scope+":"+version)

            while task_name in documentation_tasks:
                time.sleep(1)    

            if the_scope.documentation == None:
                documentation_tasks.append(task_name)
                the_scope.create_documentation()
                try:
                    documentation_tasks.remove(task_name)
                except:
                    pass



            summary_list += each_scope +" - " + str(the_scope.type) + "\n"
            summary_list += str(the_scope.documentation) + "\n\n"


    print("SUMMARY LIST: ", summary_list)

    
    #Create sha256 hash of the result
    sha256 = hashlib.sha256((summary_list+top_library).encode()).hexdigest()

    return jsonify({"status": True, "result": storage_4.get(sha256)})



@app.route(get_openai_api_key_user, methods=["get"])
def get_openai_api_key_user():
    the_result = AccessKey(request.authorization.password).openai_api_key
    special = True
    if the_result == None:
        the_result = openai_api_key
        special = False

    the_result = {"api_key": the_result, "special": special}
    return jsonify({"status": True, "result": the_result})



@app.route(create_version_prefix_url, methods=["post"])
def create_version_prefix():
    user = AccessKey(request.authorization.password)
    top_library = request.form.get("top_library")
    version = request.form.get("version")
    all_scopes = Scope.get_all_scopes_name_prefix(user, top_library)
    write_scopes = user.scopes_write
    for each_scope in all_scopes:
        if each_scope in write_scopes or user.is_admin:
            Scope(each_scope).create_version(version, user)

    jsonify({"status": True, "result": True})



@app.route(delete_version_prefix_url, methods=["post"])
def delete_version_prefix():
    user = AccessKey(request.authorization.password)
    top_library = request.form.get("top_library")
    version = request.form.get("version")


    all_scopes = Scope.get_all_scopes_name_prefix(user, top_library)
    write_scopes = user.scopes_write
    for each_scope in all_scopes:
        if each_scope in write_scopes or user.is_admin:
            try:
                Scope(each_scope).delete_version(each_scope+":"+version)
            except:
                pass

    jsonify({"status": True, "result": True})    