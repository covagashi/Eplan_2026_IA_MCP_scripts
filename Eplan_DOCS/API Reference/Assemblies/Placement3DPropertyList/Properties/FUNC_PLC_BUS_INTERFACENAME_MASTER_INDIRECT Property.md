# FUNC_PLC_BUS_INTERFACENAME_MASTER_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic624.html

---

Bus interface: Main bus port (indirect) # 20391.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUS_INTERFACENAME_MASTER_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUS_INTERFACENAME_MASTER_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Outputs the value of the same single-line bus port at a bus port of the "Overview" or "Multi-line" representation type.
