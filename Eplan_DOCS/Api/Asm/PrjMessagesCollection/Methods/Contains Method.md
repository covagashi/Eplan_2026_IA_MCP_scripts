# Contains Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Contains.html

---

Determines whether the `PrjMessagesCollection` contains a specific value.

Syntax

**C#**



public virtual bool Contains( 

   BaseProjectMessage message

)

public:

virtual bool Contains( 

   BaseProjectMessage^ message

)


#### Parameters

*message*
:   The message to locate in the `PrjMessagesCollection`.

#### Return Value

true if item is found in the `PrjMessagesCollection`; otherwise, false.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `PrjMessagesCollection` is read-only. |
