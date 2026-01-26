# AddPLCAddress() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddPLCAddress().html

---

Creates new PLC inputs or outputs for this planning object.

Syntax

**C#**



public PlanningSegment.PLCAddress AddPLCAddress()

public:

PlanningSegment.PLCAddress^ AddPLCAddress();


#### Return Value

Returns created element.

Remarks

New element is appended to the end of the [PLCAddresses](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PLCAddresses.html). All fields of new object are set to default values.

Example

The following code adds new PLCAddress to planning object.

**C#**

```
//create new planning object

PlanningSegment oNewPCTLoop = PlanningSegment.Create(oSegmentDefinition);

//add new PLC address

PlanningSegment.PLCAddress oNewAddress = oNewPCTLoop.AddPLCAddress();

//set values

oNewAddress.Direction = PlanningSegment.PLCAddress.Enums.PlcAddressDirection.Input;

oNewAddress.Address = "A2.0";

oNewAddress.DataType = "WORD";

oNewAddress.SymbolicAddress = "=EB3+ET1-H2:X1";

oNewAddress.Configuration = "Siemens SIMATIC S7";

oNewAddress.Station = "Station 300";

```
