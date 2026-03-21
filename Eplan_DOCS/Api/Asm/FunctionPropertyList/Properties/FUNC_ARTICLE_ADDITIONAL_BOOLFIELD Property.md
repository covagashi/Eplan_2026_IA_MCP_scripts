# FUNC_ARTICLE_ADDITIONAL_BOOLFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_ADDITIONAL_BOOLFIELD(Int32).html

---

Supplementary field Yes / No # 20916.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ADDITIONAL_BOOLFIELD( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ADDITIONAL_BOOLFIELD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Supplementary field for part reference data. Serves for the entry of free additional properties that can only assume two values ("Yes" or "No"). Entry is effected in the user interface via a check box. You have to note the meaning specified by you of the supplementary field. The index is used to carry out the assignment of the associated part reference, max. 50 supplementary fields can be specified. The value of this property is transferred to the "Suppl. field Yes / No" (ID 20502) property that can be used, for example, in block properties, in reports and during the manufacturing data export.
