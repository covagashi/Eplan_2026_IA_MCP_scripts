# CONNECTION_DEST_CP_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_DEST_CP_LENGTH().html

---

Connection: Connection point length target # 31083.

Syntax

**C#**



public PropertyValue CONNECTION_DEST_CP_LENGTH {get; set;}

public:

property PropertyValue^ CONNECTION_DEST_CP_LENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Indicates the item length of the connection that is required to connect the target item. It is by this value that the connection must project at the last routing point.
