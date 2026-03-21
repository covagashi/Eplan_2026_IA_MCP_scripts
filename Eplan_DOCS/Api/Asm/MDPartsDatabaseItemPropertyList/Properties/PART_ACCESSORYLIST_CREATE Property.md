# PART_ACCESSORYLIST_CREATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ACCESSORYLIST_CREATE().html

---

Creator / Creation date (accessory list) # 22936.

Syntax

**C#**



public MDPropertyValue PART_ACCESSORYLIST_CREATE {get; set;}

public:

property MDPropertyValue^ PART_ACCESSORYLIST_CREATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Creation date of the accessory list (hierarchy level "Accessory list" in parts management). The time is output in the local time of the user in accordance with the set time zone.
