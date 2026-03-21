# DMPLAOBJECTDEFINITION_NUMBER_NO_SPACE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1069.html

---

Segment definition: Separator symbolic address # 44090.

Syntax

**C#**



public PropertyValue DMPLAOBJECTDEFINITION_PREFIX_SA {get; set;}

public:

property PropertyValue^ DMPLAOBJECTDEFINITION_PREFIX_SA {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The separator defined here precedes the individual component of a segment in the symbolic address. This allows the individual components of this segment to be differentiated from the individual components of the segments of the other structure levels. In order for a change in the symbolic address to be transferred to all other segments (planning objects, PCT loops) in the pre-planning navigator or to the placed PLC connection points in the schematic, you have to update the detailed planning and in the process select the option Update device tags and symbolic addresses.
