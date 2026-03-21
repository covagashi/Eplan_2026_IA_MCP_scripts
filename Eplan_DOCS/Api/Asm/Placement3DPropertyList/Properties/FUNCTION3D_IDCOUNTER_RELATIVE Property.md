# FUNCTION3D_IDCOUNTER_RELATIVE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_IDCOUNTER_RELATIVE().html

---

Counter in item ID (relative to macro, EEC) # 36034.

Syntax

**C#**



public PropertyValue FUNCTION3D_IDCOUNTER_RELATIVE {get; set;}

public:

property PropertyValue^ FUNCTION3D_IDCOUNTER_RELATIVE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The counter is assigned automatically at the 3D part placements of the macro when reading in a macro in Eplan Engineering Configuration and is used by the Item ID (relative to macro, EEC) property. If the individual 3D part placements cannot be uniquely identified by "Function definition" and "Item" at a part that consists of several combined 3D part placements, these are additionally identified via the counter.
