# FUNC_PLCCONFIGURATIONPROJECT_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCCONFIGURATIONPROJECT_INDIRECT().html

---

Configuration project (indirect) # 20108.

Syntax

**C#**



public PropertyValue FUNC_PLCCONFIGURATIONPROJECT_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCCONFIGURATIONPROJECT_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For a PLC connection point, this shows the configuration project of the associated PLC box. At bus ports of the "Overview" representation type the value is determined at the same single-line bus port.
