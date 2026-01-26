# CDP_CON_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_CON_DESCRIPTION().html

---

Associated connections: Connection description # 31032.

Syntax

**C#**



public PropertyValue CDP_CON_DESCRIPTION {get; set;}

public:

property PropertyValue^ CDP_CON_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

This property is no longer in use and only taken into consideration in old projects. On a connection definition point, this shows the corresponding property of the connection running below the connection definition point.
