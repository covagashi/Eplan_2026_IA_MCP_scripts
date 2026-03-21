# CDP_CON_SUBCRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_CON_SUBCRAFT().html

---

Associated connections: Subtrade # 31067.

Syntax

**C#**



public PropertyValue CDP_CON_SUBCRAFT {get; set;}

public:

property PropertyValue^ CDP_CON_SUBCRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

This property is no longer in use and only taken into consideration in old projects. On a connection definition point, this shows the corresponding property of the connection running below the connection definition point.
