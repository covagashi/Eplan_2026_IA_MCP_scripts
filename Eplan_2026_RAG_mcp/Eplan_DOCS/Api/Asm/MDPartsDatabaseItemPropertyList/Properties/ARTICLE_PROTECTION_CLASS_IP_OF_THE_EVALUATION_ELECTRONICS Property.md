# ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1660.html

---

Degree of protection (IP): Evaluation electronics # 26555.

Syntax

**C#**



public MDPropertyValue ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS {get; set;}

public:

property MDPropertyValue^ ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Describes the degree of protection offered by the housing of the evaluation electronics against the penetration of foreign objects (such as dust) and water. These protection categories are indicated by the IP code (International Protection Code), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
