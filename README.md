## Metadata for NXP Matter support in VSCode

This repository contains the Matter metadata needed by NXP MCUXpresso for VSCode
extension in order to support in-tree Matter reference applications for multiple
platforms.

-   [Metadata for NXP Matter support in VSCode](#metadata-for-nxp-matter-support-in-vscode)
    -   [Prerequisites](#prerequisites)
    -   [Directory structure](#directory-structure)
    -   [Scripts](#scripts)

### Prerequisites

The scripts are using some tools provided by
[SPSDK](https://spsdk.readthedocs.io/en/latest/).

To install the preqrequisite Python modules, run this command from Matter root
folder:

```
pip install -r matter-vscode-for-mcux/requirements.txt
```

### Directory structure

| File/folder | Content                                                         |
| ----------- | --------------------------------------------------------------- |
| platforms   | The place for metadata, binaries, images specific to a platform |
| scripts     | Scripts that can be referenced in the metadata                  |

### Scripts

Currently, usage of `flash_utils` script is pretty simple, since it has only the
`--platform` option:

```
python ./scripts/flash_utils.py --platform <platform_name>
```

This will run the pre flash actions specific to the specified platform.

Some examples of pre flash actions are:

-   loading factory data
-   loading a secondary stage bootloader (SSBL)
-   loading radio firmware (NBU)
-   writing image directories needed by SSBL
