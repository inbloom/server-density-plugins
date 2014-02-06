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

import re
class FreeMemory:
    def __init__(self, agentConfig, checksLogger, rawConfig):
                self.agentConfig = agentConfig
                self.checksLogger = checksLogger
                self.rawConfig = rawConfig

    def run(self):
        data = { }
        with open("/proc/meminfo") as fd:
            for line in fd:
                if "MemFree" in line:
                    data['MemFree'] = int(re.findall('\d+', line)[0])
                elif "Buffers" in line:
                    data['Buffers'] = int(re.findall('\d+', line)[0])
                elif re.match('^Cached', line):
                    data['Cached'] = int(re.findall('\d+', line)[0])
        data['AvailableMemory'] = data['MemFree'] + data['Buffers'] + data['Cached']
        return data
