# CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic115.html

---

Unit for alternative connection cross-section / diameter # 31065.

Syntax

**C#**



public PropertyValue CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT {get; set;}

public:

property PropertyValue^ CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The alternative unit belonging to the alternative cross-section/diameter of the connection. Has to be entered manually and enables you to display the connection cross-section / diameter in parallel in different units. Possible values are:

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
