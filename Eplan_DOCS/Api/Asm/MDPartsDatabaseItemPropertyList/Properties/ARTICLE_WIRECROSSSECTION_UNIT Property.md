# ARTICLE_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_WIRECROSSSECTION_UNIT().html

---

Unit for connection cross-section / diameter # 22068.

Syntax

**C#**



public MDPropertyValue ARTICLE_WIRECROSSSECTION_UNIT {get; set;}

public:

property MDPropertyValue^ ARTICLE_WIRECROSSSECTION_UNIT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Property of a part variant. Unit for the cross-section or diameter of the connections of a cable or conduit. Possible values are:

0 = As in project

1 = mm²

2 = sqmm

3 = AWG

4 = mm

5 = KCM

6 = MCM

7 = Zoll

8 = "

9 = inch

10 = µm

11 = kcmil

12 = µm².
