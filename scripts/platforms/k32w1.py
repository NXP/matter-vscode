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

from .platform import Platform

from spsdk.utils import nxpdevscan

# This assumes that the repo is a submodule inside the Matter repository.
# Otherwise, the relative path will not work.
github_sdk = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../github_sdk/rw_k32w1/repo'))

class K32W1(Platform):

    def __init__(self):
        super().__init__()

        self.tool = ["blhost", "-p"]
        self.actions.append(["receive-sb-file", "metadata/k32w1/binaries/example-nbu.sb3"])
        self.actions.append(["flash-erase-region", "0xf4000", "8192"])
        self.actions.append(["write-memory", "0xf4000", "metadata/k32w1/binaries/example-factory-data.bin", "8192"])

    def run(self):
        uart_device = None
        nxp_uart_devices = nxpdevscan.search_nxp_uart_devices()
        if nxp_uart_devices:
            uart_device = nxp_uart_devices[0].name
        self.run_actions(uart_device)

    def pre_message(self):
        print("Please place the board in ISP mode:")
        print(" - place jumper on JP25")
        print(" - press and hold SW4, press and release Reset, then release SW4")

    def post_message(self):
        print("Board is ready for application flashing")
