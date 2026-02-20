# FUNC_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic589.html

---

Drive torque (specified), min. # 26573.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Required lowest drive torque to be applied to an item or system in order to perform the task.
