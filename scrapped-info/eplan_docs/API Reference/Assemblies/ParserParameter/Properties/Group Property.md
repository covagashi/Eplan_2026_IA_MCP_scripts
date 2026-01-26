# Group Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Group.html

---

The UnitGroup Property. When first UnitID is set,the group is automatically defined by the unit. While setting a Group also the Unit can be changed to the first Unit in new Group if: - new Group is different than the Group of assigned Unit - there is no Unit and Group assigned When new assigned Group is the same like Unit Group, nothing will change. The unitparser can never convert units of different groups

Syntax

**C#**



public UnitGroup Group {get; set;}

public:

property UnitGroup Group {

   UnitGroup get();

   void set (    UnitGroup value);

}

