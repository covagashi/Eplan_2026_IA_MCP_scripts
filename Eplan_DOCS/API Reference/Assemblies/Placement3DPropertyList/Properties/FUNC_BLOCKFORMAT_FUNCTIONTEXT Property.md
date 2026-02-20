# FUNC_BLOCKFORMAT_FUNCTIONTEXT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_BLOCKFORMAT_FUNCTIONTEXT().html

---

Block property: Format (function text, automatic) # 20545.

Syntax

**C#**



public PropertyValue FUNC_BLOCKFORMAT_FUNCTIONTEXT {get; set;}

public:

property PropertyValue^ FUNC_BLOCKFORMAT_FUNCTIONTEXT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Format for combining an automatic function text. The display of this function text defined by using the block property in the graphical editor is carried out via the placed property Function text (automatic). If a manual function text was entered at a function additionally, the Function text (automatic) property displays this text.
