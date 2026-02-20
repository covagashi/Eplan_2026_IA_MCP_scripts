# PrepareMacros(Project,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~PrepareMacros(Project,Boolean,Boolean,Boolean).html

---

Prepares and groups all elements belonging to a macro box or page macro.

Syntax

**C#**



public bool PrepareMacros( 

   Project oProject,

   bool bGroupMacroBoxes,

   bool bGroupPageMacros,

   bool bSetHandleOnMacroBoxes

)

public:

bool PrepareMacros( 

   Project^ oProject,

   bool bGroupMacroBoxes,

   bool bGroupPageMacros,

   bool bSetHandleOnMacroBoxes

)


#### Parameters

*oProject*
:   Project for which preparation should be performed. It has to be a macro project.

*bGroupMacroBoxes*
:   Group macro boxes with their contents.

*bGroupPageMacros*
:   Group contents of a page macro.

*bSetHandleOnMacroBoxes*
:   Activates handle for macro box. By this unwanted shifting of macro is prevented.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Project was set to a null reference. |
| [System.ArgumentException](#) | Project is invalid. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be prepared. |
