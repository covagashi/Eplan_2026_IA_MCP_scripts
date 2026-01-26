# Add Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~Add.html

---

Adds an item to the `MDPartsDatabaseMessages`.

Syntax

**C#**



public virtual void Add( 

   MDPartsMessage msg

)

public:

virtual void Add( 

   MDPartsMessage^ msg

)


#### Parameters

*msg*
:   The message to add to the `MDPartsDatabaseMessages`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `MDPartsDatabaseMessages` is read-only. |
