# AddCommand(MultiLangString,String,MultiLangString,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1304.html

---

Backs up master data. Master data include: Symbol libraries, plot frames, forms, macros, parts data, dictionaries, user/workstation data.

Syntax

**C#**



public void MasterData( 

   StringCollection strDataFileSelection,

   string strComment,

   string strSourcePath,

   string strTargetPath,

   string strArchiveName,

   Backup.MasterDataType eMdType

)

public:

void MasterData( 

   StringCollection^ strDataFileSelection,

   String^ strComment,

   String^ strSourcePath,

   String^ strTargetPath,

   String^ strArchiveName,

   Backup.MasterDataType eMdType

)


#### Parameters

*strDataFileSelection*
:   Selected files whose master data are to be backed up.

*strComment*
:   String that is written as a comment into the corresponding backup property in the backed up projects.

*strSourcePath*
:   Source directory

*strTargetPath*
:   Destination path where the backed up projects are stored.

*strArchiveName*
:   Name of file in which the backed up data are stored. Because strTargetpath already contains the destination path, the path must be left out when the file name is entered.

*eMdType*
:   An Enum constant, which may have the following values:

    Symbols : Backup of symbol libraries.

    Macros : Backup of macros.

    Forms : Backup of forms.

    Articles : Backup of parts data.

    Languages : Backup of dictionaries.

    StandardSheet : Backup of plot frames.

    StationData : Backup of workstation settings.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during a data backup operation. |
| **ApplicationException** | The interface to the backup system cannot be generated. |

Remarks

If the specified directory already contains a backup file with the same name, this file is overwritten
