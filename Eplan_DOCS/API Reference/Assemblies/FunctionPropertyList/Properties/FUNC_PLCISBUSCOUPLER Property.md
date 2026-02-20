# FUNC_PLCISBUSCOUPLER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCISBUSCOUPLER().html

---

Bus coupler / head station # 20164.

Syntax

**C#**



public PropertyValue FUNC_PLCISBUSCOUPLER {get; set;}

public:

property PropertyValue^ FUNC_PLCISBUSCOUPLER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Identifies a device as a bus coupler or head station. In the case of a head station the Rack property has to be filled additionally for the respective PLC card.
