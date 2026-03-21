# Project(StringCollection,String,String,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~Project(StringCollection,String,String,Boolean,Boolean).html

---

Restore projects from archive files.

Syntax

**C#**



public void Project( 

   StringCollection strColArchivenames,

   string strRestorePath,

   string strProjectName,

   bool bUnpackProjects,

   bool bQuietMode

)

public:

void Project( 

   StringCollection^ strColArchivenames,

   String^ strRestorePath,

   String^ strProjectName,

   bool bUnpackProjects,

   bool bQuietMode

)


#### Parameters

*strColArchivenames*
:   Collection of archive file names (.zw1 files) to be restored.

*strRestorePath*
:   Path into which the projects will be restored.

*strProjectName*
:   If only ONE project should be restored, the name of the target project must be set in this parameter. (If more than one project is restored, i.e. the file specified in strColArchivenames contains more than one entry,the names of the target projects will be created from the names in the archive file).

*bUnpackProjects*
:   Set this flag to false normally. Only set the attribute to true, if you want to unpack a packed project. This is a special case for the project management\: If true, in strCollArchivenames not archive names, but project link file names were passed; the restore method in this case creates the archive names from the project names.

*bQuietMode*
:   If set to true, no summary dialog will be shown at the end of the backup process. (Else a message box (decider) with the restore results for all projects will be shown).

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while restoring the project. |
| **ApplicationException** | \Internal interface for restore could not be created. |

Remarks

If the project to restore already exists, it will be overwritten. ProjectInfo.xml will be restored always.
