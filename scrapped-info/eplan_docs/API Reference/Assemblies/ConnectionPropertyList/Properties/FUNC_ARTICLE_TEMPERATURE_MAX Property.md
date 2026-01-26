# FUNC_ARTICLE_TEMPERATURE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TEMPERATURE_MAX(Int32).html

---

Temperature, max. # 26608.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TEMPERATURE_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TEMPERATURE_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum operating temperature that a device or component can withstand safely without being damaged or functionality being impaired.
