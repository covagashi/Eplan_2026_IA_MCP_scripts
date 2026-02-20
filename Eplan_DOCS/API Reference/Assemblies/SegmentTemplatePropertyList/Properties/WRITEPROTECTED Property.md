# WRITEPROTECTED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~WRITEPROTECTED().html

---

Change protection # 3014.

Syntax

**C#**



public PropertyValue WRITEPROTECTED {get; set;}

public:

property PropertyValue^ WRITEPROTECTED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

If this property is activated for an object (e.g. page, function, planning object, hierarchy level in a navigator) the complete object as well as all the subordinate objects are protected against all types of change. This means that not only the parts data are protected, as at device protection, but rather that all the properties of the object can no longer be changed and that the object cannot be deleted or moved. This property is assigned automatically inter alia during the generation of subprojects.
