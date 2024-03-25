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

from .platform import Platform

from spsdk.dk6.dk6device import DK6Device
from spsdk.dk6.driver import DriverInterface
from spsdk.apps.dk6prog import get_default_backend


class K32W0(Platform):

    def __init__(self):
        super().__init__()

        self.tool = ["dk6prog", "-d"]
        self.actions.append(["erase", "0", "0x9de00"])
        self.actions.append(["write", "0", "metadata/k32w0/binaries/example-ssbl.bin"])
        self.actions.append(["write", "0x9d600", "metadata/k32w0/binaries/example-factory-data.bin"])
        self.actions.append(["write", "0x160", "{{0000000010000000}}", "8", "PSECT"])
        self.actions.append(["write", "0x168", "{{00400000C9040101}}", "8", "PSECT"])

    def run(self):
        device_id = None
        interface = DriverInterface(get_default_backend())
        devices = interface.list_devices()
        if devices:
            device_id = devices[0].device_id
    
        self.run_actions(device_id)

    def pre_message(self):
        print("Please set up the DK6 board for pre flash actions:")
        print(" - connect the board to the connector marked with FTDI USB")
        print(" - set the J4 and J7 jumpers to the middle position (JN UART0 - FTDI)")

    def post_message(self):
        print("Please set up the DK6 board for application flashing:")
        print(" - connect the board to the connector marked with LPC-Link2 USB")
        print(" - set the J4 and J7 jumpers to the left position (JN UART0 - LPC)")
