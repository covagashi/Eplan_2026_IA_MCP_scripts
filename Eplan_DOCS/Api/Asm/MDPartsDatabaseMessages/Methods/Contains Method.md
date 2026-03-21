# Contains Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~Contains.html

---

Determines whether the `MDPartsDatabaseMessages` contains a specific value.

Syntax

**C#**



public virtual bool Contains( 

   MDPartsMessage message

)

public:

virtual bool Contains( 

   MDPartsMessage^ message

)


#### Parameters

*message*
:   The message to locate in the `MDPartsDatabaseMessages`.

#### Return Value

Returns true if item is found in the `MDPartsDatabaseMessages`; otherwise, false.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `MDPartsDatabaseMessages` is read-only. |
