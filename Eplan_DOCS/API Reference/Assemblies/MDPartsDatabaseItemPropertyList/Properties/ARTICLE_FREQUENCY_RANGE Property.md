# ARTICLE_FREQUENCY_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FREQUENCY_RANGE().html

---

Frequency range # 26342.

Syntax

**C#**



public MDPropertyValue ARTICLE_FREQUENCY_RANGE {get; set;}

public:

property MDPropertyValue^ ARTICLE_FREQUENCY_RANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Range of the frequencies in which a device or system works. The value is often specified in Hertz (Hz) or Kilohertz (kHz) and specifies the minimum and maximum frequencies that a device can process or generate.
