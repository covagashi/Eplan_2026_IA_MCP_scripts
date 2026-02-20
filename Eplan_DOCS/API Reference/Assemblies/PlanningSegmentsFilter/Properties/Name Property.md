# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~Name.html

---

Value compared with property DMPLAOBJECT\_FULLDESIGNATION while searching for planning segments.

Syntax

**C#**



public string Name {get; set;}

public:

property String^ Name {

   String^ get();

   void set (    String^ value);

}


Remarks

If this value is set then [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html) limits the result to one object which exactly matches to property DMPLAOBJECT\_FULLDESIGNATION
