# PAGE_DONT_CHANGESTANDARD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_DONT_CHANGESTANDARD().html

---

Change of standard: Do not rotate and flip # 11060.

Syntax

**C#**



public PropertyValue PAGE_DONT_CHANGESTANDARD {get; set;}

public:

property PropertyValue^ PAGE_DONT_CHANGESTANDARD {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Pages with this property are not rotated or flipped when changing standards. This property is activated by default for pages with type "Fluid power schematic".
