# CABLINGSEGMENT_HEIGHT_DIFF Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.SegmentPropertyList~CABLINGSEGMENT_HEIGHT_DIFF().html

---

Topology: Height difference # 20347.

Syntax

**C#**



public PropertyValue CABLINGSEGMENT_HEIGHT_DIFF {get; set;}

public:

property PropertyValue^ CABLINGSEGMENT_HEIGHT_DIFF {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The routing length of the vertical routing path is displayed with preceding sign in this property. The preceding sign "+" means "upwards", "-" means "downwards". The property is only filled if a direction for the height difference was specified.
