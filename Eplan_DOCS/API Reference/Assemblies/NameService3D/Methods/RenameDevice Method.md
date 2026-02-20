# RenameDevice Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameDevice.html

---

Changes the full names of the found device.

Syntax

**C#**



public static void RenameDevice( 

   IFunctionBase pFunctionBase,

   FunctionBasePropertyList pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)

public:

static void RenameDevice( 

   IFunctionBase^ pFunctionBase,

   FunctionBasePropertyList^ pNewName,

   bool bRenameCDPsAlso,

   bool bKeepDescribingProps

)


#### Parameters

*pFunctionBase*
:   Function3D from device which name will be changed.

*pNewName*
:   Name that will be set to functions of device.

*bRenameCDPsAlso*
:   If `true` then connection of this device (example: wires of cable) also will be renamed.

*bKeepDescribingProps*
:   If `true` then describing properties of functions will not be changed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Invalid parameters were found. |
| [System.ArgumentNullException](#) | Null was passed to a parameter. |

Remarks

As device we understand not only given [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html) but also other objects with the same full name. To change only function name use [RenameFunction](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D~RenameFunction.html) instead.
