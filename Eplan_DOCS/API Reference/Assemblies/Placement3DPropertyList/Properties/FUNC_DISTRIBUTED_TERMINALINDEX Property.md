# FUNC_DISTRIBUTED_TERMINALINDEX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DISTRIBUTED_TERMINALINDEX().html

---

Distributed terminal index # 20223.

Syntax

**C#**



public PropertyValue FUNC_DISTRIBUTED_TERMINALINDEX {get; set;}

public:

property PropertyValue^ FUNC_DISTRIBUTED_TERMINALINDEX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Distributed terminals are usually identified clearly via the terminal designation. But if you want to use identical designations for several distributed terminals (e.g., because terminals within a signal are to have the same terminal designation), then the distributed terminals must also have the same terminal designation. In this case, the distributed terminals are differentiated via the distributed terminal index. Distributed terminals with the same distributed terminal index are recognized as belonging together. The value of this property can be entered manually, or be assigned automatically during the optimization of the distributed terminals.
