# ARTICLE_FUSE_PROTECTION_ON_SITE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FUSE_PROTECTION_ON_SITE().html

---

Amperage (fuse, on-site) # 26002.

Syntax

**C#**



public MDPropertyValue ARTICLE_FUSE_PROTECTION_ON_SITE {get; set;}

public:

property MDPropertyValue^ ARTICLE_FUSE_PROTECTION_ON_SITE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Current strength (in amperes) of the electrical fuses to be used as proposed or specified by the device manufacturer for the safety-oriented operation of the respective device.
