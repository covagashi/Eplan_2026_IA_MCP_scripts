# SetName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~SetName.html

---

Sets a default device tag to the function. (I.e. a device tag which is automatically assigned when manually inserting a symbol on a page)

Syntax

**C#**



public bool SetName( 

   Function func

)

public:

bool SetName( 

   Function^ func

)


#### Parameters

*func*
:   A function whose name is to be set.

#### Return Value

Returns TRUE, if the device tag has actually been changed.

Remarks

The function must have its function definition configured (since the code letter is provided by this).
