# PART_ACCESSORYPLACEMENT_LASTCHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ACCESSORYPLACEMENT_LASTCHANGE().html

---

Last editor / Modification date (accessory placement) # 22973.

Syntax

**C#**



public MDPropertyValue PART_ACCESSORYPLACEMENT_LASTCHANGE {get; set;}

public:

property MDPropertyValue^ PART_ACCESSORYPLACEMENT_LASTCHANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Last change to part in the "Accessory placement" hierarchy level in parts management. The time is output in the local time of the user in accordance with the set time zone.
