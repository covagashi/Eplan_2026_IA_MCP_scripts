# DoLabel(Project,String,String,String,UInt32,UInt32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Label~DoLabel(Project,String,String,String,UInt32,UInt32).html

---

do a labeling for a project.

Syntax

**C#**



public void DoLabel( 

   Project oProject,

   string strConfigScheme,

   string strLanguage,

   string strDestinationFile,

   uint nRecordRepeat,

   uint nTaskRepeat

)

public:

void DoLabel( 

   Project^ oProject,

   String^ strConfigScheme,

   String^ strLanguage,

   String^ strDestinationFile,

   uint nRecordRepeat,

   uint nTaskRepeat

)


#### Parameters

*oProject*
:   Project, for which a labeling will be done.

*strConfigScheme*
:   Name of the configuration scheme.

*strLanguage*
:   Language used by the labeling operation, ex. de\_DE, en\_EN, or ??\_?? for all display languages.

*strDestinationFile*
:   Destination file where the labeling results will be stored.Extension of this \file must be set according to the configuration in strConfigScheme. If this parameter is empty, the destination file name is taken from the configuration selected by the strConfigScheme parameter.

*nRecordRepeat*
:   Repeating number per each record. It must be greater or equal 1

*nTaskRepeat*
:   Repeating number per task. It must be greater or equal 1.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | \Parameters are invalid. |
| **ApplicationException** | Needed internal interface could not be created. |
| **ArgumentNullException** | A parameter is a null reference. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error occurred by labeling. |

Remarks

If a user scheme is not empty, so it will be checked for existence. An ArgumentException will be thrown if it does not exist. If the user configuration scheme is empty or null, so the last used configuration scheme will be implicitly reused which is currently set in GUI. Filter and sort scheme names will be taken from configuration scheme.

The destination file should have the extension .txt, .xls, .xlsx or .xml. Otherwise the given extension will be replaced with .txt per default.

Microsoft Excel application is necessary to run Labeling with output file extension set to .xls (Excel format).

In contrary to the behavior, when Labeling is executed via the EPLAN ribbon, the API never considers the current selection in the project. In EPLAN GUI the selection causes the filters to be ignored, in API, the filters are never ignored, when set.
