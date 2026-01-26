# CONNECTION_AUTO_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic117.html

---

Unit for connection cross-section / diameter (automatic) # 31060.

Syntax

**C#**



public PropertyValue CONNECTION_AUTO_WIRECROSSSECTION_UNIT {get; set;}

public:

property PropertyValue^ CONNECTION_AUTO_WIRECROSSSECTION_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Automatically determined units of the connection cross-section or diameter. Possible values are:

0 = Undefined

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
