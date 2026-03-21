# FUNC_PLC_SUBSLOT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_SUBSLOT().html

---

Subslot # 20312.

Syntax

**C#**



public PropertyValue FUNC_PLC_SUBSLOT {get; set;}

public:

property PropertyValue^ FUNC_PLC_SUBSLOT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Some modules have built-in inputs and outputs or integrated interface modules that are shown as subslots. These subslots are not shown in the PLC navigator and are treated differently for data exchanges.
