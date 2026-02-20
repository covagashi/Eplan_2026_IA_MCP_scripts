# FUNC_ARTICLE_THROUGHPUT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_THROUGHPUT(Int32).html

---

Throughput # 26270.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_THROUGHPUT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_THROUGHPUT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Quantity that is processed or transferred within a specified time period through a predefined limit. Kvs value of the valve in cubic meters per hour (m³/h).
