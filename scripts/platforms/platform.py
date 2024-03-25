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


class Platform:
    """Defines a common API for pre flash actions for different platforms."""

    def __init__(self):
        """The list of actions should be populated here in derived classes."""
        self.tool = list()
        self.actions = list()

    def run(self):
        """This is the main function called when a platform is given as input."""
        print("run should be implemented in derived class.")
        pass

    def pre_message(self):
        """This message is printed when there is something wrong with the connection."""
        print("pre_message should be implemented in derived class.")
        pass

    def post_message(self):
        """This message is printed at the end of the run actions."""
        print("post_message should be implemented in derived class.")
        pass

    def run_actions(self, connection):
        """This should be called by run in concrete classes.
        
        connection is a string that should contain the serial port, the device name
        or any identifier used by the flashing tool.
        """
        if connection:
            for action in self.actions:
                subprocess.run(self.tool + [connection] + action)
            self.post_message()
        else:
            self.pre_message()
