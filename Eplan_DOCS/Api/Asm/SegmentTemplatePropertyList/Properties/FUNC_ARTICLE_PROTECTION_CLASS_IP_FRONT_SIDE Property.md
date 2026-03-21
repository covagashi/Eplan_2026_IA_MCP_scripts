# FUNC_ARTICLE_PROTECTION_CLASS_IP_FRONT_SIDE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1227.html

---

Degree of protection (IP): Mounted # 26562.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROTECTION_CLASS_IP_MOUNTED( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROTECTION_CLASS_IP_MOUNTED {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Degree of protection of a device against the penetration of foreign objects and water when the device is mounted.
