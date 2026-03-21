# Page Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~Page.html

---

Gets/Sets the page. Page must be set, because most of the NameService class's methods work on page only (except for e.g. CorrectDeviceTagProperties, EvaluateAndSetAllNamesTXN methods).

Syntax

**C#**



public Page Page {get; set;}

public:

property Page^ Page {

   Page^ get();

   void set (    Page^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
