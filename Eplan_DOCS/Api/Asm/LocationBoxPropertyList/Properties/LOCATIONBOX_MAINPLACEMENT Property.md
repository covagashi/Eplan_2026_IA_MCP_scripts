# LOCATIONBOX_MAINPLACEMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationBoxPropertyList~LOCATIONBOX_MAINPLACEMENT().html

---

Main placement # 20305.

Syntax

**C#**



public PropertyValue LOCATIONBOX_MAINPLACEMENT {get; set;}

public:

property PropertyValue^ LOCATIONBOX_MAINPLACEMENT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Defines the structure box as a main placement to which cross-references refer. This allows the display of cross-references between structure boxes. If the property is not enabled at any box, then the first structure box in the graphic is regarded as the main placement.
