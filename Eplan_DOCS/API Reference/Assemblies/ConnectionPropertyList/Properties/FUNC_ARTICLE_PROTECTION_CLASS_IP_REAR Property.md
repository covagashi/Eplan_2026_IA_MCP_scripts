# FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR(Int32).html

---

Degree of protection (IP): Rear side # 26564.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROTECTION_CLASS_IP_REAR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Degree of protection of a device against the penetration of foreign objects and water at the rear of the device.
