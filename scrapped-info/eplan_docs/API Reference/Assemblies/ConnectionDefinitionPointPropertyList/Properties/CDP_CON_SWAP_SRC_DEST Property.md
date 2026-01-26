# CDP_CON_SWAP_SRC_DEST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_CON_SWAP_SRC_DEST().html

---

Associated connections: Exchange source and target # 31036.

Syntax

**C#**



public PropertyValue CDP_CON_SWAP_SRC_DEST {get; set;}

public:

property PropertyValue^ CDP_CON_SWAP_SRC_DEST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

This property is no longer in use and only taken into consideration in old projects. On a connection definition point, this shows the corresponding property of the connection running below the connection definition point.
