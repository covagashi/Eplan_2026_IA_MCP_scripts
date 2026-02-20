# ARTICLE_CAN_BE_LINED_UP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CAN_BE_LINED_UP().html

---

Alignable # 22229.

Syntax

**C#**



public MDPropertyValue ARTICLE_CAN_BE_LINED_UP {get; set;}

public:

property MDPropertyValue^ ARTICLE_CAN_BE_LINED_UP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Shows whether a terminal part (terminal or accessories) can be aligned. Terminals can always be aligned. This property can be changed in the case of accessory parts. The property for accessories with product subgroups "Terminator," "End clamp" and "Partition" is enabled by default; it is not enabled by default for all other product subgroups.
