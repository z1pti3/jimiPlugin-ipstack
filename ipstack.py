import jimi

class _ipstack(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("ipstackIPLookup","_ipstackIPLookup","_action","plugins.ipstack.models.action")
        jimi.model.registerModel("ipstackMyIP","_ipstackMyIP","_action","plugins.ipstack.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("ipstackIPLookup","_ipstackIPLookup","_action","plugins.ipstack.models.action")
        jimi.model.deregisterModel("ipstackMyIP","_ipstackMyIP","_action","plugins.ipstack.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
