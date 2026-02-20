# ARTICLE_FREQUENCY_RANGE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FREQUENCY_RANGE_MIN().html

---

Frequency range, min. # 26332.

Syntax

**C#**



public MDPropertyValue ARTICLE_FREQUENCY_RANGE_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_FREQUENCY_RANGE_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum frequency that a device or system can process or generate. This specification is made in Hertz (Hz) or Kilohertz (kHz) and specifies the lower limit of the frequency range in which the device can operate effectively.
