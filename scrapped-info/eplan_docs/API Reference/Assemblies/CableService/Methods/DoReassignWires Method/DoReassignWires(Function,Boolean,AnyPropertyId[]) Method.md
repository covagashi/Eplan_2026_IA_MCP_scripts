# DoReassignWires(Function,Boolean,AnyPropertyId[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DoReassignWires(Function,Boolean,AnyPropertyId[]).html

---

All wires in cable are assigned to a matching template of the cable. Works only for [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) or [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) with category **Eplan.EplApi.DataModel.Function.Enums.Category.Shielding**.

Syntax

**C#**



public void DoReassignWires( 

   Function oFunction,

   bool bChangeExistingProperties,

   AnyPropertyId[] arrListOfExcludedAnyPropertyIds

)

public:

void DoReassignWires( 

   Function^ oFunction,

   bool bChangeExistingProperties,

   array<AnyPropertyId^>^ arrListOfExcludedAnyPropertyIds

)


#### Parameters

*oFunction*
:   Function on which this procedure will be executed.

*bChangeExistingProperties*
:   If true existing wire properties can be changed.

*arrListOfExcludedAnyPropertyIds*
:   List of properties ids. Value of those properties will not be changed. Can be NULL.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | If `oCable` is NULL. |
| **ArgumentException** | If parameter is invalid. |
| **ApplicationException** | Internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when reassigning wires. Please read the exception message. |

Remarks

Every template will be used only once. A wire will be assigned to a template, only if both have the same [potential type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_TYPE.html). If a wire is assigned to a template, the identifying wire properties of the template will be copied to the wire.

Only functions with category **Eplan.EplApi.DataModel.Function.Enums.Category.Cable** or **Eplan.EplApi.DataModel.Function.Enums.Category.Shielding** can be passed as `oFunction`.
