# RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled.html

---

Determines if removal of unnecessary main and nested device tag in the visible name should be forced. The property is need to be set, if you have a function with a device tag in the visible name, you want to evaluate a new visible name and the device tag should be removed from the visible name if it matches the device tag of a surrounding device box or of a function laying in search direction (which normally is "left"). By default or if this parameter is set to false, the device tag is kept in the visible name even if it is not necessary.

Syntax

**C#**



public bool RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled {get; set;}

public:

property bool RemovalOfUnnecessaryDeviceTagNamePartsIsEnabled {

   bool get();

   void set (    bool value);

}

