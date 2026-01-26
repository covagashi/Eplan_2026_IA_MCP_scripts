# SortTerminalStrips Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~SortTerminalStrips.html

---

Sorts terminal strips with one of the following sort methods specified by sortKind parameter: - Default, - Numeric, - AlphaNumeric, - Position, - ExtCable, - Bridges, - WriteSortIdToAll

Syntax

**C#**



public void SortTerminalStrips( 

   TerminalStrip[] arrTerminalStrips,

   DeviceService.TerminalStripSortMethods sortKind

)

public:

void SortTerminalStrips( 

   array<TerminalStrip^>^ arrTerminalStrips,

   DeviceService.TerminalStripSortMethods sortKind

)


#### Parameters

*arrTerminalStrips*
:   Array of terminal strips to sort.

*sortKind*
:   Specifies sort method.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | NULL was passed as a parameter. |
| **ArgumentException** | Invalid parameter passed. |
| **ApplicationException** | The internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while performing the action. Please refer to the exception message. |
