# RenameFunction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameFunction.html

---

Changes the full names of the function and its children.

Syntax

**C#**



public static void RenameFunction( 

   IFunctionBase pFunctionBase,

   FunctionBasePropertyList pNewName,

   bool bKeepDescribingProps

)

public:

static void RenameFunction( 

   IFunctionBase^ pFunctionBase,

   FunctionBasePropertyList^ pNewName,

   bool bKeepDescribingProps

)


#### Parameters

*pFunctionBase*
:   Function3D which name will be changed.

*pNewName*
:   Name that will be set to function and its children.

*bKeepDescribingProps*
:   if `true` then describing properties of function will not be changed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Invalid parameters were found. |
| [System.ArgumentNullException](#) | Null was passed to a parameter. |

Remarks

Method changes name only for given [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html) and its children, not whole device. To change name of whole device use [RenameDevice](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameDevice.html) instead.
