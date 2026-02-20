# PART_TERMINAL_TYPEDEFAULT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_TERMINAL_TYPEDEFAULT().html

---

Wire termination processing (Eplan Cabinet, default) # 22947.

Syntax

**C#**



public MDPropertyValue PART_TERMINAL_TYPEDEFAULT {get; set;}

public:

property MDPropertyValue^ PART_TERMINAL_TYPEDEFAULT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is only required for reasons of compatibility with Eplan Cabinet. It is used if no wire termination processing has been entered for the individual connection point in the connection point pattern. Shows how the end of the connection is handled, for example with stripping or crimping. Is entered in parts management for connection points and specifies the default value for a group of connection points.

0 = Undefined

1 = Cut

2 = Strip

3 = Crimp

4 = Other

from 5 = User-defined.
