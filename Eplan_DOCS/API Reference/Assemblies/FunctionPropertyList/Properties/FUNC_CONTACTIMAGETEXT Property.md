# FUNC_CONTACTIMAGETEXT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CONTACTIMAGETEXT().html

---

Revision: Contact image text (for property comparison) # 20199.

Syntax

**C#**



public PropertyValue FUNC_CONTACTIMAGETEXT {get; set;}

public:

property PropertyValue^ FUNC_CONTACTIMAGETEXT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property provides text information about a contact image. It can be used for property comparison of projects, to highlight changes to the contact image on the relevant coil and to show the result of the comparison. Changes are only specified if the content of the contact image changes, for example if a contact is deleted or added or moved to another schematic path. Changes to properties that are not visible in the contact image (e.g., technical characteristics) are not specified.
