# FUNC_PLC_BUSSYSTEM_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_BUSSYSTEM_INDIRECT().html

---

Bus system (indirect) # 20338.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUSSYSTEM_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUSSYSTEM_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Specifies the type of the bus system at a bus port of the "Overview" representation type to which the same single-line bus port is assigned as the bus node. The following values are possible: see the property "Bus system" (ID 20308).
