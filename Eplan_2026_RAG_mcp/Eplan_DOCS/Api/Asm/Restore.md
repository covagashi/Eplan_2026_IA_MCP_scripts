# Restore

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore.html

---

Class providing functionality to restore backups of projects or master data.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Restore**

Syntax

**C#**



public class Restore

public ref class Restore


Remarks

Restored project is automatically upgraded to the currently used EPLAN version.

Example

Following example shows how to use Restore class.

**C#**

```
Restore oRestore = new Restore();

StringCollection oArchives = new StringCollection();

oArchives.Add("$(MD_PROJECTS)\\EPLAN_Sample_Project.zw1");

oRestore.Project(oArchives,

                "C:\\temp",

                "EPLAN-DEMO_restored",

                false,

                false);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Restore Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~Dispose().html) | Destructor |
| Public Method | [MasterData](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~MasterData.html) | Restore master data from archive files. |
| Public Method | [Project](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~Project.html) | Overloaded. Restore projects from archive files. |


