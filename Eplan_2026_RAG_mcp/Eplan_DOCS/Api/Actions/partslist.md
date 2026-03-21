# partslist

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/partslist.html

---

```
Action class for exporting and importing parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements. Allows also to delete stored properties.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 '¢ "IMPORT": Import parts lists
 '¢ "EXPORT": Export parts lists
 '¢ "IMPORTTOSYSTEM": Import to parts management
 '¢ "EXPORTFROMSYSTEM": Export from parts management
 '¢ "DELETESTOREDPROPERTIES": Delete stored properties from project
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` The directory and the file name of the file to be imported must be specified here. This only applies to "IMPORT".
 ``` |
| ``` EXPORTFILE
 ``` | ``` The directory and the file name of the file to be exported must be specified here. The file extension is automatically added by the system. This only applies to "EXPORT"
 ``` |
| ``` FORMAT
 ``` | ``` File format ("XPalXmlExporter","XPalCSVConverter", or user-defined format) (optional). 
 For parts management ("XPamImportXml" and "XPamExportXml")
 '¢ "XPalXmlExporter" is the default format value for tasks of TYPE "IMPORT" and "EXPORT".
 '¢ "XPamExportXml" is the default format value for tasks of TYPE "IMPORTTOSYSTEM" and "EXPORTFROMSYSTEM".
 See also "XMLConverter" and "XMLConverterCategories" namespace.
 ``` |
| ``` FIELDASSIGNMENTSCHEME
 ``` | ``` Name of scheme that is used to assign fields in some article properties (optional).
 ``` |
| ``` MODE
 ``` | ``` Import mode (optional).
 Supported modes are:
 '¢ 0: Append new records only
 '¢ 1: Update existing records only
 '¢ 2: Update existing records and append new ones
 Default value = 0, append new records only. If an invalid value is set, the default value 0 will be used.
 ``` |
| ``` ADDITIONAL_LANGUAGE
 ``` | ``` Valid only when TYPE has "IMPORTTOSYSTEM" value (optional).
 If the value of this parameter is 1, multi-language properties will be updated with another language values rather than being replaced with the file's content.
 If the parameter is omitted, content of the file replaces values of multi-language properties.
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Configuration scheme for deleting stored properties (optional).
 Default value: Recent configuration scheme. The most recently used scheme is taken if an empty string is passed. This applies only to delete stored properties.
 ``` |

**Remarks**

```
When an error occurs during a parts list operation, a "BaseException" is thrown.

```

**Example**

```
Export:

partslist /TYPE:EXPORT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk    /FORMAT:XPalCSVConverter /EXPORTFILE:C:\temp\PartsList.csv

Import:

partslist /TYPE:IMPORT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk    /FORMAT:XPalCSVConverter /IMPORTFILE:C:\temp\PartsList.csv

Deletes stored properties from a project.

partslist /TYPE:DELETESTOREDPROPERTIES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /CONFIGSCHEME:config_scheme

Use the most recent configuration scheme: The 'CONFIGSCHEME'

parameter is not entered.

partslist /TYPE:DELETESTOREDPROPERTIES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```