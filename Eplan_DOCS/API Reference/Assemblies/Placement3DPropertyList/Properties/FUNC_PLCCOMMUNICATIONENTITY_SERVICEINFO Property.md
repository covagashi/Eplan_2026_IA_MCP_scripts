# FUNC_PLCCOMMUNICATIONENTITY_SERVICEINFO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic633.html

---

Service info (Interbus) # 20132.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_SERVICEINFO( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_SERVICEINFO {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. The service info can be set at bus nodes in Interbus systems. Using the index, you can differentiate between up to 10 info elements.
