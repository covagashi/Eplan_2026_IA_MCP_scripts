# POTENTIAL_VALID_POTENTIALS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~POTENTIAL_VALID_POTENTIALS().html

---

Possible counter potentials # 33005.

Syntax

**C#**



public PropertyValue POTENTIAL_VALID_POTENTIALS {get; set;}

public:

property PropertyValue^ POTENTIAL_VALID_POTENTIALS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Enter here which other potentials may be connected to the same consumer. This property is only used for information purposes and can be output in the potential overview for documentation purposes.
