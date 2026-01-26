# ARTICLE_CAPACITIVE_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CAPACITIVE_LOAD().html

---

Capacitive load # 26402.

Syntax

**C#**



public PropertyValue ARTICLE_CAPACITIVE_LOAD {get; set;}

public:

property PropertyValue^ ARTICLE_CAPACITIVE_LOAD {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specific properties of a capacitive load, for example capacitance, nominal voltage, nominal current, inrush current, etc. Capacitive loads are electric consumers which store electric energy in the electric field of a capacitor. These loads influence the phase angle between the current and voltage in an AC circuit, which leads to the current running ahead of the voltage.
