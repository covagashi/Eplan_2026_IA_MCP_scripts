# CONNECTION_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRECROSSSECTION_UNIT().html

---

Unit for connection cross-section / diameter # 31059.

Syntax

**C#**



public PropertyValue CONNECTION_WIRECROSSSECTION_UNIT {get; set;}

public:

property PropertyValue^ CONNECTION_WIRECROSSSECTION_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Units of the connection cross-section or diameter. Possible values are:

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
