# FUNC_TERMINAL_SECONDARY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_SECONDARY().html

---

Auxiliary terminal # 20228.

Syntax

**C#**



public PropertyValue FUNC_TERMINAL_SECONDARY {get; set;}

public:

property PropertyValue^ FUNC_TERMINAL_SECONDARY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Indicates whether the terminal is an auxiliary terminal. Terminals can be managed as main terminals or auxiliary terminals. This means that auxiliary terminals can be used, for example, to represent terminals which consist of several functions (several separate terminals in one housing).
