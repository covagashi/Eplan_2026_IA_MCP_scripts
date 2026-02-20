# FUNC_ARTICLE_RATED_SPEED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_SPEED(Int32).html

---

Nominal rotation speed # 26469.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_SPEED( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_SPEED {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Rotation speed at which a motor or machine outputs the maximum power under normal operating conditions. This rotation speed is specified in revolutions per minute (rpm).
