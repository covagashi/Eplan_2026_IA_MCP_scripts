# PART_TERMINAL_TERMINALSIZE_DEFAULT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_TERMINALSIZE_DEFAULT().html

---

Connection dimension (default) # 22969.

Syntax

**C#**



public PropertyValue PART_TERMINAL_TERMINALSIZE_DEFAULT {get; set;}

public:

property PropertyValue^ PART_TERMINAL_TERMINALSIZE_DEFAULT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is used if no connection dimension has been entered for the individual connection point in the connection point pattern. A connection dimension can be specified in this property for bolt connections, flat plug-in connectors, band connections, rail connections, internal threads and external threads.

Example: For a terminal with the connection category "Bolt connection" you can specify the bolt diameter here, for example "3 mm". For a push-in fitting with the connection category "External thread" you can specify the connection thread here, for example "M3" or "G1/8".
