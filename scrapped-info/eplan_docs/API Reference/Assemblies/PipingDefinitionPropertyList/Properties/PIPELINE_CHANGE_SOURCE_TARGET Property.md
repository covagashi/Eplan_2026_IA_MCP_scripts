# PIPELINE_CHANGE_SOURCE_TARGET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~PIPELINE_CHANGE_SOURCE_TARGET().html

---

Piping: Exchange source and target # 33301.

Syntax

**C#**



public PropertyValue PIPELINE_CHANGE_SOURCE_TARGET {get; set;}

public:

property PropertyValue^ PIPELINE_CHANGE_SOURCE_TARGET {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Through this entry you specify whether the target designations of a piping correspond to the targets of the underlying connection or the source and target have been exchanged.
