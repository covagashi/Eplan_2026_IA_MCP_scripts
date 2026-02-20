# CONNECTION_HAS_DISTRIBUTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_HAS_DISTRIBUTOR().html

---

Connection splicers exist # 31139.

Syntax

**C#**



public PropertyValue CONNECTION_HAS_DISTRIBUTOR {get; set;}

public:

property PropertyValue^ CONNECTION_HAS_DISTRIBUTOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows whether connection passes through at least one connection splicer. This property can be used as a filter criterion for connection lists.
