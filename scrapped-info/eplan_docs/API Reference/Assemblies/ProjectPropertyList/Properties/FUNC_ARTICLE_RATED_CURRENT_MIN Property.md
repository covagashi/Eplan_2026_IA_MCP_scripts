# FUNC_ARTICLE_RATED_CURRENT_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_RATED_CURRENT_MIN(Int32).html

---

Nominal current, min. # 26503.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_CURRENT_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_CURRENT_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum value of the current that an electrical device or a component requires to function properly. For example, sensors often require a minimum current in order to carry out precise measurements.
