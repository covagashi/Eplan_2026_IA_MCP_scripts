# FUNC_PLCCOMMUNICATIONENTITY_OBJECTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic630.html

---

Object ID of communication unit # 20098.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_OBJECTID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_OBJECTID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Unique identifier for data exchange / synchronization between Eplan Electric P8 and PLC configuration systems (max. 10 allowed). The object ID uniquely identifies communication units within P8.
