# ImportPrePlanningData

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ImportPrePlanningData.html

---

```
Action to import pre-planning data.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` FILENAME
 ``` | ``` Full file name of target file. This parameter is mandatory.
 ``` |
| ``` SCHEMENAME
 ``` | ``` Name of the scheme that defines the assignment of the external data fields to the EPLAN properties. This parameter is mandatory.
 ``` |
| ``` TABLENAME
 ``` | ``` If import is done from excel file then this parameter is used. It is a name of table or data area contained in the data source.
 ``` |
| ``` DELIMITER
 ``` | ``` If import is done from text file then this parameter is used. It is used to determine the separator that is used in the text file in order to separate the columns.
 ``` |
| ``` HEADER
 ``` | ``` If 1then column names from the data table are output in the External field  column of the assignment table. If 0the import ignores the column names.
 Used only for import from excel file. Parameter is optional. Default = 0(No).
 ``` |
| ``` TARGETNAME
 ``` | ``` Name of object (DMPLAOBJECT_FULLDESIGNATION) below which the imported data are to be inserted. If parameter not exists then data are inserted under project.
 ``` |
| ``` SKIPERRORS
 ``` | ``` If 1 the import will not be aborted because of errors and messages that occur. Parameter is optional. Default = 1(Yes).
 ``` |
| ``` OVERWRITE
 ``` | ``` If 1then existing planning objects will be overwritten with the data from the planning objects of the same name from the import file.
 If 0 then existing planning objects remain unchanged. Parameter is optional. Default = 1(Yes).
 ``` |
| ``` UPDATEONLY
 ``` | ``` If 1 then only data of existing structure segments and planning objects will be updated. Parameter is optional. Default = 0(No).
 ``` |

**Example**

```
Importing pre-planning data from excel file:  

ImportPrePlanningData /PROJECTNAME:C:\Projects\EPLAN_Sample_Project.elk /FILENAME:C:\Projects\EPLAN\preplanning.xls     /SCHEMENAME:config_scheme       /HEADER:1 /SKIPERRORS:0 /UPDATEONLY:0

```