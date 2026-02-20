# FUNC_PLCCOMMUNICATIONENTITY_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCOMMUNICATIONENTITY_NAME(Int32).html

---

Communication unit (at communication units) # 20106.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Name of the communication unit. Using the index, you can differentiate between up to 10 communications units.
