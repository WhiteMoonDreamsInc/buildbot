    @defer.inlineCallbacks
    def run_vc(self, branch, revision, patch):
        self.stdio_log = yield self.addLogForRemoteCommands("stdio")
            yield self.patch(patch)
        return SUCCESS
        build = yield self.doForceBuild(wantSteps=True, wantLogs=True,
                                        forceParams={'foo_patch_body': PATCH})