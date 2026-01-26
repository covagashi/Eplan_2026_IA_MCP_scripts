# generatemacros

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/generatemacros.html

---

```
Action for generating macros from project.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be considered (optional), where n is a number e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc. 
 ``` |
| ``` INSTALLATIONSPACENAMEn
 ``` | ``` Names of the InstallationSpaces to be considered (optional), where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /INSTALLATIONSPACENAME2:BR2 /INSTALLATIONSPACENAME:BR3 etc.
 ``` |
| ``` STRUCTUREn
 ``` | ``` Structure identifiers of the InstallationSpaces to be exported (optional), where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /STRUCTURE1:=EB3+ET1 /INSTALLATIONSPACENAME2:BR2 /STRUCTURE2:=EB3+ET2 etc.
 ``` |
| ``` WINDOWMACRODIR
 ``` | ``` Window macro directory
 ``` |
| ``` PAGEMACRODIR
 ``` | ``` Page macro directory
 ``` |
| ``` FILTERSCHEME
 ``` | ``` Filter  scheme
 ``` |
| ``` OVERWRITE
 ``` | ``` Overwrite already existing files
 ``` |

**Remarks**

```
For preparation of macros please use the PrepareMacros action instead.

Project must have property "Type of project" set to "Macro project".                    

```

**Example**

```
Macros generation

generatemacros /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```