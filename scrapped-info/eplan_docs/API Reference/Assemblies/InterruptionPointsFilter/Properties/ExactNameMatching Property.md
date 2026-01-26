# ExactNameMatching Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~ExactNameMatching.html

---

Sets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter. Dafault this property is `false`.

Syntax

**C#**



public bool ExactNameMatching {get; set;}

public:

property bool ExactNameMatching {

   bool get();

   void set (    bool value);

}


Example

**C#**

```
Project proj;//a valid project

Page p;//a valid page object

p.Filter.ExactNameMatching = true;

p.Filter.Name = "AP+ST-X";

InterruptionPoint[] interruptionPoints = p.InterruptionPoints; //now we have all InterruptionPoints named exactly "AP+ST-X"

p.Filter.ExactNameMatching = false;

interruptionPoints = p.InterruptionPoints; //now we have all InterruptionPoints that name starts from "AP+ST-X"
```
