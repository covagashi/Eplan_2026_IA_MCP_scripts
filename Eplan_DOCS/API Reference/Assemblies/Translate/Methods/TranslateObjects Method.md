# TranslateObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateObjects.html

---

Translates all texts of a StorableObject (also project or page).

Syntax

**C#**



public bool TranslateObjects( 

   StorableObject[] storableObjects

)

public:

bool TranslateObjects( 

   array<StorableObject^>^ storableObjects

)


#### Parameters

*storableObjects*
:   Array of StorableObjects to be translated.

#### Return Value

true, in case of success.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during translation. |

Remarks

For projects or pages all elements within will be translated.
