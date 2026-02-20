# ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1539.html

---

Power circuit breaker - test available # 26433.

Syntax

**C#**



public MDPropertyValue ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE {get; set;}

public:

property MDPropertyValue^ ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specifies whether a power circuit breaker has already been checked and the corresponding check results are available. Example: For a low-voltage power circuit breaker the check includes, for example, the check of the contact resistance, the switching time measurement and the isolation test.
