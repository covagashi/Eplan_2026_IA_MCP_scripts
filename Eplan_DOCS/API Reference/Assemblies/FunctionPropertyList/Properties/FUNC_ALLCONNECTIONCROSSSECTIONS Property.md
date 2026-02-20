# FUNC_ALLCONNECTIONCROSSSECTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ALLCONNECTIONCROSSSECTIONS().html

---

Connection point cross-section / diameter (all) # 20296.

Syntax

**C#**



public PropertyValue FUNC_ALLCONNECTIONCROSSSECTIONS {get; set;}

public:

property PropertyValue^ FUNC_ALLCONNECTIONCROSSSECTIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property contains all connection point cross-sections / diameters of a function. During entering (in the property dialog or for tabular editing) the individual values are separated by paragraph marks. For the display the values are separated by semicolons.

When setting the property an exception is thrown, if no value of the semicolon separated string is saved. This means the object has connection points (Pins) or the string is empty.
