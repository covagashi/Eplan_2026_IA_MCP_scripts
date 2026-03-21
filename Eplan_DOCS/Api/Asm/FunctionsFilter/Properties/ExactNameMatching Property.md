# ExactNameMatching Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~ExactNameMatching.html

---

Gets/Sets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter. Dafault this property is `false`.

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

Function[] functions = p.Functions; //now we have all functions named exactly "AP+ST-X"

p.Filter.ExactNameMatching = false;

functions = p.Functions; //now we have all functions that name starts from "AP+ST-X"
```
