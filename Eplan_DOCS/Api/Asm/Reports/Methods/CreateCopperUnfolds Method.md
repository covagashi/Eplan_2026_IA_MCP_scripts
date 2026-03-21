# CreateCopperUnfolds Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateCopperUnfolds.html

---

Creates copper unfolds report

Syntax

**C#**



public void CreateCopperUnfolds( 

   Project oProject,

   StringCollection colTemplates,

   bool bReplaceExisting

)

public:

void CreateCopperUnfolds( 

   Project^ oProject,

   StringCollection^ colTemplates,

   bool bReplaceExisting

)


#### Parameters

*oProject*
:   Project

*colTemplates*
:   Collection of templates

*bReplaceExisting*
:   Replace existing copper unfolds when true

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any of parameters is null. |
| [System.ArgumentException](#) | If any of parameters is invalid. |
| [System.ApplicationException](#) | Failed to create. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating. Please refer to the error message. |

Example

**C#**

```
StringCollection oTemplates = new StringCollection();

oTemplates.Add("1");

new Reports().CreateCopperUnfolds(m_oProject, oTemplates, true);
```
