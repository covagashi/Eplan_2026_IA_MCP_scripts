# Project(String,String,String,String,Type,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup~Project(String,String,String,String,Type,Boolean).html

---

Backs up an entire project. Project is backed up on hard disk, diskette... The path specified in strProjectPath parameter becomes invalid after the backup. All documents and images included in the project are also backup-ed.

Syntax

**C#**



public void Project( 

   string strProjectPath,

   string strComment,

   string strTargetPath,

   string strArchiveName,

   Backup.Type eBakMethod,

   bool bAutomaticallyCopyReferencedData

)

public:

void Project( 

   String^ strProjectPath,

   String^ strComment,

   String^ strTargetPath,

   String^ strArchiveName,

   Backup.Type eBakMethod,

   bool bAutomaticallyCopyReferencedData

)


#### Parameters

*strProjectPath*
:   An entire path to the project. (File extensions, e.g. \*.elk, don't have to be specified.)

*strComment*
:   String that is written as a comment into the corresponding backup property in the backed up project.

*strTargetPath*
:   Destination path where the backed up project is stored.

*strArchiveName*
:   File name under which backed up project is to be saved.

*eBakMethod*
:   An Enum constant, which may have the following values:

    Backup : Project is backed up

    SourceOut : Project is filed off

    Archive : Project is archived. Must not be set when "eBakMedia" parameter is "EMail".

    Pack : Project is packed. Param `strTargetPath` is ignored.

*bAutomaticallyCopyReferencedData*
:   If true, all external files that are referenced by the project are copied to the project's directory (the '\DOC' and '\Images' subdirectories) before the backup.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during a data backup operation. |
| **ApplicationException** | The interface to the backup system cannot be generated. |
| **ProjectLockingException** | The project could not be locked for back up. |

Remarks

If the specified directory already contains a backup file with the same name, this file is overwritten. Archive names of the form <some name>.nnn (n = a digit 0 - 9) are forbidden, because an archive name of this form ( with a three-digit-extension)is automatically created when the backup file is split into several parts.

Example

Following example shows how to use the method:

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
