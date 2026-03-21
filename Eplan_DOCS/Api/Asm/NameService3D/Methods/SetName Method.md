# SetName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~SetName.html

---

Sets a default device tag to the function.

Syntax

**C#**



public static bool SetName( 

   IFunctionBase pFunctionBase

)

public:

static bool SetName( 

   IFunctionBase^ pFunctionBase

)


#### Parameters

*pFunctionBase*
:   A Function3D for which name is to be set.

#### Return Value

Returns true, if the device tag has actually been changed.

Remarks

The function must have its function definition configured (since the code letter is provided by this).
