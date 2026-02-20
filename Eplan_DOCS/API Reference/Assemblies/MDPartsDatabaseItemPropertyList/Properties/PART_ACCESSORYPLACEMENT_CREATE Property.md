# PART_ACCESSORYPLACEMENT_CREATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ACCESSORYPLACEMENT_CREATE().html

---

Creator / Creation date (accessory placement) # 22972.

Syntax

**C#**



public MDPropertyValue PART_ACCESSORYPLACEMENT_CREATE {get; set;}

public:

property MDPropertyValue^ PART_ACCESSORYPLACEMENT_CREATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Creation date of the part of the "Accessory placement" hierarchy level in parts management. The time is output in the local time of the user in accordance with the set time zone.
