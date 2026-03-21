# GetCommonLanguages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~GetCommonLanguages.html

---

Determines the list of languages, which the given storableObjects have in common. Is used for getting the common languages of a project.

Syntax

**C#**



public bool GetCommonLanguages( 

   StringCollection listLanguages,

   StorableObject[] storableObjects

)

public:

bool GetCommonLanguages( 

   StringCollection^ listLanguages,

   array<StorableObject^>^ storableObjects

)


#### Parameters

*listLanguages*
:   [out] Collection returns the common languages. Languages are returned as language shortcuts, e.g.. de\_DE, en\_US, ...

*storableObjects*
:   [in] Array of `StorableObject`s.

#### Return Value

true, in case of no error.
