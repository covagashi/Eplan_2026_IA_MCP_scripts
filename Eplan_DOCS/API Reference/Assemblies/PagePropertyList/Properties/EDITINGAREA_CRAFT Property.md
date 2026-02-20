# EDITINGAREA_CRAFT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~EDITINGAREA_CRAFT().html

---

Trade (Defined working sections) # 25000.

Syntax

**C#**



public PropertyValue EDITINGAREA_CRAFT {get; set;}

public:

property PropertyValue^ EDITINGAREA_CRAFT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Can be used in the filter schemes for defined working sections in order to filter pages, functions, and connections by trade. The following values are possible:

0 = Electrical engineering

1 = Fluid power, general

2 = Mechanics

3 = Process engineering.

99 = General.

In this context, the "Fluid power, general" setting includes also the trades Hydraulics, Pneumatics, Cooling, and Lubrication. Pages contain the additional trade setting "General". The "General" trade is the default setting when generating report pages. If you filter defined working sections by certain trades, pages with the "General" trade are output along any other trade.
