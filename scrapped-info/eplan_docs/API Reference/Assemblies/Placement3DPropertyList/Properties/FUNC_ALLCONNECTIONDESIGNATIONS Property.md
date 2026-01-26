# FUNC_ALLCONNECTIONDESIGNATIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ALLCONNECTIONDESIGNATIONS().html

---

Connection point designations (all) # 20038.

Syntax

**C#**



public PropertyValue FUNC_ALLCONNECTIONDESIGNATIONS {get; set;}

public:

property PropertyValue^ FUNC_ALLCONNECTIONDESIGNATIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Contains all connection point designations of a function. During entering (in the property dialog or for tabular editing) the individual values are separated by paragraph marks. For the display the values are separated by semicolons.

When setting the property an exception is thrown, if no value of the semicolon separated string is saved. This means the object has connection points (Pins) or the string is empty.
