# FORM_BEHAVIOUR_PROPERTY_VAL_GRAPHIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic737.html

---

Assignment: Property / value to graphic # 13026.

Syntax

**C#**



public PropertyValue FORM_BEHAVIOUR_PROPERTY_VAL_GRAPHIC( 

   int index

) {get; set;}

public:

property PropertyValue^ FORM_BEHAVIOUR_PROPERTY_VAL_GRAPHIC {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

Assignment of a property and / or a value to a symbol variant. This property contains the assignment table assigning a graphic to the property and / or the value. A max. of 10 assignments allowed.
