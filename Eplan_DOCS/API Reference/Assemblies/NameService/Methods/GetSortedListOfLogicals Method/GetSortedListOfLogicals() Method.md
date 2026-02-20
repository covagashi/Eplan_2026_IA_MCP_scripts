# GetSortedListOfLogicals() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~GetSortedListOfLogicals().html

---

Returns a sorted list of logicals (that is everything derived from functionbase). The logicals are sorted in that way, so that objects which are dependent on the name of other logicals are sorted behind them.

Syntax

**C#**



public FunctionBase[] GetSortedListOfLogicals()

public:

array<FunctionBase^>^ GetSortedListOfLogicals();


Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | When page is not set. |
