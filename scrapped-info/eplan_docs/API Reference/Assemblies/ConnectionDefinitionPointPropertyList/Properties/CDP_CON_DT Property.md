# CDP_CON_DT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_CON_DT().html

---

Associated connections: Device tag (identifying) # 31027.

Syntax

**C#**



public PropertyValue CDP_CON_DT {get; set;}

public:

property PropertyValue^ CDP_CON_DT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is no longer in use and only taken into consideration in old projects. On a connection definition point, this shows the corresponding property of the connection running below the connection definition point.
