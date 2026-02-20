# ARTICLE_FEEDBACK_CONTACT_PRESENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_FEEDBACK_CONTACT_PRESENT().html

---

Feedback contact available # 26061.

Syntax

**C#**



public MDPropertyValue ARTICLE_FEEDBACK_CONTACT_PRESENT {get; set;}

public:

property MDPropertyValue^ ARTICLE_FEEDBACK_CONTACT_PRESENT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification whether an electrical contact is available for a feedback signal or not. A feedback contact monitors the state or the position of a device or a component and forwards this information to a control system.
