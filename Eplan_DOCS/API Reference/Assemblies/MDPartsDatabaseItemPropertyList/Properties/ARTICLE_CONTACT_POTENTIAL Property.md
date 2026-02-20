# ARTICLE_CONTACT_POTENTIAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTACT_POTENTIAL().html

---

Contact potential # 26119.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTACT_POTENTIAL {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTACT_POTENTIAL {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Electrical potential applied to an output contact. Example: The value is "24 V DC" for a relay, which means that the output contact of the relay has a potential of 24 V DC.
