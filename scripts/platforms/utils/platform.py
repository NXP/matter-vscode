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
import sys


class Platform:
    """Defines a common API for pre flash actions for different platforms."""

    def __init__(self):
        """The list of actions should be populated here in derived classes."""
        self.tool = None

    def pre_message(self):
        """This message is printed when there is something wrong with the connection.
        
        Can be reimplemented in derived classes to inform the user regarding the
        board state: e.g. some actions require the board to be put in ISP mode.
        """
        pass

    def post_message(self):
        """This message is printed at the end of the run actions."""
        print("Board is ready for application flashing")
        pass

    def run_actions(self):
        """This should be called by run in concrete classes."""
        if self.tool.is_connected():
            self.tool.run_actions()
            self.post_message()
        else:
            # Inform caller that the board must be set up correctly.
            self.pre_message()
            sys.exit(1)
