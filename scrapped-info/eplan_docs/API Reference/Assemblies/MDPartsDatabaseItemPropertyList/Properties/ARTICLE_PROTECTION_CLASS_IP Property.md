# ARTICLE_PROTECTION_CLASS_IP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PROTECTION_CLASS_IP().html

---

Degree of protection (IP) # 26553.

Syntax

**C#**



public MDPropertyValue ARTICLE_PROTECTION_CLASS_IP {get; set;}

public:

property MDPropertyValue^ ARTICLE_PROTECTION_CLASS_IP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Extent of protection provided by a housing against access to hazardous parts and intrusion of solid foreign objects and/or water, as confirmed by standardized test methods. These protection categories are indicated by the IP code (International Protection Code), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
