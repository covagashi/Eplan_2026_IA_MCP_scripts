# MatchingMateNames Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~MatchingMateNames.html

---

Names of mates that can be snapped to this one separated by '#'.

Syntax

**C#**



public string MatchingMateNames {get; set;}

public:

property String^ MatchingMateNames {

   String^ get();

   void set (    String^ value);

}


Remarks

Value can be'\*' which mean that all mates can be matched with this. Value "\*-R" means that this mate matches all other mates but without mates from mounting rail (name of such mates is 'R').
