# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Remove.html

---

Removes the first occurrence of a specific object from the `PrjMessagesCollection`.

Syntax

**C#**



public virtual bool Remove( 

   BaseProjectMessage msg

)

public:

virtual bool Remove( 

   BaseProjectMessage^ msg

)


#### Parameters

*msg*
:   The object to remove to the `PrjMessagesCollection`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `PrjMessagesCollection` is read-only. |
