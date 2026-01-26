# FUNC_TERMINAL_JUMPERBAR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_JUMPERBAR().html

---

Saddle jumper option # 20808.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_JUMPERBAR {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_JUMPERBAR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Indicates the saddle jumper option:

0 = Automatic

1 = Manual, start of jumper

2 = Manual, center of jumper

3 = Manual, end of jumper

4 = No automatic jumper

5 = Automatic, start of jumper

6 = Automatic, end of jumper.

The settings for automatic saddle jumpers are only available for terminals. The settings for manual saddle jumpers are only available for pins.
