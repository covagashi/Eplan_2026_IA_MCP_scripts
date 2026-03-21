# CreateMergedFunctions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~CreateMergedFunctions.html

---

Returns an array of MergedFunction objects created from the functions passed in the array parameter. Functions that belong to the same device and represent one functional part of the device are merged together into one merged function in the output vector.

Syntax

**C#**



public static MergedFunction[] CreateMergedFunctions( 

   Function[] functions

)

public:

static array<MergedFunction^>^ CreateMergedFunctions( 

   array<Function^>^ functions

)


#### Parameters

*functions*

#### Return Value

An array of merged functions for the given functions.
