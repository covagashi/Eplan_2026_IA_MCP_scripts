# ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1662.html

---

Protection type class (motor) # 26565.

Syntax

**C#**



public MDPropertyValue ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR {get; set;}

public:

property MDPropertyValue^ ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Classifies the extent of protection of an electric motor against direct contact, against penetration of solid foreign objects and/or against penetration of water. This degree of protection is indicated by the IP code (International Protection), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
