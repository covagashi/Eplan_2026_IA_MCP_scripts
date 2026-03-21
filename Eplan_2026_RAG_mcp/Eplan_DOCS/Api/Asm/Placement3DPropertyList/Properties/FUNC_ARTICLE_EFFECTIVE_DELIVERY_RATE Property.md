# FUNC_ARTICLE_EFFECTIVE_DELIVERY_RATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic539.html

---

Effective delivery amount # 26272.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EFFECTIVE_DELIVERY_RATE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EFFECTIVE_DELIVERY_RATE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of material dispensed per time unit.
