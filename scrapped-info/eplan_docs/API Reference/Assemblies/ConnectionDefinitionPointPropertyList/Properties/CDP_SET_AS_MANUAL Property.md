# CDP_SET_AS_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_SET_AS_MANUAL().html

---

Manually set # 31046.

Syntax

**C#**



public PropertyValue CDP_SET_AS_MANUAL {get; set;}

public:

property PropertyValue^ CDP_SET_AS_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Controls the editing possibilities of the connection numbering. Connection definition points which have this property can be excluded by the actions "Designate," "Realign," "Format" as well as being deleted. This property can be automatically set on designation (depending on the settings).
