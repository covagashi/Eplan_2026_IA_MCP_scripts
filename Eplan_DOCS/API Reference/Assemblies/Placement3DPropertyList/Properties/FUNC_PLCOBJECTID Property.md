# FUNC_PLCOBJECTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCOBJECTID().html

---

PLC object ID (at functions) # 20162.

Syntax

**C#**



public PropertyValue FUNC_PLCOBJECTID {get; set;}

public:

property PropertyValue^ FUNC_PLCOBJECTID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Unique identifier for data exchange / synchronization between Eplan Electric P8 and PLC configuration systems. The object ID uniquely identifies objects of this configuration system.
