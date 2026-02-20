# FUNC_ARTICLE_NUMBER_OF_OUTPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic972.html

---

Opening pressure # 26523.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_OPENING_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_OPENING_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Pressure at which a valve begins to open under defined conditions.
