# GenerateMacrosFromMacroProject(Project,String,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1383.html

---

Generate macros from project. Project must have property "Type of project" set to "Macro project".

Syntax

**C#**



public void GenerateMacrosFromMacroProject( 

   Project oProject,

   string strWindowMacroDirectory,

   string strPageMacroDirectory,

   string strFilterScheme,

   bool bOverwriteExistingMacros

)

public:

void GenerateMacrosFromMacroProject( 

   Project^ oProject,

   String^ strWindowMacroDirectory,

   String^ strPageMacroDirectory,

   String^ strFilterScheme,

   bool bOverwriteExistingMacros

)


#### Parameters

*oProject*
:   Project from which the macros will be generated.

*strWindowMacroDirectory*
:   Specifies output directory for window macros. If empty or null default macro directory is used.

*strPageMacroDirectory*
:   Specifies output directory for window macros. If empty or null default macro directory is used.

*strFilterScheme*
:   Specifies filter scheme. If empty or null no filter is used.

*bOverwriteExistingMacros*
:   If the output file already exists specifies whether it should be overwritten.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | A parameter was set to a null reference. |
| [System.ArgumentException](#) | Parameters are invalid, e.g. given project name doesn't exist. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be exported. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidScheme](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidScheme.html) | Used filter scheme name doesn't exist |

Example

The following examples shows how to use method GenerateMacrosFromMacroProject.

**C#**

```
// Generate macros with specified strWindowMacroDirectory without filter.

// Page macros will be exported to default Macros directory.

string strWindowMacroDirectory = Path.Combine(m_oDir.FullName, "Test009d_WindowMacroDir");

new Masterdata().GenerateMacrosFromMacroProject(oTestProject, strWindowMacroDirectory, null, null, true);

```

**C#**

```
// Generate macros with specified strWindowMacroDirectory and strPageMacroDirectory without filter

strWindowMacroDirectory = Path.Combine(m_oDir.FullName, "Test009d_WindowMacroDir");

strPageMacroDirectory = Path.Combine(m_oDir.FullName, "Test009d_PageMacroDir");

new Masterdata().GenerateMacrosFromMacroProject(oTestProject, strWindowMacroDirectory, strPageMacroDirectory, null, true);

```

**C#**

```
// Generate macros with specified strFilterName to default Macros directory

string strFilterName = "page_macros";

new Masterdata().GenerateMacrosFromMacroProject(oTestProject, null, null, strFilterName, true);

```
