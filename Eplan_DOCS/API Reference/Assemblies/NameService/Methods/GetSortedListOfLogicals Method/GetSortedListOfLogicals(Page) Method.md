# GetSortedListOfLogicals(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~GetSortedListOfLogicals(Page).html

---

Sets the page and returns a sorted list of logicals (that is everything derived from functionbase). The logicals are sorted in that way, so that objects which are dependent on the name of other logicals are sorted behind them.

Syntax

**C#**



public FunctionBase[] GetSortedListOfLogicals( 

   Page pPage

)

public:

array<FunctionBase^>^ GetSortedListOfLogicals( 

   Page^ pPage

)


#### Parameters

*pPage*
:   Page to set.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
