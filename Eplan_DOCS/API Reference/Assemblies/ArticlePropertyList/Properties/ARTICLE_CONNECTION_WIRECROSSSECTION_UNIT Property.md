# ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT().html

---

Connection: Unit for connection cross-section / diameter # 22255.

Syntax

**C#**



public PropertyValue ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT {get; set;}

public:

property PropertyValue^ ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Property of a part variant. Units of the connection cross-section or diameter. Possible values are:

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
