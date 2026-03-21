# ARTICLE_SUPPORTS_PROTOCOL_OUTGOING_EIB_KNX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1693.html

---

KNX: Supports EIB protocol, outgoing # 26065.

Syntax

**C#**



public MDPropertyValue ARTICLE_SUPPORTS_PROTOCOL_OUTGOING_EIB_KNX {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUPPORTS_PROTOCOL_OUTGOING_EIB_KNX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification whether the hardware disposes of an interface that uses a communication protocol for EIB/KNX for the outgoing data transmission.
