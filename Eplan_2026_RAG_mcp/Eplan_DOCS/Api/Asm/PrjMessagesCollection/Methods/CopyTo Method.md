# CopyTo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~CopyTo.html

---

Copies the elements of the `PrjMessagesCollection` to an Array, starting at a particular Array index.

Syntax

**C#**



public virtual void CopyTo( 

   BaseProjectMessage[] messages,

   int arrayIndex

)

public:

virtual void CopyTo( 

   array<BaseProjectMessage^>^ messages,

   int arrayIndex

)


#### Parameters

*messages*
:   The one-dimensional Array that is the destination of the elements copied from `PrjMessagesCollection`. The Array must have zero-based indexing.

*arrayIndex*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | `messages` is a null reference (Nothing in Visual Basic). |
| [System.ArgumentOutOfRangeException](#) | `arrayIndex` is less than 0. |
| [System.ArgumentException](#) | `messages` is multidimensional -or- `arrayIndex` is equal to or greater than the length of `messages` -or- The number of elements in the source `PrjMessagesCollection` is greater than the available space from `arrayIndex` to the end of the destination array. |
