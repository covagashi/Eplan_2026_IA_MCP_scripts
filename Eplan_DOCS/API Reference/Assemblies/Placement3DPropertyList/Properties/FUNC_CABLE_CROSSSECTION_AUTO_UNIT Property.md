# FUNC_CABLE_CROSSSECTION_AUTO_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_CROSSSECTION_AUTO_UNIT().html

---

Cable / Conduit: Unit for cross-section / diameter (automatic) # 20124.

Syntax

**C#**



public PropertyValue FUNC_CABLE_CROSSSECTION_AUTO_UNIT {get; set;}

public:

property PropertyValue^ FUNC_CABLE_CROSSSECTION_AUTO_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Automatically determined unit for the cross-section or diameter of the cable or conduit. Possible values are:

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

For pipes and hoses in fluid power and process engineering the property refers to the inner diameter.
