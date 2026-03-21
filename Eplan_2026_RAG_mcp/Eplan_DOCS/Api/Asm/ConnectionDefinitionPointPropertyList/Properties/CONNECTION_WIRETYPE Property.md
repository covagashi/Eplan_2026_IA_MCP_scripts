# CONNECTION_WIRETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_WIRETYPE().html

---

Connection: Type designation # 31048.

Syntax

**C#**



public PropertyValue CONNECTION_WIRETYPE {get; set;}

public:

property PropertyValue^ CONNECTION_WIRETYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Type designation of the connection part, e.g., the type number of the wire type, pipe type or tube type. During a part selection the value of the property "Cable type / type designation" (ID 22030) or "Connection type" (ID 22254) is transferred into this property. These properties can be found in the parts management in the "Properties" tab below the hierarchy level "Technical data". But the value can also be entered manually.
