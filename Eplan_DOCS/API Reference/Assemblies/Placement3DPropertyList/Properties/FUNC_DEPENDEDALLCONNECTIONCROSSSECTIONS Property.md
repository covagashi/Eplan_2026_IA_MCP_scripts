# FUNC_DEPENDEDALLCONNECTIONCROSSSECTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DEPENDEDALLCONNECTIONCROSSSECTIONS().html

---

Connection point cross-section / diameter (all, depending on DT adoption) # 20297.

Syntax

**C#**



public PropertyValue FUNC_DEPENDEDALLCONNECTIONCROSSSECTIONS {get; set;}

public:

property PropertyValue^ FUNC_DEPENDEDALLCONNECTIONCROSSSECTIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property contains all connection point cross-sections / diameters of a function where the individual connection point cross-sections / diameters are separated by "¶". In addition, other connection point cross-sections / diameters of functions are also listed that are located in the search direction for the DT transfer.
