# TERMINAL_COUNTOFINTERNALOBJECTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStripPropertyList~TERMINAL_COUNTOFINTERNALOBJECTS().html

---

Terminal strips: Total number of objects on terminal strip # 35001.

Syntax

**C#**



public PropertyValue TERMINAL_COUNTOFINTERNALOBJECTS {get; set;}

public:

property PropertyValue^ TERMINAL_COUNTOFINTERNALOBJECTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Quantity of all objects on the terminal strip, including the terminal strip definition, terminals, terminal accessories, and function templates.
