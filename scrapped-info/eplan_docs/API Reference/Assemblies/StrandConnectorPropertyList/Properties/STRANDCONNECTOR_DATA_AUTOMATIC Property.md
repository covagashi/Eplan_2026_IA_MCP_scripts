# STRANDCONNECTOR_DATA_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandConnectorPropertyList~STRANDCONNECTOR_DATA_AUTOMATIC().html

---

Bundle: Connection point data # 19072.

Syntax

**C#**



public PropertyValue STRANDCONNECTOR_DATA_AUTOMATIC {get; set;}

public:

property PropertyValue^ STRANDCONNECTOR_DATA_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Contains either the bundle description or, if this is not present, the bundle connection point designation.
