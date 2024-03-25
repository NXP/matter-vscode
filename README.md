## Metadata for NXP Matter support in VSCode

This repository contains the Matter metadata needed by NXP VSCode extension
in order to support in-tree Matter reference applications for multiple platforms.

## Prerequisites
The scripts are using some tools provided by [SPSDK](https://spsdk.readthedocs.io/en/latest/spsdk.html).

To install the preqrequisite Python modules:
```
pip install -r requirements.txt
```

## Directory structure
| File/folder | Content                                                         |
| ----------- | --------------------------------------------------------------- |
| platforms   | The place for metadata, binaries, images specific to a platform | 
| scripts     | Scripts that can be referenced in the metadata                  |

## Scripts
Currently, usage of `flash_utils` script is pretty simple, since it has only the `--platform` option:
```
python ./scripts/flash_utils.py --platform <platform_name>
```
This will run the pre flash actions specific to the specified platform.

Some examples of pre flash actions are:
- loading factory data
- loading a secondary stage bootloader (SSBL)
- loading radio firmware (NBU)
- writing image directories needed by SSBL
