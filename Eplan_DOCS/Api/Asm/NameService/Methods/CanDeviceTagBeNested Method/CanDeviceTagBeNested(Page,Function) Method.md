# CanDeviceTagBeNested(Page,Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~CanDeviceTagBeNested(Page,Function).html

---

Sets the page and returns, if the device tag of a given function can be nested

Syntax

**C#**



public bool CanDeviceTagBeNested( 

   Page pPage,

   Function pFunction

)

public:

bool CanDeviceTagBeNested( 

   Page^ pPage,

   Function^ pFunction

)


#### Parameters

*pPage*
:   Page to set.

*pFunction*
:   Function for check.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
