# ARTICLE_CABLE_LENGTH_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CABLE_LENGTH_MAX().html

---

Cable length, max. # 26117.

Syntax

**C#**



public MDPropertyValue ARTICLE_CABLE_LENGTH_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_CABLE_LENGTH_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum length of a cable that is permissible for a specific application or installation. Example: An extension cable may not be longer than 50 m in order to be used safely.
