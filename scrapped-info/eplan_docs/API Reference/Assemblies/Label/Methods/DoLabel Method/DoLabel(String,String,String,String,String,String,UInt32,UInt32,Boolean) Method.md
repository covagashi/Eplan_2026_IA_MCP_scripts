# DoLabel(String,String,String,String,String,String,UInt32,UInt32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1378.html

---

do a labeling for a project.

Syntax

**C#**



public void DoLabel( 

   string strFullLinkFileName,

   string strConfigScheme,

   string strFilterScheme,

   string strSortScheme,

   string strLanguage,

   string strDestinationFile,

   uint nRecordRepeat,

   uint nTaskRepeat,

   bool bShowOutput

)

public:

void DoLabel( 

   String^ strFullLinkFileName,

   String^ strConfigScheme,

   String^ strFilterScheme,

   String^ strSortScheme,

   String^ strLanguage,

   String^ strDestinationFile,

   uint nRecordRepeat,

   uint nTaskRepeat,

   bool bShowOutput

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, for which a labeling will be done.

*strConfigScheme*
:   Name of the configuration scheme.

*strFilterScheme*
:   Name of the filter scheme.If this value is empty filter scheme name will be taken from configuration scheme

*strSortScheme*
:   Name of the sorting scheme. If this value is empty sorting scheme name will be taken from configuration scheme

*strLanguage*
:   Language used by the labeling operation, ex. de\_DE, en\_EN, or ??\_?? for all display languages.

*strDestinationFile*
:   Destination file where the labeling results will be stored.Extension of this \file must be set according to the configuration in strConfigScheme. If this parameter is empty, the destination file name is taken from the configuration selected by the strConfigScheme parameter.

*nRecordRepeat*
:   Repeating number per each record. It must be greater or equal 1

*nTaskRepeat*
:   Repeating number per task. It must be greater or equal 1.

*bShowOutput*
:   Show output file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | \Parameters are invalid. |
| **ApplicationException** | Needed internal interface could not be created. |
| **ArgumentNullException** | A parameter is a null reference. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error occurred by labeling. |

Remarks

If a user scheme is not empty, so it will be checked for existence. An ArgumentException will be thrown if it does not exist. If the user configuration scheme is empty or null, so the last used configuration scheme will be implicitly reused which is currently set in GUI. If filter or sort scheme is empty or null, its name will be taken from configuration scheme.

The destination file should have the extension .txt, .xls, .xlsx or .xml. Otherwise the given extension will be replaced with .txt per default.

Microsoft Excel application is necessary to run Labeling with output file extension set to .xls (Excel format).

In contrary to the behavior, when Labeling is executed via the EPLAN ribbon, the API never considers the current selection in the project. In EPLAN GUI the selection causes the filters to be ignored, in API, the filters are never ignored, when set.
