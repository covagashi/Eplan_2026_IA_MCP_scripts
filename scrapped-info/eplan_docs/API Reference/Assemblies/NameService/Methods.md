# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_methods.html

---

For a list of all members of this type, see [NameService members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AdjustFullName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustFullName.html) | Overloaded. Sets the page and evaluates for a given functionbase the full name from the visible name of the functionbase and sets that evaluated value at the functionbase-object |
| Public Method | [AdjustVisibleName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustVisibleName.html) | Overloaded. Sets the page and evaluates for a given functionbase the visible name and visible name format from the fullname of the functionbase and sets these evaluated values at the functionbase-object |
| Public Method | [CanDeviceTagBeNested](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~CanDeviceTagBeNested.html) | Overloaded. Sets the page and returns, if the device tag of a given function can be nested |
| Public Method | [CorrectDeviceTagProperties](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~CorrectDeviceTagProperties.html) | Do a correction on the namelist, if properties for main and nested devicetags are incorrect. In detail the nested devicetags are moved to the main devicetags if these have been empty. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~Dispose().html) | Destructor |
| Public Method | [EvaluateAndSetAllNames](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllNames.html) | Overloaded. Sets the page and evaluates the full name for all placed functions and interruption points on page by calling EvaluateName for all those objects. |
| Public Method | [EvaluateAndSetAllNamesTXN](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllNamesTXN.html) | Evaluate all names for all FunctionBase objects in the project by calling EvaluateName for all those objects. This methods does own transactions, so no transactions around the method are allowed. |
| Public Method | [EvaluateAndSetAllVisibleNames](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateAndSetAllVisibleNames.html) | Overloaded. Sets the page and evaluate the visible names from the full names for all placed functions and interruption points on page. |
| Public Method | [EvaluateName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~EvaluateName.html) | Overloaded. Sets the page and evaluates the full name for a FunctionBase (which is either a Function or a Location box or an Interruption-point) by using the visible device tag of that FunctionBase and building the full name by graphical search on the page where the FunctionBase is placed. In the visible name missing project structures, which for example are supplemented from surrounding LocationBoxes or from the Page-Object itself. For an empty visible name the full name is taken from a function in search direction or from a surrounding device box. Nesting of device tags is made by using an surrounding device box, if nesting is enabled. The parameters used for evaluation are defined in the dialog with the project properties. |
| Public Method | [FindNameGivingFunction](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingFunction.html) | Overloaded. Sets the page and finds the function, that would give hActual the function name, if hActual has no instance name parts (has no visible device tag). Returns NULL, if no such function exists or hActual don't take over a name. |
| Public Method | [FindNameGivingObject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingObject.html) | Overloaded. Finds an object, that would give the f function its name, if f has no its instance name parts assigned (has no visible device tag). Returns NULL, if no such object exists or f don't take over a name. |
| Public Method | [GetSortedListOfLogicals](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~GetSortedListOfLogicals.html) | Overloaded. Sets the page and returns a sorted list of logicals (that is everything derived from functionbase). The logicals are sorted in that way, so that objects which are dependent on the name of other logicals are sorted behind them. |
| Public Method | [RenameDevice](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~RenameDevice.html) | Overloaded. Rename all functions of device. |
| Public Method | [SetFullNameAndAdjustVisibleName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~SetFullNameAndAdjustVisibleName.html) | Overloaded. Sets the page and sets the given full name as the new full name to the given function and adjusts the visible name of that function. Returns false, if a problem occured (if a visible name cannot be evaluated) - no changes to the function-object have been made then. |
| Public Method | [SetName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~SetName.html) | Sets a default device tag to the function. (I.e. a device tag which is automatically assigned when manually inserting a symbol on a page) |
| Public Method | [SetVisibleNameAndAdjustFullName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~SetVisibleNameAndAdjustFullName.html) | Overloaded. Sets the page and sets the given visible name as the new visible name to the given function and adjusts the full name of that function accordingly (by calling "EvaluateName"). |
| Public Method | [UpdateConnectionDefinitionPointsParent](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~UpdateConnectionDefinitionPointsParent.html) | Overloaded. Sets the page and updates the graphical parent of a connection definition point |


