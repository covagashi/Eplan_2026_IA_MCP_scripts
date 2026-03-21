# Project(StringCollection,String,String,StringCollection,Type,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1306.html

---

All wires in cable are assigned to a matching template of the cable or shielding. User specifies templates to which wires will be assigned. Works only for [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) or [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) with category **Eplan.EplApi.DataModel.Function.Enums.Category.Shielding**.

Syntax

**C#**



public void DoReassignWires( 

   Function oFunction,

   Connection[] arrWireTemplates,

   bool bChangeExistingProperties,

   AnyPropertyId[] arrListOfExcludedAnyPropertyIds

)

public:

void DoReassignWires( 

   Function^ oFunction,

   array<Connection^>^ arrWireTemplates,

   bool bChangeExistingProperties,

   array<AnyPropertyId^>^ arrListOfExcludedAnyPropertyIds

)


#### Parameters

*oFunction*
:   Function on which this procedure will be executed.

*arrWireTemplates*
:   List of templates which will be assign to wires.

*bChangeExistingProperties*
:   If true existing wire properties can be changed.

*arrListOfExcludedAnyPropertyIds*
:   List of properties ids. Value of those properties will not be changed. Can be NULL.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | If parameter is NULL. |
| **ArgumentException** | If parameter is invalid. |
| **ApplicationException** | Internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when reassigning wires. Please read the exception message. |

Remarks

Every template will be used only once. A wire will be assigned to a template, only if both have the same [potential type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_TYPE.html). If a wire is assigned to a template, the identifying wire properties of the template will be copied to the wire.

Only functions with category **Eplan.EplApi.DataModel.Function.Enums.Category.Cable** or **Eplan.EplApi.DataModel.Function.Enums.Category.Shielding** can be passed as `oFunction`.
