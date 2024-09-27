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

import subprocess

from spsdk.dk6.dk6device import DK6Device
from spsdk.dk6.driver import DriverInterface
from spsdk.apps.dk6prog import get_default_backend

from spsdk.utils import nxpdevscan


class Tool:
    """Defines a common API for pre flash tools.
    
    Each derived class (specific tool) shall define a way of
    identifying the connected device (self.identifier) and
    shall specify the cli command to access the tool: e.g. jlink
    """

    def __init__(self):
        self.actions = list()
        self.cmd = list()
        self.identifier = None

    def run_actions(self):
        for action in self.actions:
            subprocess.run(self.cmd + action, check=True)

    def add_action(self, action):
        self.actions.append(action)
    
    def is_connected(self):
        return self.identifier != None


class DK6Prog(Tool):
    """Wrapper over dk6prog CLI."""

    def __init__(self):
        super().__init__()

        interface = DriverInterface(get_default_backend())
        devices = interface.list_devices()
        if devices:
            self.identifier = devices[0].device_id
        self.cmd = ["dk6prog", "-d", str(self.identifier)]


class BlHost(Tool):
    """Wrapper over blhost CLI."""

    def __init__(self):
        super().__init__()

        nxp_uart_devices = nxpdevscan.search_nxp_uart_devices()
        if nxp_uart_devices:
            self.identifier = nxp_uart_devices[0].name
        self.cmd = ["blhost", "-p", self.identifier]
