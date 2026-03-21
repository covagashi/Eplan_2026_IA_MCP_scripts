# PropertiesAndHandleObjectPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList.html

---

Base class of all property list classes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList**  
      [Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList.html)  
      [Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList.html)  
      [Eplan.EplApi.MasterData.MDSymbolPropertyList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList.html)  
      [Eplan.EplApi.MasterData.MDSymbolVariantPropertyList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolVariantPropertyList.html)

Syntax

**C#**



[DefaultMember("Property")]

public class PropertiesAndHandleObjectPropertyList

[DefaultMember("Property")]

public ref class PropertiesAndHandleObjectPropertyList

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PropertiesAndHandleObjectPropertyList Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~_ctor().html) | This constructor creates local property list. Any changes done to this PropertiesAndHandleObjectPropertyList are local. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~ExistingIds.html) | Returns array of MDPropertyValue objects. If PropertiesAndHandleObjectPropertyList works on local property list it will be an array of unique properties from local property list. Otherwise it will be an array of all existing properties for related object. |
| Public Property | [Parent](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~Parent.html) | PropertiesAndHandleObject to which this property list is connected. |
| Public Property | [Property](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties by MDAnyPropertyId. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~Dispose().html) | Destructor for deterministic finalization of PropertiesAndHandleObjectPropertyList object. |
| Public Method | [Exists](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~Exists.html) | Checks if property exists for used object. |


