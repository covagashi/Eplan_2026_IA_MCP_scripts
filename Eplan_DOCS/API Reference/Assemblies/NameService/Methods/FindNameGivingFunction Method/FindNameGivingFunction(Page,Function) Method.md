# FindNameGivingFunction(Page,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingFunction(Page,Function).html

---

Sets the page and finds the function, that would give hActual the function name, if hActual has no instance name parts (has no visible device tag). Returns NULL, if no such function exists or hActual don't take over a name.

Syntax

**C#**



public Function FindNameGivingFunction( 

   Page pPage,

   Function pActual

)

public:

Function^ FindNameGivingFunction( 

   Page^ pPage,

   Function^ pActual

)


#### Parameters

*pPage*
:   Page to set.

*pActual*
:   Function, which give name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
