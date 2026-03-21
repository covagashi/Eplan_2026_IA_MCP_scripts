# PlcTracking Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~PlcTracking.html

---

Assigns a pin designation or index for PLC tracking.

Syntax

**C#**



public string PlcTracking {get; set;}

public:

property String^ PlcTracking {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [NoSuchPinException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NoSuchPinException.html) | Thrown when the pin of such index doesn't exist on the parent function . |
