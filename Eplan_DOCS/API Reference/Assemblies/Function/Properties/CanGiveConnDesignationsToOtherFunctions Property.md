# CanGiveConnDesignationsToOtherFunctions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CanGiveConnDesignationsToOtherFunctions.html

---

Returns flag, if this function can give connection designations to other functions (is meant for the Device-Tag-Editor, where sometimes there can be edited more connection designations than the actual function has)

Syntax

**C#**



public virtual bool CanGiveConnDesignationsToOtherFunctions {get;}

public:

virtual property bool CanGiveConnDesignationsToOtherFunctions {

   bool get();

}


#### Property Value

true : can give connection designations to other functions

false : cannot give connection designations to other functions

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the property cannot be obtained |
