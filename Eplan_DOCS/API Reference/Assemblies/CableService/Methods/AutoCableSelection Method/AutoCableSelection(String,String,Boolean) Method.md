# AutoCableSelection(String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~AutoCableSelection(String,String,Boolean).html

---

Commits an automatic cable selection in the project.

Syntax

**C#**



public void AutoCableSelection( 

   string strFullLinkFileName,

   string strAutoSelSchemeName,

   bool bOnlyAutomaticCables

)

public:

void AutoCableSelection( 

   String^ strFullLinkFileName,

   String^ strAutoSelSchemeName,

   bool bOnlyAutomaticCables

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project for which the cable selection is done.

*strAutoSelSchemeName*
:   scheme name for the automatic cable selection.

*bOnlyAutomaticCables*
:   If set to true, the selection is only done for automatically generated cables.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | invalid parameters found, e.g. the scheme was invalid. |
| **ApplicationException** | \Internal interface for generating cables could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error during cable selection. |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |

Remarks

If the given user scheme (strAutoSelSchemeName) does not exist, an ArgumentException is thrown. If the parameter strAutoSelSchemeName is set to an empty string, the last-used scheme will be used which is currently set in GUI.
