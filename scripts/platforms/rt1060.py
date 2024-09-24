#!/usr/bin/env python3
#
#    Copyright 2024 NXP
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import os

from .utils.platform import Platform
from .utils.tools import BlHost

class RT1060(Platform):

    def __init__(self):
        super().__init__()

        self.tool = BlHost()
        self.tool.add_action(["flash-erase-region", "0x607df000", "8192"])
        self.tool.add_action(["write-memory", "0x607df000", self.get_binary("example-factory-data.bin"), "8192"])
        self.tool.add_action(["reset"])
