# PART_CONSTRUCTION_CREATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_CONSTRUCTION_CREATE().html

---

Creator / Creation date (drilling pattern) # 22939.

Syntax

**C#**



public MDPropertyValue PART_CONSTRUCTION_CREATE {get; set;}

public:

property MDPropertyValue^ PART_CONSTRUCTION_CREATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Creation date of the drilling pattern. The time is output in the local time of the user in accordance with the set time zone.
