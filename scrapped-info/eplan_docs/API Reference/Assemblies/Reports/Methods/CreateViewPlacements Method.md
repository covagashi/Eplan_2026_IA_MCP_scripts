# CreateViewPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateViewPlacements.html

---

Creates model views report

Syntax

**C#**



public void CreateViewPlacements( 

   Project oProject,

   StringCollection colTemplates,

   bool bReplaceExisting

)

public:

void CreateViewPlacements( 

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
:   Replace existing model views when true

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
//prepare page macro file for a report template

System.IO.File.Copy(strMacrosDirectory + "\\ModelView.emp", new ProjectManager().Paths.Macros + "\\ModelView.emp", true);

//load report template

ProjectSettings oProjectSettings = new ProjectSettings(m_oProject);

oProjectSettings.ReadSettings(strXMLDirectory + "\\ModelView.xml");

StringCollection oTemplates = new StringCollection();

oTemplates.Add("1");

new Reports().CreateViewPlacements(m_oProject, oTemplates, true);
```
