# DoProjectInspection(Project,Project,Boolean,String,Boolean,String,Boolean,String,Boolean,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1429.html

---

Compares two projects and writes the results as project messages into the message management. This method corresponds to the following functionality of EPLAN Electric P8: Project / Management, Extras / Verify Project

Syntax

**C#**



public bool DoProjectInspection( 

   Project oProject,

   Project oRefProject,

   bool bCompareSettings,

   string sSettingsScheme,

   bool bCompareProperties,

   string sPropertiesScheme,

   bool bDoVerification,

   string sVerificationScheme,

   bool bComparePrjStructure,

   bool bCompareLayers,

   bool bReportNewLayers,

   bool bStopOnFirstDifference

)

public:

bool DoProjectInspection( 

   Project^ oProject,

   Project^ oRefProject,

   bool bCompareSettings,

   String^ sSettingsScheme,

   bool bCompareProperties,

   String^ sPropertiesScheme,

   bool bDoVerification,

   String^ sVerificationScheme,

   bool bComparePrjStructure,

   bool bCompareLayers,

   bool bReportNewLayers,

   bool bStopOnFirstDifference

)


#### Parameters

*oProject*
:   First project to be compared.

*oRefProject*
:   Second project to be compared.

*bCompareSettings*
:   If true, comparison of project settings is done.

*sSettingsScheme*
:   Name of settings comparison scheme. If `null` or `empty` string is passed then last used scheme will be used. This parameter is used only if `bCompareSettings` is `true`. If the scheme is not supported, information is passed as a system message.

*bCompareProperties*
:   If true, comparison of project properties is done.

*sPropertiesScheme*
:   Name of properties comparison scheme. If `null` or `empty` string is passed then last used scheme will be used. This parameter is used only if `bCompareProperties` is `true`. If the scheme is not supported, information is passed as a system message.

*bDoVerification*
:   If true, projects verification is also done.

*sVerificationScheme*
:   Name of verification scheme. If `null` or `empty` string is passed then last used scheme will be used. This parameter is used only if `bDoVerification` is `true`. If the scheme is not supported, information is passed as a system message.

*bComparePrjStructure*
:   If true, comparison of project structure is done.

*bCompareLayers*
:   If true, comparison of layersSecond is done.

*bReportNewLayers*
:   If true, new layers are reported. Used only if parameter `bCompareLayers` is `true`.

*bStopOnFirstDifference*
:   If true, the comparisons/verifications will stop on first difference/error.

#### Return Value

true if the inspection was succesful

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if oProject or oRefProject is null value. |

Remarks

Messages created by old project verifications are deleted.
