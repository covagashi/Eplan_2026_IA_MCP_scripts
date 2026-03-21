# Selected Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart+PropertyPlacementsSchemasList~Selected.html

---

Gets a PropertyPlacementsSchema object that represents the selected property placements configuration. Sets the current property placements configuration. Note: Changing the current property placements configuration deletes the existing property placements. This can make some API objects of type PropertyPlacement become invalid.

Syntax

**C#**



public ViewPart.PropertyPlacementsSchema Selected {get; set;}

public:

property ViewPart.PropertyPlacementsSchema^ Selected {

   ViewPart.PropertyPlacementsSchema^ get();

   void set (    ViewPart.PropertyPlacementsSchema^ value);

}

