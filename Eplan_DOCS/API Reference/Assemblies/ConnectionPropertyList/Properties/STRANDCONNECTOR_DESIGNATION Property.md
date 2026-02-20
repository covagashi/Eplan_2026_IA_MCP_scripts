# STRANDCONNECTOR_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~STRANDCONNECTOR_DESIGNATION().html

---

Bundle: Connection point designation # 19070.

Syntax

**C#**



public PropertyValue STRANDCONNECTOR_DESIGNATION {get; set;}

public:

property PropertyValue^ STRANDCONNECTOR_DESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The bundle connection point designation identifies a connection within a bundle. It occurs in pairs (but not more often) for each bundle: At the connection point entering the bundle and at the connection point leaving the bundle. Several bundle connection point numbers can also be entered, separated by commas.
