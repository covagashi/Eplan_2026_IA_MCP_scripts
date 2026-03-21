# FindMatchingTemplatePairs Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~FindMatchingTemplatePairs.html

---

Matches templates and wires. No changes on objects are performed.

Syntax

**C#**



public KeyValuePair<Connection,Connection>[] FindMatchingTemplatePairs( 

   Project oProject,

   Connection[] arrTemplatesToWires,

   bool bChangeExistingProperties,

   AnyPropertyId[] arrListOfExcludedAnyPropertyIds,

   Function oSortInfoCable,

   bool bDividePairsBeforeReassign

)

public:

array<KeyValuePair<Connection^,Connection^>>^ FindMatchingTemplatePairs( 

   Project^ oProject,

   array<Connection^>^ arrTemplatesToWires,

   bool bChangeExistingProperties,

   array<AnyPropertyId^>^ arrListOfExcludedAnyPropertyIds,

   Function^ oSortInfoCable,

   bool bDividePairsBeforeReassign

)


#### Parameters

*oProject*
:   Project on which this operation will be executed.

*arrTemplatesToWires*
:   Contains pairs wire and template which will be assign to the wire.

*bChangeExistingProperties*
:   If true matching procedure act as existing properties could be changed.

*arrListOfExcludedAnyPropertyIds*
:   List of properties ids which wouldn't be changed. Can be NULL.

*oSortInfoCable*
:   Function that contains information for sorting rules. Can be NULL.

*bDividePairsBeforeReassign*
:   If true and bChangeExistingProperties is true another wire with higher sorting order may be match to the template instead of the old assigned wire.

#### Return Value

Result is return as array of `KeyValuePair`. `Key` contain template and `Value` contain a Connection (wire). If no match was found for a wire then `Key` for its pair is NULL. If no match was found for a template then `Value` for its pair is NULL.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | If necessary parameter is NULL. |
| **ArgumentException** | If parameter is invalid. |
| **ApplicationException** | Internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when matching wires. Please read the exception message. |

Remarks

Function tries to find a template for every wire. A matching template will be found for a wire, only if both have the same [potential type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~POTENTIAL_TYPE.html).
