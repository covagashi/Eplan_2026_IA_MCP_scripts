# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame~Name.html

---

Get the name of the plot frame.

Syntax

**C#**



public string Name {get;}

public:

property String^ Name {

   String^ get();

}


#### Property Value

PlotFrame's name.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when name of the page cannot be read from data model. |
| [System.ArgumentNullException](#) | Thrown when `newName` is `null`. |
