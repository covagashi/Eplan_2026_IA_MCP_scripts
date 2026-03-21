# AddPLCAddress(PLCAddress) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddPLCAddress(PLCAddress).html

---

Creates copy of existing PLC inputs or outputs for this planning object.

Syntax

**C#**



public PlanningSegment.PLCAddress AddPLCAddress( 

   PlanningSegment.PLCAddress pSourceAddress

)

public:

PlanningSegment.PLCAddress^ AddPLCAddress( 

   PlanningSegment.PLCAddress^ pSourceAddress

)


#### Parameters

*pSourceAddress*
:   PLCAddress object of which copy will be created. If `null` new object will be created.

#### Return Value

Returns created element.

Remarks

Methods creates new element and copies values from source element to the new one. If the source is `null` then olny copy is created and its fields are set to default values.

New element is appended to the end of the [PLCAddresses](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PLCAddresses.html).

Example

**C#**

```
PlanningSegment.PLCAddress oSourceAddress;

PlanningSegment.PLCAddress oNewAddress;

//get plc input or output which will be copied

oSourceAddress = oPCTLoop.PLCAddresses[0];

//create a new copy of source object

oNewAddress = oPCTLoop.AddPLCAddress(oSourceAddress);

```
