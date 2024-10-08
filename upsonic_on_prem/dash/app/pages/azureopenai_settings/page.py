# Page Informations
from app.pages.utils import get_current_directory_name

name = "Azure OpenAI Settings"
location = get_current_directory_name()
hiden = True
#


from django.urls import path
from dash.logs import logger
from django.shortcuts import render
from django.shortcuts import redirect
from app.api_integration import API_Integration
from django.contrib.auth.decorators import login_required


@login_required
def view(request):
    logger.debug("Hi")
    result = None

    if request.method == "POST":
        azureopenai_baseurl_ = request.POST.get("azureopenai_baseurl")
        azureopenai_key_ = request.POST.get("azureopenai_key")
        azureopenai_searchdeployment_ = request.POST.get("azureopenai_searchdeployment")
        azureopenai_version_ = request.POST.get("azureopenai_version")

        if azureopenai_baseurl_:
            API_Integration(request.user.access_key).change_azureopenai_baseurl(azureopenai_baseurl_)
            result = "Azure OpenAI Base URL Updated"
        
        if azureopenai_key_:
            API_Integration(request.user.access_key).change_azureopenai_key(azureopenai_key_)
            result = "Azure OpenAI Key Updated"

        if azureopenai_searchdeployment_:
            API_Integration(request.user.access_key).change_azureopenai_searchdeployment(azureopenai_searchdeployment_)
            result = "Azure OpenAI Search Deployment Updated"

        
        if azureopenai_version_:
            logger.info("verison")
            logger.info(azureopenai_version_)
            API_Integration(request.user.access_key).change_azureopenai_version(azureopenai_version_)
            result = "Azure OpenAI Version Updated"

    azureopenai = API_Integration(request.user.access_key).view_azureopenai()
    azureopenai_baseurl = API_Integration(request.user.access_key).view_azureopenai_baseurl()
    azureopenai_key = API_Integration(request.user.access_key).view_azureopenai_key()

    azureopenai_version = API_Integration(request.user.access_key).view_azureopenai_version()

    if azureopenai_key:
        the_length = len(azureopenai_key)
        azureopenai_key = "*" * the_length



    if azureopenai_baseurl == None:
        azureopenai_baseurl = ""

    if azureopenai_key == None:
        azureopenai_key = ""

    if azureopenai_version == None:
        azureopenai_version = ""

    

    data = {
        "page_title": name,
        "azureopenai": azureopenai,
        "azureopenai_baseurl": azureopenai_baseurl, 
        "azureopenai_key": azureopenai_key,         
        "azureopenai_version": azureopenai_version, 
        "result": result,
    }
    return redirect(to="AI Providers")


url = path(location, view, name=name)
