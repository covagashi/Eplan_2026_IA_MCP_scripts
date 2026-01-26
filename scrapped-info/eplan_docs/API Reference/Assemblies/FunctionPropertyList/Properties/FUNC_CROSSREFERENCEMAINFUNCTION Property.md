# FUNC_CROSSREFERENCEMAINFUNCTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CROSSREFERENCEMAINFUNCTION().html

---

Cross-reference display: Auxiliary function as main function # 20314.

Syntax

**C#**



public PropertyValue FUNC_CROSSREFERENCEMAINFUNCTION {get; set;}

public:

property PropertyValue^ FUNC_CROSSREFERENCEMAINFUNCTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated at an auxiliary function, it will behave, in terms of the cross-reference display, like a main function, and the main function of the same device will automatically behave like an auxiliary function. If a contact image is displayed at the main function, it is not carried over to the auxiliary function, but remains at the main function.

If the property is activated for several functions of a device, a possible main function "wins", otherwise the graphically first function.
