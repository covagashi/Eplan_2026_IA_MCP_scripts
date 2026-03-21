# PrepareMacros(ICollection<Page>,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~PrepareMacros(ICollection{Page},Boolean,Boolean,Boolean).html

---

Prepares and groups all elements belonging to a macro box or page macro.

Syntax

**C#**



public bool PrepareMacros( 

   ICollection<Page> colPages,

   bool bGroupMacroBoxes,

   bool bGroupPageMacros,

   bool bSetHandleOnMacroBoxes

)

public:

bool PrepareMacros( 

   ICollection<Page^>^ colPages,

   bool bGroupMacroBoxes,

   bool bGroupPageMacros,

   bool bSetHandleOnMacroBoxes

)


#### Parameters

*colPages*
:   Collection of pages for which macro preparation should be done. All pages have to belong to the same project and the project must be a macro project.

*bGroupMacroBoxes*
:   Group macro boxes with their contents.

*bGroupPageMacros*
:   Group contents of a page macro.

*bSetHandleOnMacroBoxes*
:   Activates handle for macro box. By this unwanted shifting of macro is prevented.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Pages collection was set to a null reference. |
| [System.ArgumentException](#) | Collection is empty or pages are not from the same project. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be prepared. |
