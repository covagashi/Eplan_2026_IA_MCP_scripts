# FUNC_ARTICLE_PROTECTION_CLASS_IP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PROTECTION_CLASS_IP(Int32).html

---

Degree of protection (IP) # 26554.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROTECTION_CLASS_IP( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROTECTION_CLASS_IP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Extent of protection provided by a housing against access to hazardous parts and intrusion of solid foreign objects and/or water, as confirmed by standardized test methods. These protection categories are indicated by the IP code (International Protection Code), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
