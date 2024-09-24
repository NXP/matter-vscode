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

from .utils.platform import K32W0_SDK
from .utils.platform import Platform
from .utils.tools import DK6Prog

# This assumes that the matter-vscode-for-mcux repo is cloned in Matter root path.
ssbl_path = os.path.abspath(os.path.join(K32W0_SDK, "examples/k32w061dk6/wireless_examples/framework/ssbl/binary/ssbl_ext_flash_pdm_support.bin"))

class K32W0(Platform):

    def __init__(self):
        super().__init__()

        self.tool = DK6Prog()
        self.tool.add_action(["erase", "0", "0x9de00"])
        self.tool.add_action(["write", "0", ssbl_path])
        self.tool.add_action(["write", "0x9d600", self.get_binary("example-factory-data.bin")])
        self.tool.add_action(["write", "0x160", "{{0000000010000000}}", "8", "PSECT"])
        self.tool.add_action(["write", "0x168", "{{00400000C9040101}}", "8", "PSECT"])

    def pre_message(self):
        print("Please set up the DK6 board for pre flash actions:")
        print(" - set the J4 and J7 jumpers to the middle position (JN UART0 - FTDI)")
        print(" - connect the board to the connector marked with FTDI USB")
        print(" - connect the board to the connector marked with LPC-Link2 USB")
