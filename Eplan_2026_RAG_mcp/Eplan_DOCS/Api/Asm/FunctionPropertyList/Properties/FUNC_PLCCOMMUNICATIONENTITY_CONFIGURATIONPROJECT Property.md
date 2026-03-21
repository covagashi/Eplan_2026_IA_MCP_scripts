# FUNC_PLCCOMMUNICATIONENTITY_CONFIGURATIONPROJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic257.html

---

Configuration project (at communication units) # 20107.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_CONFIGURATIONPROJECT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_CONFIGURATIONPROJECT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Main group orientation element of bus data. All objects to which the same configuration project is assigned belong together and represent the PLC configuration. Using the index, you can differentiate between up to 10 configuration projects.
