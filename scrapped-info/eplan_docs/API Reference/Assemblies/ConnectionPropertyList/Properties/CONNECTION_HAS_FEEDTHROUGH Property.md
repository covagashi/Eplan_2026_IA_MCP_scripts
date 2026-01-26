# CONNECTION_HAS_FEEDTHROUGH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_HAS_FEEDTHROUGH().html

---

Mechanical feedthroughs available # 31165.

Syntax

**C#**



public PropertyValue CONNECTION_HAS_FEEDTHROUGH {get; set;}

public:

property PropertyValue^ CONNECTION_HAS_FEEDTHROUGH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Specifies whether the connection runs through a mechanical feedthrough. This property can be used as a filter criterion for connection lists.
