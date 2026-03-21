# ARTICLE_DELIVERYLENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DELIVERYLENGTH().html

---

Delivery length # 22058.

Syntax

**C#**



public MDPropertyValue ARTICLE_DELIVERYLENGTH {get; set;}

public:

property MDPropertyValue^ ARTICLE_DELIVERYLENGTH {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Delivery length of the parts. During a part selection or device selection the property is filled with the corresponding value of the delivery length from the parts management. You can use the property in forms for the parts list, for example in calculation formulas for calculating the order length.
