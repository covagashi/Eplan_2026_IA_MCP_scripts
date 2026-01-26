# CopyTo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~CopyTo.html

---

Copies the elements of the `MDPartsDatabaseMessages` to an Array, starting at a particular Array index.

Syntax

**C#**



public virtual void CopyTo( 

   MDPartsMessage[] messages,

   int arrayIndex

)

public:

virtual void CopyTo( 

   array<MDPartsMessage^>^ messages,

   int arrayIndex

)


#### Parameters

*messages*
:   The one-dimensional Array that is the destination of the elements copied from `MDPartsDatabaseMessages`. The Array must have zero-based indexing.

*arrayIndex*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | `Array of messages` is a null reference. |
| [System.ArgumentOutOfRangeException](#) | `ArrayIndex` is less than 0. |
| [System.ArgumentException](#) | `Array of messages` is multidimensional -or- `ArrayIndex` is equal to or greater than the length of `Array of messages` -or- The number of elements in the source `MDPartsDatabaseMessages` is greater than the available space from `arrayIndex` to the end of the destination array. |
