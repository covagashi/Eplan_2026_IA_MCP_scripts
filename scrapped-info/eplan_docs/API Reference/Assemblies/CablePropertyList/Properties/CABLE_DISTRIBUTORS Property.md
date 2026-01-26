# CABLE_DISTRIBUTORS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList~CABLE_DISTRIBUTORS().html

---

Cables: Connection splicers passed through # 35111.

Syntax

**C#**



public PropertyValue CABLE_DISTRIBUTORS {get; set;}

public:

property PropertyValue^ CABLE_DISTRIBUTORS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the DTs of the connection splicers which pass through the cable. The individual values are separated by a semicolons and sorted alphanumerically. This property can be used in cable reports, for example during the evaluation of single-line cables.
