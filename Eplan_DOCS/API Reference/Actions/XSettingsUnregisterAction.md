# XSettingsUnregisterAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsUnregisterAction.html

---

```
 Unregistration of Add-ons.

```

| Parameter | Description |
| --- | --- |
| ``` path
 ``` | ``` The path where the Add-on is located, e.g. "..\addon\1.0.0". Alternative to the parameter "installFile".
 ``` |
| ``` installFile
 ``` | ``` The complete path of the install.xml file. Alternative to the parameter "path".
 ``` |

**Example**

```
 Registering Add-ons with the path in which the Add-on is located:

 XSettingsUnregisterAction /Path:c:\MyAddOn

 Registering Add-ons with the complete path of the install.xml file:

 XSettingsUnregisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml

```