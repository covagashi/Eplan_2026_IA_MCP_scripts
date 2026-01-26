# CONNECTION_SWAP_SRC_DEST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_SWAP_SRC_DEST().html

---

Exchange source and target # 31013.

Syntax

**C#**



public PropertyValue CONNECTION_SWAP_SRC_DEST {get; set;}

public:

property PropertyValue^ CONNECTION_SWAP_SRC_DEST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

The source and target of a connection are determined by the device tag of the connected functions. Using this property, you can reverse the direction of the individual connection on the connection.
