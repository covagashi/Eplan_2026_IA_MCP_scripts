# CreateDevice(Project,String,String,FunctionPropertyList,List<IFunctionBase>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1328.html

---

Create a new device.

Syntax

**C#**



public Function[] CreateDevice( 

   Project oProject,

   string strPartNummer,

   string strPartVariant,

   FunctionPropertyList pLocationList

)

public:

array<Function^>^ CreateDevice( 

   Project^ oProject,

   String^ strPartNummer,

   String^ strPartVariant,

   FunctionPropertyList^ pLocationList

)


#### Parameters

*oProject*
:   Project in which the new device will be.

*strPartNummer*
:   Part number.

*strPartVariant*
:   Part variant. If not existing variant is specified, then by default is selected a first available part's variant.

*pLocationList*
:   Property list for the hierarchy properties. This parameter may be NULL. If the parameter is NULL or the list doesn't contain code letter and counter properties, the name of the device will be generated in accordance to the device numeration settings.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid \arguments. |
| **ArgumentNullException** | Is thrown, if some argument was not passed. |
| **ApplicationException** | A necessary internal interface for creating devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an Error occurred while creating a device. |

Remarks

Method does not return 3D objects even when they are created. To get 3D object use other overloaded method instead.
