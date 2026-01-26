# DoProjectInspection(Project,Project,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1430.html

---

Compares two projects and writes the results as project messages into the message management. This method corresponds to the following functionality of EPLAN Electric P8: Project / Management, Extras / Verify Project

Syntax

**C#**



public bool DoProjectInspection( 

   Project oProject,

   Project oRefProject,

   bool bCompareSettings,

   bool bCompareProperties,

   bool bDoVerification,

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

   bool bCompareProperties,

   bool bDoVerification,

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
:   If true, comparison of project settings is done. Last used settings comparison scheme will be used.

*bCompareProperties*
:   If true, comparison of project properties is done. Last used properties comparison scheme will be used.

*bDoVerification*
:   If true, projects verification is also done. Last used verification scheme will be used.

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
| **System\:\:ArgumentNullException** | Thrown if oProject or oRefProject is null value. |

Remarks

In case `bDoVerification` is true, the project will be checked. Messages created by old project verifications are deleted.
