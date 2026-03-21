# FUNC_ARTICLE_COLLECTION_VOLUME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_COLLECTION_VOLUME(Int32).html

---

Retention volume # 26222.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_COLLECTION_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_COLLECTION_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume which a container or a device can receive for collecting excess fluids or materials. This is relevant to prevent leaks or overflows.
