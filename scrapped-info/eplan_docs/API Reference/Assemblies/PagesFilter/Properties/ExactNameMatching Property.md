# ExactNameMatching Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~ExactNameMatching.html

---

Gets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter.

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

proj.Filter.ExactNameMatching = true;

proj.Filter.Name = "=AP+ST1/1";

Page[] pages = proj.Pages; //now we have all pages named exactly "=AP+ST1/1"
```

**C#**

```
Project proj;//a valid project

p.Filter.ExactNameMatching = false;

proj.Filter.Name = "=AP+ST1";

pages = p.Pages; //now we have all pages with names starting with "=AP+ST1"
```
