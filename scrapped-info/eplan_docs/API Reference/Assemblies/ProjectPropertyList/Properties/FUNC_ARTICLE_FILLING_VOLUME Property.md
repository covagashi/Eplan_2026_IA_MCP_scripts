# FUNC_ARTICLE_FILLING_VOLUME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_FILLING_VOLUME(Int32).html

---

Fill volume # 26347.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FILLING_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FILLING_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume specification about the space occupied by the filler. The maximum volume that a container or similar product can hold.
