# FUNC_ARTICLE_CLIMATE_CLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CLIMATE_CLASS(Int32).html

---

Climate class # 26408.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CLIMATE_CLASS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CLIMATE_CLASS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification of the environmental climatic conditions, i.e. air temperature, humidity and pressure at specific operating locations, that may occur during operation (including downtimes), storage or transportation on land or at sea. Maintenance and repair conditions are not included.
