# XSettingsImport

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSettingsImport.html

---

```
 Imports project-, station-, company- or user settings from an XML file.

```

| Parameter | Description |
| --- | --- |
| ``` XmlFile
 ``` | ```  Full name of an XML file. If the param is empty, a file selection dialog will appear to choose an XML file.
 ``` |
| ``` Node
 ``` | ```  Node of settings to import
 ``` |
| ``` Project
 ``` | ```  Full name of the target project
 ``` |

**Example**

```
 Imports all station-, company- and user settings from a given XML file:

 XSettingsImport /XmlFile:c:\file.xml

 Imports only the node from a given XML file:

 XSettingsImport /XmlFile:c:\file.xml /Node:User.XSbGui.CustomSymbols

 Imports project settings to target project from a given XML file:

 XSettingsImport /XmlFile:c:\my_project.xml /Project:c:\...\EPLAN_Sample_Project.elk

 Imports only the project setting nodes into the target project from a given XML file:

 XSettingsImport /XmlFile:c:\my_project.xml /Project:c:\...\EPLAN_Sample_Project.elk /Node:XSbGui.CustomSymbols

```