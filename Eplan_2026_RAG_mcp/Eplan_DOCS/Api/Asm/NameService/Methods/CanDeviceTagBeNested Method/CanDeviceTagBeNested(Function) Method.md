# CanDeviceTagBeNested(Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~CanDeviceTagBeNested(Function).html

---

Returns, if the device tag of a given function can be nested

Syntax

**C#**



public bool CanDeviceTagBeNested( 

   Function pFunction

)

public:

bool CanDeviceTagBeNested( 

   Function^ pFunction

)


#### Parameters

*pFunction*
:   Function for check.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
