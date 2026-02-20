# DESIGNATION_DOCTYPE_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~DESIGNATION_DOCTYPE_PART().html

---

Document type (single component) # 1528.

Syntax

**C#**



public PropertyValue DESIGNATION_DOCTYPE_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_DOCTYPE_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the document type that is entered at this planning object. The entire document type for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
