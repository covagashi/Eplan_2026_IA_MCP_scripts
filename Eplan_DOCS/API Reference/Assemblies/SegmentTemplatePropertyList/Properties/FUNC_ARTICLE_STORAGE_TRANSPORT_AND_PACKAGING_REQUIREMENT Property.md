# FUNC_ARTICLE_STORAGE_TRANSPORT_AND_PACKAGING_REQUIREMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1259.html

---

Jacket (cable) stripping length # 31176.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_STRIPPING_LENGTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_STRIPPING_LENGTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Length of the area on a cable where the outer sheath is removed or can be removed.
