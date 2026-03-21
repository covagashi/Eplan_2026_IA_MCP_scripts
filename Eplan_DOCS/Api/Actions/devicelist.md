# devicelist

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/devicelist.html

---

```
Action class for device list functions: import, export, and delete device lists.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "IMPORT": Import device list
 '¢ "EXPORT": Export device list
 '¢ "DELETE": Delete device list 
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is calledfrom GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` The directory and the file name of       the device list to be imported must be specified here.
 ``` |
| ``` EXPORTFILE
 ``` | ``` The directory and the file name of       the device list to be exported must be specified here.
 ``` |
| ``` FORMAT
 ``` | ``` Optional: File format ("XDLXmlExporter","XDLTxtImporterExporter", "XDLCsvImporterExporter", or        user-defined format)
 Default= XDLXmlExporter
 ``` |

**Remarks**

```
When an error occurs during a device list operation, a "BaseException" is thrown.

```

**Example**

```
import:

devicelist /TYPE:IMPORT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /IMPORTFILE:C:\EPLAN\deviceListe.xml

export:

devicelist /TYPE:EXPORT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /EXPORTFILE:C:\EPLAN\deviceListe2.xml

delete:

devicelist /TYPE:DELETE /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```