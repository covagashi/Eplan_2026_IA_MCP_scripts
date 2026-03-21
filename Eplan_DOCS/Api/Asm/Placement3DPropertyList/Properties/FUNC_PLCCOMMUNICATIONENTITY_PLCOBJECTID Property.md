# FUNC_PLCCOMMUNICATIONENTITY_PLCOBJECTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic632.html

---

PLC object ID (at communication units) # 20139.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_PLCOBJECTID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_PLCOBJECTID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Unique identifier for data exchange / synchronization between Eplan Electric P8 and PLC configuration systems. The object ID uniquely identifies objects of this configuration system. Using the index, you can differentiate between up to 10 identifiers.
