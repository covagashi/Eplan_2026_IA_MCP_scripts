# FUNC_ARTICLE_INPUT_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_INPUT_VOLUME_FLOW(Int32).html

---

Input flow rate # 26280.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INPUT_VOLUME_FLOW( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INPUT_VOLUME_FLOW {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Flow rate flowing through the input connection.
