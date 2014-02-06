 # Copyright 2012-2014 inBloom, Inc. and its affiliates.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 # http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.

import calendar
import os
import time
class LastChefRun:
    def __init__(self, agentConfig, checksLogger, rawConfig):
                self.agentConfig = agentConfig
                self.checksLogger = checksLogger
                self.rawConfig = rawConfig

    def run(self):
        data = { }
	data['LastGoodRun'] = int(calendar.timegm(time.gmtime()) - os.stat("/var/chef/reports/last-good-run.json").st_mtime)
        return data
