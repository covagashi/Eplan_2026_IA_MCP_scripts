# Variant Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~Variant.html

---

The used variant.

Syntax

**C#**



public int Variant {get; set;}

public:

property int Variant {

   int get();

   void set (    int value);

}


#### Property Value

The currently used variant as Int32 value. Variant\_A = 0 Variant\_B = 1 ... Variant\_Z = 25

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the macro was not opened before or could not opened successfully. |
