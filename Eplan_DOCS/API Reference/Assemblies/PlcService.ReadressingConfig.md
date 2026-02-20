# PlcService.ReadressingConfig

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig.html

---

Used as a container for PLC re-addressing settings.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.PlcService.ReadressingConfig**

Syntax

**C#**



public class PlcService.ReadressingConfig

public ref class PlcService.ReadressingConfig

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PlcService.ReadressingConfig Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AnalogStartAddress](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~AnalogStartAddress.html) | Start address value to use for analog addresses. If empty, a default value will be used. |
| Public Property | [ChangeAnalog](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~ChangeAnalog.html) | If true, analog addresses will be changed. |
| Public Property | [ChangeDigital](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~ChangeDigital.html) | If true, digital addresses will be changed. |
| Public Property | [ConfigurationProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~ConfigurationProject.html) | Gets/Sets ... |
| Public Property | [CpuName](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~CpuName.html) | Gets/Sets ... |
| Public Property | [DigitalStartAddress](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~DigitalStartAddress.html) | Start address value to use for digital addresses. If empty, a default value will be used. |
| Public Property | [OnlySelectedTerminals](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~OnlySelectedTerminals.html) | Gets/Sets if the re-addressing process affects all PLC terminals in the project or just the selected ones. |
| Public Property | [SortModeIndex](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~SortModeIndex.html) | Gets/Sets a sort mode that should be used during re-addressing. Should be in range from 0 (default) to the value returned by SortModesCount property -1. |
| Public Property | [Station](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~Station.html) | Gets/Sets ... |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Methodstatic (Shared in Visual Basic) | [GetSortModesCount](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ReadressingConfig~GetSortModesCount.html) | Returns a number of valid sort modes. |


