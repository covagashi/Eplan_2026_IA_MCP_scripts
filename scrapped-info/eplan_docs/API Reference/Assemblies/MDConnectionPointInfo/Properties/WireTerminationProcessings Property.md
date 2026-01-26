# WireTerminationProcessings Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~WireTerminationProcessings.html

---

Returns a map of ids and theirs names of all possible wire termination processing.

Syntax

**C#**



public IDictionary<short,MultiLangString> WireTerminationProcessings {get;}

public:

property IDictionary<short,MultiLangString^>^ WireTerminationProcessings {

   IDictionary<short,MultiLangString^>^ get();

}


Remarks

Some of them are default, the rest is user defined in the parts database. To change wire termination processing, set the property PART\_TERMINAL\_TYPEDEFAULT to index of an appropriate entry of [WireTerminationProcessings](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionPointInfo~WireTerminationProcessings.html) array
