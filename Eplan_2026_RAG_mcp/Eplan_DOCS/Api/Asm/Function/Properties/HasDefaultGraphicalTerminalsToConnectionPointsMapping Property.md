# HasDefaultGraphicalTerminalsToConnectionPointsMapping Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~HasDefaultGraphicalTerminalsToConnectionPointsMapping.html

---

Determines if connection points to graphical terminals mapping is the default mapping, according to the symbol. Please refer to the line "Symbol connection point" in dialog "Connection point logic" in GUI. This property returns ... true, if all Symbol connection points are mapped to the respective connection point of the Function. false, if the mapping on the Function was changed in regard to the Symbol.

Syntax

**C#**



public bool HasDefaultGraphicalTerminalsToConnectionPointsMapping {get;}

public:

property bool HasDefaultGraphicalTerminalsToConnectionPointsMapping {

   bool get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it was impossible to read the mapping |
