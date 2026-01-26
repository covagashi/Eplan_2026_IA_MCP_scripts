# ARTICLE_SLOT_GAP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SLOT_GAP().html

---

Slot width # 22286.

Syntax

**C#**



public MDPropertyValue ARTICLE_SLOT_GAP {get; set;}

public:

property MDPropertyValue^ ARTICLE_SLOT_GAP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Width of a slot between two wire duct fingers. This part property is required solely for the manufacturing data export for the Rittal Secarex cutting center. This property does not have any influence on the graphical representation of the wire duct in a layout space.
