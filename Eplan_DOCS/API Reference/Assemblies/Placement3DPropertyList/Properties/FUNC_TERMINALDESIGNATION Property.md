# FUNC_TERMINALDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINALDESIGNATION(Int32).html

---

Connection point designation # 20028.

Syntax

**C#**



public PropertyValue FUNC_TERMINALDESIGNATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_TERMINALDESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Shows the connection point designations of a connection point. A maximum of 100 connection point designations can be defined by using the index.
