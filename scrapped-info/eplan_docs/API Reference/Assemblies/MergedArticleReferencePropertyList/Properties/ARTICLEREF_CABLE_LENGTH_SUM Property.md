# ARTICLEREF_CABLE_LENGTH_SUM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_CABLE_LENGTH_SUM().html

---

Total cable length # 20500.

Syntax

**C#**



public PropertyValue ARTICLEREF_CABLE_LENGTH_SUM {get; set;}

public:

property PropertyValue^ ARTICLEREF_CABLE_LENGTH_SUM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Placeholder for the summarized parts list, for one cable part, this adds up all lengths of the cables taken into consideration in the report block and for which this cable part is entered. Every cable is considered only once here. The system recognizes a cable part by the fact that the product group "Cables" and the product subgroup "Undefined" are specified on the part.
