"""
Created by auto_sdk on 2020.11.25
"""
from api.base import RestApi


class OapiProcessinstanceFileUrlGetRequest(RestApi):
    def __init__(self, url=None):
        RestApi.__init__(self, url)
        self.request = None

    def getHttpMethod(self):
        return 'POST'

    def getapiname(self):
        return 'dingtalk.oapi.processinstance.file.url.get'