# AUTOMATIONML_OBJECTID_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~AUTOMATIONML_OBJECTID_2(Int32).html

---

AutomationML GUID 2 # 25031.

Syntax

**C#**



public PropertyValue AUTOMATIONML_OBJECTID_2( 

   int index

) {get; set;}

public:

property PropertyValue^ AUTOMATIONML_OBJECTID_2 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 12.

The property manages a second GUID that is required during a PLC data exchange in AutomationML AR APC format. The GUID is generated automatically and should normally not be modified manually. Only the index [1] is used here. In this property the GUID of the symbolic address is stored at PLC connection points that are digital or analog inputs / outputs. At PLC boxes the GUID of the rack is stored in this property.
