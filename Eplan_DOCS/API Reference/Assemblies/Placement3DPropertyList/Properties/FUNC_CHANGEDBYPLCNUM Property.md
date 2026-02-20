# FUNC_CHANGEDBYPLCNUM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CHANGEDBYPLCNUM().html

---

Numbered using PLC data # 20812.

Syntax

**C#**



public PropertyValue FUNC_CHANGEDBYPLCNUM {get; set;}

public:

property PropertyValue^ FUNC_CHANGEDBYPLCNUM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Shows whether the DT (or the terminal / pin designation) was changed by numbering with PLC data. The property is automatically set when numbering but can also be set manually.
