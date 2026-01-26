# CONNECTION_DISTRIBUTORS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DISTRIBUTORS().html

---

Connection splicers passed through # 31136.

Syntax

**C#**



public PropertyValue CONNECTION_DISTRIBUTORS {get; set;}

public:

property PropertyValue^ CONNECTION_DISTRIBUTORS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the DTs of the connection splicers which pass through the connection. The individual values are separated by a semicolons and sorted alphanumerically. This property can be used in reports.
