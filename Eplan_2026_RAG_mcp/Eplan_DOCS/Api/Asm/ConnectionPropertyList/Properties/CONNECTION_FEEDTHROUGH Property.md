# CONNECTION_FEEDTHROUGH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FEEDTHROUGH().html

---

Routed mechanical feedthroughs # 31164.

Syntax

**C#**



public PropertyValue CONNECTION_FEEDTHROUGH {get; set;}

public:

property PropertyValue^ CONNECTION_FEEDTHROUGH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the DT of the device through which the connection runs as a mechanical feedthrough. This property can be used in reports. If the connection runs through several devices, the individual DTs are output semicolon-separated and alphanumerically sorted.
