# EplApiModuleAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/EplApiModuleAction.html

---

```
 Loads and registers an API Add-in.

```

| Parameter | Description |
| --- | --- |
| ``` register
 ``` | ```  File name of the  Add-in DLL to be registered. If no absolute file name is specified, the file name is preceeded with system's current directory.
 ``` |
| ``` registerModule
 ``` | ``` Register an API Module. The Settings must be available, then the services are created.
 ``` |
| ``` unregister
 ``` | ```  Assembly file title of the Add-in to be de-registered. The file title is the one displayed in the API module dialog. (This is the name of the assembly without path and without the ending .dll)
 ``` |
| ``` unregisterInternal
 ``` | ```  Assembly file title of the Add-in to be de-registered. When an error makes the unload impossible, the module is only deregistered.
 ``` |

**Example**

```
 Action call to load an Add-in.

      EPLAN.exe /Variant:"Electric P8" EplApiModuleAction /register:"C:Program Files\\EPLAN\\Platform\\...\\bin\\Eplan.EplAddIn.MyAddin3.dll"

      EPLAN.exe /Variant:"Electric P8" EplApiModuleAction /unregister:"Eplan.EplAddIn.MyAddin3"

```