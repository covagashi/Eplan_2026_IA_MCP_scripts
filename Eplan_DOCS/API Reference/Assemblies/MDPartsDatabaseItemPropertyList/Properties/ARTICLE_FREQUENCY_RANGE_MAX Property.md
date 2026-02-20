# ARTICLE_FREQUENCY_RANGE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FREQUENCY_RANGE_MAX().html

---

Frequency range, max. # 26330.

Syntax

**C#**



public MDPropertyValue ARTICLE_FREQUENCY_RANGE_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_FREQUENCY_RANGE_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum frequency that a device or system can process or generate. This specification is made in Hertz (Hz) or Kilohertz (kHz) and specifies the upper limit of the frequency range in which the device can operate effectively.
