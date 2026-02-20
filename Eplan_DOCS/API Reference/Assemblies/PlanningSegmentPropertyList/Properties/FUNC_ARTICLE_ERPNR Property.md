# FUNC_ARTICLE_ERPNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_ERPNR(Int32).html

---

ERP / PDM number 1 # 31117.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ERPNR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ERPNR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

This property can be used to filter in the project data navigators. By default, the property is preset with the value of the part property "ERP / PDM number 1" (ID 22056) of the associated part. During entry as many characters as you wish are possible, but only the first 64 characters in the UTF-8 format are identifying. A max. of 50 definitions can be defined using the index.
