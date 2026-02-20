# DoReassignWires(Project,Boolean,AnyPropertyId[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DoReassignWires(Project,Boolean,AnyPropertyId[]).html

---

All wires in all cables from the project are assigned to a matching template of a cable.

Syntax

**C#**



public void DoReassignWires( 

   Project oProject,

   bool bChangeExistingProperties,

   AnyPropertyId[] arrListOfExcludedAnyPropertyIds

)

public:

void DoReassignWires( 

   Project^ oProject,

   bool bChangeExistingProperties,

   array<AnyPropertyId^>^ arrListOfExcludedAnyPropertyIds

)


#### Parameters

*oProject*
:   Project on which this procedure will be executed.

*bChangeExistingProperties*
:   If true existing wire properties can be changed.

*arrListOfExcludedAnyPropertyIds*
:   List of properties ids. Value of those properties will not be changed. Can be NULL.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | If `oProject` is NULL. |
| **ArgumentException** | If parameter is invalid. |
| **ApplicationException** | Internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when reassigning wires. Please read the exception message. |

Remarks

Every template will be used only once. A wire will be assigned to a template, only if both have the same [potential type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_TYPE.html). If a wire is assigned to a template, the identifying wire properties of the template will be copied to the wire.
