# PAGE_CRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_CRAFT().html

---

Trade # 11037.

Syntax

**C#**



public PropertyValue PAGE_CRAFT {get; set;}

public:

property PropertyValue^ PAGE_CRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Determines the technology to be applied or selected. Depending on the page type, miscellaneous trades are available for a project page:

0 = Electrical engineering

1 = Mechanics

2 = Hydraulics

3 = Pneumatics

4 = Cooling

5 = Lubrication

6 = Process engineering

7 = Fluid power, general

99 = General.

The "General" trade is the default setting when generating report pages. If you filter defined working sections by certain trades, pages with the "General" trade are output along any other trade.
