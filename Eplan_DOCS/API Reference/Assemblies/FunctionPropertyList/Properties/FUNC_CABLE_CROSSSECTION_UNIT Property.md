# FUNC_CABLE_CROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLE_CROSSSECTION_UNIT().html

---

Cable / Conduit: Unit for cross-section / diameter # 20068.

Syntax

**C#**



public PropertyValue FUNC_CABLE_CROSSSECTION_UNIT {get; set;}

public:

property PropertyValue^ FUNC_CABLE_CROSSSECTION_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Unit for the cross-section or diameter. Possible values are:

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

For pipes and hoses in fluid power and process engineering the property refers to the inner diameter.
