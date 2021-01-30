import jimi
from plugins.ipstack.includes import ipstack

class _ipstackIPLookup(jimi.action._action):
    apiToken = str()
    ip = str()
    fields = list()
    includeHostname = True
    includeSecurity = True
    secure = False
    
    def run(self,data,persistentData,actionResult):
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})
        
        result, statusCode = ipstack._ipstack(apiToken,secure=self.secure).ipLookup(ip,self.fields,self.includeHostname,self.includeSecurity)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["ipInfo"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from ipstack API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_ipstackIPLookup,self).setAttribute(attr,value,sessionData=sessionData)

class _ipstackMyIP(jimi.action._action):
    apiToken = str()
    secure = False
    
    def run(self,data,persistentData,actionResult):
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        ip = jimi.helpers.evalString(self.ip,{"data" : data})
        
        result, statusCode = ipstack._ipstack(apiToken,secure=self.secure).myIP()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["ipInfo"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from ipstack API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_ipstackMyIP,self).setAttribute(attr,value,sessionData=sessionData)