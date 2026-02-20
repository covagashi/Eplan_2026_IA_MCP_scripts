# FUNC_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic216.html

---

Power circuit breaker - test available # 26434.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies whether a power circuit breaker has already been checked and the corresponding check results are available. Example: For a low-voltage power circuit breaker the check includes, for example, the check of the contact resistance, the switching time measurement and the isolation test.
