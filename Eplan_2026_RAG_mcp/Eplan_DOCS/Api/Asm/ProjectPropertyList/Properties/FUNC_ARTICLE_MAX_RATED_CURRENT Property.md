# FUNC_ARTICLE_MAX_RATED_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAX_RATED_CURRENT(Int32).html

---

Nominal current, max. # 26501.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MAX_RATED_CURRENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MAX_RATED_CURRENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum permissible current that an electrical device or a plant can carry continuously without overheating or damage occurring. This value is, among other things, decisive for the dimensioning of items and fuses.
