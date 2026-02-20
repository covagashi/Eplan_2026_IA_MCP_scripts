# FUNC_ARTICLE_START_UP_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_START_UP_TIME(Int32).html

---

Switch-on time # 26193.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_START_UP_TIME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_START_UP_TIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Time interval which has elapsed between the application of the control signal (electrical or pneumatic) and the pressure increase at the corresponding valve outlet until 10% of the specified working pressure is reached.
