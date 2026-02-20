# FUNC_PLCCPU Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCCPU().html

---

CPU: Name # 20433.

Syntax

**C#**



public PropertyValue FUNC_PLCCPU {get; set;}

public:

property PropertyValue^ FUNC_PLCCPU {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs a semicolon-separated list of all the CPU names that are entered at the PLC box. The display is effected without gaps, meaning that empty entries are not listed.
