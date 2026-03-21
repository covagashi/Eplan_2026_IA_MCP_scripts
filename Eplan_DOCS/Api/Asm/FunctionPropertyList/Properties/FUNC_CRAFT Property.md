# FUNC_CRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CRAFT().html

---

Trade # 20466.

Syntax

**C#**



public PropertyValue FUNC_CRAFT {get; set;}

public:

property PropertyValue^ FUNC_CRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Determines the technology to be applied or selected. The following values are possible:

0 = Electrical engineering,

1 = Mechanics,

2 = Hydraulics,

3 = Pneumatics,

4 = Cooling,

5 = Lubrication,

6 = Process engineering,

7 = Cooling lubricant,

8 = Gas engineering,

9 = Fluid power, general.
