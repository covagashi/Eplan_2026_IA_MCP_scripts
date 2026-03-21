# MasterData Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1305.html

---

Backs up the entire project. Project is backed up on hard disk, diskette... Projects with a path specified in parameter strColPrjSelection become invalid. All documents and images included in the project are also backup-ed.

Syntax

**C#**



public void Project( 

   StringCollection strColPrjSelection,

   string strComment,

   string strTargetPath,

   StringCollection strColArcName,

   Backup.Type eBakMethod,

   bool bAutomaticallyCopyReferencedData

)

public:

void Project( 

   StringCollection^ strColPrjSelection,

   String^ strComment,

   String^ strTargetPath,

   StringCollection^ strColArcName,

   Backup.Type eBakMethod,

   bool bAutomaticallyCopyReferencedData

)


#### Parameters

*strColPrjSelection*
:   Collection of projects that are to be backed up. The names must contain the entire project path. Project file extensions (e.g. \*.elk) don't have to be specified, they are filtered out.

*strComment*
:   String that is written as a comment into the corresponding backup property in the backed up projects.

*strTargetPath*
:   Destination path where the backed up projects are stored.

*strColArcName*
:   Collection of file names under which backed up projects are to be saved. The entries of strColArcName must be listed in the same order as those of strColPrjSelection. Because strTargetpath already contains the destination path, the path must be left out when the file name is entered.

*eBakMethod*
:   An Enum constant, which may have the following values:

    Backup : Project is backed up

    SourceOut : Project is filed off

    Archive : Project is archived. Must not be set when "eBakMedia" parameter is "EMail".

    Pack : Project is packed. Param `strTargetPath` is ignored.

*bAutomaticallyCopyReferencedData*
:   If true, external files that are referenced by the project are copied to the project's directory (the '\DOC' and '\Images' subdirectories) before the backup.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during a data backup operation. |
| **ApplicationException** | The interface to the backup system cannot be generated. |

Remarks

If the specified directory already contains a backup file with the same name, this file is overwritten. Archive names of the form <some name>.nnn (n = a digit 0 - 9) are forbidden, because an archive name of this form ( with a three-digit-extension)is automatically created when the backup file is split into several parts.
