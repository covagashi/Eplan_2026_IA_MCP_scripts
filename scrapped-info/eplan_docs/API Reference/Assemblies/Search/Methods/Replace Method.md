# Replace Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Replace.html

---

Replaces text in a searched objects.

Syntax

**C#**



public void Replace( 

   StorableObject[] oObjectsInSearchResults,

   string strTextToFind,

   string strReplaceWith

)

public:

void Replace( 

   array<StorableObject^>^ oObjectsInSearchResults,

   String^ strTextToFind,

   String^ strReplaceWith

)


#### Parameters

*oObjectsInSearchResults*
:   Objects found by a Search class for which we are replacing text.

*strTextToFind*
:   Text that we want to find.

*strReplaceWith*
:   Text that we want to replace with.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the passed objects are not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
