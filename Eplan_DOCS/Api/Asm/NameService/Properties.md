# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_properties.html

---

For a list of all members of this type, see [NameService members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdjustmentOfDeviceTagSeparatorIsEnabled](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustmentOfDeviceTagSeparatorIsEnabled.html) | Determines if adjustment of the visible device tag separator should be forced |
| Public Property | [Page](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~Page.html) | Gets/Sets the page. Page must be set, because most of the NameService class's methods work on page only (except for e.g. CorrectDeviceTagProperties, EvaluateAndSetAllNamesTXN methods). |
| Public Property | [RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled.html) | Determines if removal of unnecessary main and nested device tag in the visible name should be forced. The property is need to be set, if you have a function with a device tag in the visible name, you want to evaluate a new visible name and the device tag should be removed from the visible name if it matches the device tag of a surrounding device box or of a function laying in search direction (which normally is "left"). By default or if this parameter is set to false, the device tag is kept in the visible name even if it is not necessary. |
| Public Property | [RemovalOfUnnecessaryProjectStructuresIsEnabled](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~RemovalOfUnnecessaryProjectStructuresIsEnabled.html) | Determines if removal of unnecessary project structures in the visible device tag should be forced. This property is need to be set, if you have a function with a visible name that contains project structures, you want to evaluate a new visible name and the project structures should be removed from the visible name if they matches the project structures of a surrounding location box or the page. By default or if this parameter is set to false, the project structures are kept in the visible name even if they are not necessary. |


