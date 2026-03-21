# ARTICLE_CONTROL_SIGNAL_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTROL_SIGNAL_TYPE().html

---

Control signal: Type # 26583.

Syntax

**C#**



public MDPropertyValue ARTICLE_CONTROL_SIGNAL_TYPE {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTROL_SIGNAL_TYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Type of signal used to control an actuator or a valve. Example: A position controller receives (for example from a superior controller) the actuating signal in the form of a unit signal (for example 4-20 mA) and implements it on-site.
