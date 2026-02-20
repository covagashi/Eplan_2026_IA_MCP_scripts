# CONNECTION_WIRELENGTH_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRELENGTH_UNIT().html

---

Connection: Unit of length # 31001.

Syntax

**C#**



public PropertyValue CONNECTION_WIRELENGTH_UNIT {get; set;}

public:

property PropertyValue^ CONNECTION_WIRELENGTH_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Display unit of the length. Possible values are:

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
