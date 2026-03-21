# MACROBOX_USECONNECTIONPOINTDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBoxPropertyList~MACROBOX_USECONNECTIONPOINTDESIGNATION().html

---

Macro: Take connection point designations into account # 23014.

Syntax

**C#**



public PropertyValue MACROBOX_USECONNECTIONPOINTDESIGNATION {get; set;}

public:

property PropertyValue^ MACROBOX_USECONNECTIONPOINTDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies for the macro, whether connection point designations are taken into account for device assignment when macros are updated.

0 = From user settings: The connection point designations are taken into account during the device assignment, if the user setting "Take the connection point designations into account during the device assignment" is activated.

1 = Yes: The connection point designations are always taken into account.

2 = No: The connection point designations are never taken into account.
