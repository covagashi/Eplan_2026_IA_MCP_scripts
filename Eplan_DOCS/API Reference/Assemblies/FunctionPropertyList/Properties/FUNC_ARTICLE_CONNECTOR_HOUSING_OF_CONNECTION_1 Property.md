# FUNC_ARTICLE_CONNECTOR_HOUSING_OF_CONNECTION_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic217.html

---

Plug-in connector housing (connection 1) # 26580.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CONNECTOR_HOUSING_OF_CONNECTION_1( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CONNECTOR_HOUSING_OF_CONNECTION_1 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specific details and properties of the housing that protects the plug-in connector at connection point 1, for example at a patch cable (prefabricated cable that is provided with plugs at both ends). Possible specifications are, for example, the type of construction, the material, etc.
