# FUNC_ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic453.html

---

Suitable for degree of protection (IP) # 26359.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Classification of the protection of a device or a component against the penetration of foreign objects and water. The IP degree of protection (International Protection) is specified by two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
