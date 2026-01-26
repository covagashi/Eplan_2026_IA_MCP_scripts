# FUNC_CABLELENGTH_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLELENGTH_UNIT().html

---

Cable / Conduit: Unit of length # 20065.

Syntax

**C#**



public PropertyValue FUNC_CABLELENGTH_UNIT {get; set;}

public:

property PropertyValue^ FUNC_CABLELENGTH_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Displayed measuring unit for the cable length or length of the conduit. Possible values are:

0 = As in project

1 = mm

2 = cm

3 = dm

4 = m

5 = Meter

6 = km

8 = Inch

9 = "

10 = In

11 = ft

12 = feet

13 = foot

14 = yd

15 = yard

29 = µm.
