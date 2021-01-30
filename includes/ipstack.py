import requests
import json
import time
from pathlib import Path

class _ipstack():
    hostname = "api.ipstack.com"
    
    def __init__(self, apiToken, secure=False, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.apiToken = apiToken
        self.url = "http://{0}".format(self.hostname)
        if secure:
            self.url = "https://{0}".format(self.hostname)
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            if methord == "GET":
                response = requests.get("{0}/{1}".format(self.url,endpoint), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        return None, response.status_code

    def ipLookup(self,ip,fields=[],hostname=False,security=False,language="en"):
        if type(ip) is str:
            uri = ip
        elif type(ip) is list:
            uri = ",".join(ip)
        uri += "?access_key={0}".format(self.apiToken)
        if fields:
            uri += "&fields=" + ",".join(fields)
        if hostname:
            uri += "&hostname=1"
        if security:
            uri += "&security=1"
        uri += "&output=json"
        response, statusCode = self.apiCall(uri)
        try:
            del response["location"]["country_flag_emoji"]
        except KeyError:
            pass
        return response, statusCode

    def myIP(self):
        uri = "check"
        uri += "?access_key={0}".format(self.apiToken)
        response, statusCode = self.apiCall(uri)
        try:
            del response["location"]["country_flag_emoji"]
        except KeyError:
            pass
        return response, statusCode
