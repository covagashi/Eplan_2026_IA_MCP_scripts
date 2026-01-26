# ARTICLE_CALIBRATION_AUTHORISATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CALIBRATION_AUTHORISATION().html

---

Calibration approval # 26034.

Syntax

**C#**



public MDPropertyValue ARTICLE_CALIBRATION_AUTHORISATION {get; set;}

public:

property MDPropertyValue^ ARTICLE_CALIBRATION_AUTHORISATION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Official approval that confirms that a measuring instrument corresponds to the legal requirements and is approved for use in the trade or in the industry. This authorization ensures that the device delivers accurate and reliable measurements that comply with legal standards (e.g., precise specifications for packaging, vessels and scales, specifications for consumption meters such as water meters, gas meters, electricity meters, heat meters, etc.). Example: Approval code or approval number of certificates, accuracy class, year of calibration.
