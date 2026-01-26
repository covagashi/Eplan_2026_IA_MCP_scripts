# PathMap

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap.html

---

This class enables you access to the functions used for processing strings that could contain EPLAN path variables.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.PathMap**

Syntax

**C#**



public class PathMap

public ref class PathMap


Remarks

Here are available EPLAN path variables: $(PROJPROP\_<ID>)Project property. In order to identify such a path variable, the ID of the respective property is included in the name.

| Path variable | Meaning |
| --- | --- |
| $(BIN) | A program directory generated on installation contains the program libraries (\*.dll) of the individual modules. |
| $(CFG) | A configuration directory generated on installation containing the xml files of the individual modules. |
| $(CFG\_COMPANY) | Configuration directory generated on installation, contains the company settings. |
| $(CFG\_STATION) | Configuration directory generated on installation, contains the station settings. |
| $(CFG\_USER) | Configuration directory generated on installation, contains the user settings. |
| $(DOC) | Project-specific directory for documents. |
| $(EPLAN) | An upper-level main directory generated on installation. |
| $(EPLAN\_DATA) | A superior directory for master data, generated on installation. |
| $(EPLAN\_EXECUTABLE) | The directory to Eplan.exe. |
| $(ENVVAR\_<Variable\_Name>) | OS environment variable. |
| $(EPLAN\_VARIANT) | Name of the started product variant. |
| $(EPLAN\_VERSION) | Version number of the used Eplan. |
| $(EPLAN\_VERSION\_SHORT) | Main version number of the used Eplan. |
| $(IMG) | Project-specific directory for images. |
| $(LOCALDATE) | Current local date. |
| $(LOCALTIME) | Current local time. |
| $(MD\_DOCUMENTS) | The directory for documents defined under Options > Settings > User > Management > Directories. |
| $(MD\_DXFDWG) | The directory for DXF / DWG files defined under Options > Settings > User >Management > Directories. |
| $(MD\_FCTDEFS) | The directory for function definitions available under Options > Settings >User > Management > Directories. |
| $(MD\_FORMS) | The directory for forms defined under Options > Settings > User > Management > Directories. |
| $(MD\_FRAMES) | The directory for plot frames defined under Options > Settings > User >Management > Directories. |
| $(MD\_IMG) | The directory for images defined under Options > Settings > User > Management > Directories. |
| $(MD\_MACROS) | The directory for macros and outlines defined under Options > Settings >User > Management > Directories. |
| $(MD\_MECHANICALMODELS) | The directory for mechanical models defined under Options > Settings >User > Management > Directories. |
| $(MD\_PARTS) | The directory for parts defined under Options > Settings > User >Management > Directories. |
| $(MD\_PROJECTS) | The directory for projects defined under Options > Settings > User >Management > Directories. |
| $(MD\_SCHEME) | The directory for schemes defined under Options > Settings > User >Management > Directories. |
| $(MD\_SCRIPTS) | The directory for scripts defined under Options > Settings > User >Management > Directories. |
| $(MD\_SYMBOLS) | The directory for symbols defined under Options > Settings > User >Management > Directories. |
| $(MD\_TEMPLATES) | The directory for templates defined under Options > Settings > User >Management > Directories. |
| $(MD\_TRANSLATE) | The directory for translation files defined under Options > Settings >User > Management > Directories. |
| $(MD\_XML) | The directory for XML files defined under Options > Settings > User > Management > Directories. |
| $(P) | Full project directory of the currently selected project. |
| $(PROJECTNAME) | Project name of the currently selected project, without directory path and file extension. |
| $(PROJECTPATH) | Full project directory of the currently selected project. |
|  |
|  |
| $(RIGHTS\_DB\_PATH) | Directory of the user rights database. |
| $(TMP) | The directory used by the operating system for temporary files. |

  
For more information about path variables, please refer to EPLAN Help under the topic:  
Using EPLAN>User Interface>Reference>Dialog Select Path variable.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PathMap Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~Dispose().html) | Destructor for deterministic finalization of PathMap object. |
| Public Methodstatic (Shared in Visual Basic) | [ReSubstitutePath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~ReSubstitutePath.html) | Overloaded. Substitute values with variable strVariableName. Returns the changed path. |
| Public Methodstatic (Shared in Visual Basic) | [ReSubstitutePathForDisplay](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~ReSubstitutePathForDisplay.html) | Substitute values with variables. Returns the changed path. Ignores all variables which are not visible in P8 Dialogs. |
| Public Methodstatic (Shared in Visual Basic) | [SubstitutePath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap~SubstitutePath.html) | Overloaded. Substitutes variables with their values for a partuclar Project. Returns the changed path. |


