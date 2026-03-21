# FUNCTION3D_TERMINALPOSITION_TERMINALSIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic694.html

---

Connection point pattern: Connection dimension # 36067.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_TERMINALSIZE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TERMINALSIZE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

A connection dimension can be specified in this property for bolt connections, flat plug-in connectors, band connections, rail connections, internal threads and external threads.

Example: For a terminal with the connection category "Bolt connection" you can specify the bolt diameter here, for example "3 mm". For a push-in fitting with the connection category "External thread" you can specify the connection thread here, for example "M3" or "G1/8".
