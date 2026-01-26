# BundleConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~BundleConnections.html

---

Bundle connections of project.

Syntax

**C#**



public void BundleConnections( 

   Project pProject,

   int nStartValue,

   int nStepWith,

   int nNumWiresInBundleMax,

   double dSubXSectionInBundle,

   List<string> arrBundlingSchemas,

   bool bPreferChains,

   bool bDoCompleteProject,

   bool bShowPreview

)

public:

void BundleConnections( 

   Project^ pProject,

   int nStartValue,

   int nStepWith,

   int nNumWiresInBundleMax,

   double dSubXSectionInBundle,

   List<String^>^ arrBundlingSchemas,

   bool bPreferChains,

   bool bDoCompleteProject,

   bool bShowPreview

)


#### Parameters

*pProject*
:   Project, which connections will be bundled

*nStartValue*
:   Start value for bundle numbers

*nStepWith*
:   Step with for bundle numbers

*nNumWiresInBundleMax*
:   Maximum number of wires per bundle

*dSubXSectionInBundle*
:   Maximum summary cross-section in a bundle

*arrBundlingSchemas*
:   List of bundling schemes

*bPreferChains*
:   If true daisy chanins (Net) will be prefered in bundle.

*bDoCompleteProject*
:   Apply for entire project

*bShowPreview*
:   Show preview

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ApplicationException](#) | An interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |
