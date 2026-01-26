# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~Remove.html

---

Removes the first occurrence of a message from the `MDPartsDatabaseMessages`.

Syntax

**C#**



public virtual bool Remove( 

   MDPartsMessage msg

)

public:

virtual bool Remove( 

   MDPartsMessage^ msg

)


#### Parameters

*msg*
:   The message to be removed from the `MDPartsDatabaseMessages`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `MDPartsDatabaseMessages` is read-only. |
