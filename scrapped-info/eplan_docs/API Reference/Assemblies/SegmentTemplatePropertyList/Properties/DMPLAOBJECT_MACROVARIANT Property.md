# DMPLAOBJECT_MACROVARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~DMPLAOBJECT_MACROVARIANT().html

---

Macro: Variant # 44093.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_MACROVARIANT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_MACROVARIANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specifies the macro variant for the macro specified in the Macro (ID 44008) property at a planning object. The preset macro and the preset variant of this macro are used when creating the detailed planning. The property is also taken into consideration during the export and import of pre-planning data for external editing as well as during the pre-planning import.
