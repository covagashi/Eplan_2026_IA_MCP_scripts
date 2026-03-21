# FUNC_ARTICLE_ADDITIONAL_TEXTFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ADDITIONAL_TEXTFIELD(Int32).html

---

Suppl. field: Text # 20915.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ADDITIONAL_TEXTFIELD( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ADDITIONAL_TEXTFIELD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Supplementary field for part reference data. Serves for the entry of free additional properties. Entry is effected in the user interface via a text box. You have to note the meaning specified by you of the supplementary field. The index is used to carry out the assignment of the associated part reference, max. 50 supplementary fields can be specified. The value of this property is transferred to the "Suppl. field Text" (ID 20501) property that can be used, for example, in block properties, in reports and during the manufacturing data export.
