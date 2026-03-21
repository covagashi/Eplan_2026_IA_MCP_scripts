# IExtendedProcessor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor.html

---

Interface for implementing an extended processor in connection with the IXMLProcessor.

Syntax

**C#**



public interface IExtendedProcessor : IInterface

public interface class IExtendedProcessor : public IInterface

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [InterfaceName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface~InterfaceName.html) | This name is used to register the type as an interface. (Inherited from [Eplan.EplApi.ApplicationFramework.IInterface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CanExportDirect](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~CanExportDirect.html) | Indicates whether the converter provides an export. |
| Method | [CanImportDirect](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~CanImportDirect.html) | Indicates whether the converter can import external formats |
| Method | [ExportDirect](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~ExportDirect.html) | Exports to a special file. All Parameter are in the context. |
| Method | [GetExtendedOptions](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~GetExtendedOptions.html) | Function for extended Options. Set the parameters in the context |
| Method | [ImportDirect](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~ImportDirect.html) | Imports the file to the system EContext may point to an EProgress object to support a progress bar. Returns true if successful. |


