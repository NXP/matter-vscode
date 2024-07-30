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

import click

from platforms.k32w0 import K32W0
from platforms.k32w1 import K32W1
from platforms.mcxw71 import MCXW71
from platforms.rw61x import RW61X

PLATFORMS = {
    "k32w0": K32W0,
    "k32w1": K32W1,
    "mcxw71": MCXW71,
    "rw61x": RW61X
}

@click.command()
@click.option("--platform", default=None, help="Platform name")
def main(platform):
    """Utility script to run pre flash actions for different platforms.
    Examples: loading factory data, writing the radio firmware etc.
    """

    try:
        PLATFORMS[platform]().run_actions()
    except KeyError as _:
        print(f"{platform} is not supported")
        print(f"Here is a list of supported platforms: {list(PLATFORMS.keys())}")

if __name__ == "__main__":
    main()
