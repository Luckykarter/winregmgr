# winregmgr
[![PyPI](https://img.shields.io/pypi/v/winregmgr)](https://pypi.org/project/winregmgr/)

Helper library that allows to read/write from/to Windows Registry via simplified syntax of Python contextmanager.

## Install:

```bash  
$ pip install winregmgr
```  

## Usage Samples:

```Python
from winregmgr import OpenKey
import winreg   # for accessing constants

# Read parameter from Registry:
with OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\ODBC\ODBC.INI\MS Access Database\\") as reg_key:
  value = reg_key.get_value("Driver")
  
# If parameter is read only - optional access type has to be explicitly set:
with OpenKey(winreg.HKEY_LOCAL_MACHINE, "Read Only Path", access=winreg.KEY_READ) as reg_key:
  value = reg_key.get_value("Driver")
 
# Read all parameters under given path into dictionary
with OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\") as reg_key:
  values = reg_key.get_values()
 
# Write Parameter if path does not exist - creates it
with OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\") as reg_key:
  reg_key.set_value("Parameter", "Its value")
 
# Delete Parameter
with OpenKey(winreg.HKEY_CURRENT_USER, r"PATH\TO\PARAMETER\\") as reg_key:
  reg_key.delete_value("Parameter")

```


