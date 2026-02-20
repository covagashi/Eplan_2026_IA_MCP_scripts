# Backup

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup.html

---

This class provides functions for the data backup. Following example shows how to use Backup class.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Backup**

Syntax

**C#**



public class Backup

public ref class Backup


Example

Following example shows how to use Backup class.

**C#**

```
Backup oBackup = new Backup();

oBackup.Project(

 "$(MD_PROJECTS)\\EPLAN_Sample_Project.elk",

  "Project backup - test comment",

  "$(MD_PROJECTS)",

  "EPLAN_Sample_Project.zw1",

  Backup.Type.MakeBackup,

 false);

Console.Out.WriteLine("Backup of project was created !");

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Backup Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup~Dispose().html) | Destructor |
| Public Method | [MasterData](topic1304.html) | Backs up master data. Master data include: Symbol libraries, plot frames, forms, macros, parts data, dictionaries, user/workstation data. |
| Public Method | [Project](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup~Project.html) | Overloaded. Backs up an entire project. Project is backed up on hard disk, diskette... The path specified in strProjectPath parameter becomes invalid after the backup. All documents and images included in the project are also backup-ed. |


