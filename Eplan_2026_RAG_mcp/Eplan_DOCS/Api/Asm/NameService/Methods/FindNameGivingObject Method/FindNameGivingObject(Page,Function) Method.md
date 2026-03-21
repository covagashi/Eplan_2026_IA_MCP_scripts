# FindNameGivingObject(Page,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingObject(Page,Function).html

---

Finds an object, that would give the f function its name, if f has no its instance name parts assigned (has no visible device tag). Returns NULL, if no such object exists or f don't take over a name.

Syntax

**C#**



public FunctionBase FindNameGivingObject( 

   Page page,

   Function f

)

public:

FunctionBase^ FindNameGivingObject( 

   Page^ page,

   Function^ f

)


#### Parameters

*page*
:   A page to search the result object on.

*f*
:   Function, which takes over a name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |

Remarks

Similar to the FindNameGivingFunction method but returns objects like e.g. LocationBox too.
