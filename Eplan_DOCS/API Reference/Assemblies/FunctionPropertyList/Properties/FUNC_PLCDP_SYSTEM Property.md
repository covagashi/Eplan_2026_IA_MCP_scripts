# FUNC_PLCDP_SYSTEM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCDP_SYSTEM().html

---

Physical network: Name # 20413.

Syntax

**C#**



public PropertyValue FUNC_PLCDP_SYSTEM {get; set;}

public:

property PropertyValue^ FUNC_PLCDP_SYSTEM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Designation of the bus bundle or name of the physical network on which the bus port is connected. This name must be unique within the configuration project. Only one bus system can exist within a physical network.
