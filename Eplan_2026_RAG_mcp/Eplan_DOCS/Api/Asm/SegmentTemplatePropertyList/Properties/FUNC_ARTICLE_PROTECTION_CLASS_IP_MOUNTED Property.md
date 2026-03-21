# FUNC_ARTICLE_PROTECTION_CLASS_IP_MOUNTED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1228.html

---

Degree of protection (IP): Evaluation electronics # 26556.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describes the degree of protection offered by the housing of the evaluation electronics against the penetration of foreign objects (such as dust) and water. These protection categories are indicated by the IP code (International Protection Code), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
