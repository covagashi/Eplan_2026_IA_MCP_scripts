# ARTICLEREF_ADDITIONAL_BOOLFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLEREF_ADDITIONAL_BOOLFIELD().html

---

Suppl. field: Yes / No # 20502.

Syntax

**C#**



public PropertyValue ARTICLEREF_ADDITIONAL_BOOLFIELD {get; set;}

public:

property PropertyValue^ ARTICLEREF_ADDITIONAL_BOOLFIELD {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Supplementary field for part reference data. Serves for the entry of free additional properties that can only assume two values ("Yes" or "No"). Outputs the value of the "Supplementary field Yes / No" (ID 20916) per part reference. You have to note the meaning specified by you of the supplementary field. This property can be used, for example in block properties or as a filter criterion in reports and during the manufacturing data export. In a parts list you can, for example, output only those parts for which this property is activated.
