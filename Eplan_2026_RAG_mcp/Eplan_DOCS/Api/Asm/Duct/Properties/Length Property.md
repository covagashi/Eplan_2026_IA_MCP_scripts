# Length Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Duct~Length.html

---

Returns and sets length of this object. Length is stored in mm.

Syntax

**C#**



public override double Length {set;}

public:

property double Length {

   void set (    double value) override;

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Length must be grater then zero. |
| [Eplan.EplApi.DataModel.OperationFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OperationFailedException.html) | Failed to set the length. |
