# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~Name.html

---

Returns the name that was set to this filter.

Syntax

**C#**



public string Name {get; set;}

public:

property String^ Name {

   String^ get();

   void set (    String^ value);

}


#### Property Value

Name that was set on this filter.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown while setting when `null` is given as a new value. |
