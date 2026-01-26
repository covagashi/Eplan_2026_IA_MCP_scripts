# ExportProductionWiring(Project,Connection[],PWMachineType,String,String,String,Language,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1322.html

---

Exports manufacturing data for wire fabrication machines.

Syntax

**C#**



public bool ExportProductionWiring( 

   Project oPrj,

   ConnectionService.PWMachineType kindOfMachine,

   string strNameOfMachine,

   string strDestinationPath,

   string strFileName,

   ISOCode.Language nExportLanguage,

   bool bAllowExportConnectionMultiple

)

public:

bool ExportProductionWiring( 

   Project^ oPrj,

   ConnectionService.PWMachineType kindOfMachine,

   String^ strNameOfMachine,

   String^ strDestinationPath,

   String^ strFileName,

   ISOCode.Language nExportLanguage,

   bool bAllowExportConnectionMultiple

)


#### Parameters

*oPrj*
:   Project from which production wirings will be exported.

*kindOfMachine*
:   Type of machine that will be used to export production wirings.

*strNameOfMachine*
:   Name of machine that will be used to export production wirings.

*strDestinationPath*
:   Directory into which export will done. If not exists then it will be created.

*strFileName*
:   If passed then export will be to this file. Can be `null` or empty. In Case of KOMAX and Steinhauer PWA export, fixed filename is used. So, this filename parameter will not be considered.

*nExportLanguage*
:   Language in which export will be done.

*bAllowExportConnectionMultiple*
:   If true then multiple connections are also exported.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |
