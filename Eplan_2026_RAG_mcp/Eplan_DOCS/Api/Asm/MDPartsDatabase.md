# MDPartsDatabase

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase.html

---

This is the class that represents a parts database

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDPartsDatabase**

Syntax

**C#**



public class MDPartsDatabase

public ref class MDPartsDatabase


Remarks

It's possible to work on other parts database that configured in the EPLAN Settings

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDPartsDatabase Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~_ctor(String).html) | Opens parts database |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessoryLists](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AccessoryLists.html) | Gets all accessory lists that are stored in the parts database. They are sorted by it's name. |
| Public Property | [AccessoryPlacements](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AccessoryPlacements.html) | Gets all accessory lists that are stored in the parts database. They are sorted by it's name. |
| Public Property | [ConnectionPointInfos](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ConnectionPointInfos.html) | Gets all connection point infos that are stored in the parts database. |
| Public Property | [Constructions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Constructions.html) | Gets all constructions that are stored in the parts database. |
| Public Property | [Currency\_1](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Currency_1.html) | Get/Set article library currency 1 |
| Public Property | [Currency\_2](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Currency_2.html) | Get/Set article library currency 2 |
| Public Property | [Customers](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Customers.html) | Gets all customers that are stored in the parts database. |
| Public Property | [ID](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ID.html) | Get Database ID |
| Public Property | [IsOpen](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~IsOpen.html) | Returns true if a parts database is open. Instead of SQL Server returns true if connected. |
| Public Property | [IsReadOnly](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~IsReadOnly.html) | Returns true if the parts database is read only. That can be if the EPLAN database file has read only attribute set, or the SQL Server has write restrictions to the current user. |
| Public Property | [IsSchemeUpToDate](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~IsSchemeUpToDate.html) | Test, whether the scheme of the database is up to date. |
| Public Property | [Manufacturers](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Manufacturers.html) | Gets all customers that are stored in the parts database. |
| Public Property | [Name](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Name.html) | Get database Name |
| Public Property | [Parts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Parts.html) | Gets all parts that are stored in the parts database. |
| Public Property | [Type](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Type.html) | Returns the type of the database (SQL or EPLAN) |
| Public Property | [UserDefinedPropertyDefinitions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~UserDefinedPropertyDefinitions.html) | Returns user-defined property definitions array |
| Public Property | [Version](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Version.html) | Returns the parts database version |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddAccessoryList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddAccessoryList.html) | Adds a new accessory list to the parts database |
| Public Method | [AddAccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddAccessoryPlacement.html) | Adds a new accessory placement to the parts database |
| Public Method | [AddConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddConnectionPointInfo.html) | Adds a new connection point info to the parts data |
| Public Method | [AddConstruction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddConstruction.html) | Adds a new construction to the parts database |
| Public Method | [AddCustomer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddCustomer.html) | Adds a new customer to the parts database. |
| Public Method | [AddManufacturer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddManufacturer.html) | Adds a new manufacturer to the parts data |
| Public Method | [AddPart](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddPart.html) | Overloaded. Adds a new part into the parts database. |
| Public Method | [Close](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Close.html) | Closes the database |
| Public Method | [CreateFunctionTemplatesFromMacro](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~CreateFunctionTemplatesFromMacro.html) | Creates new function templates out of the macro that is referenced from all the parts in the parts database. |
| Public Method | [CreateTransaction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~CreateTransaction.html) | Creates a new database transaction. |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Dispose().html) | Destructor for deterministic finalization of MDPartsDatabase object. |
| Public Method | [ExistsConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExistsConnectionPointInfo.html) | Checks if a connection point info with the given name exists. |
| Public Method | [ExistsConstruction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExistsConstruction.html) | Checks if a construction with the given name exists. |
| Public Method | [ExistsCustomer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExistsCustomer.html) | Checks if a customer info with the given short name exists. |
| Public Method | [ExistsManufacturer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExistsManufacturer.html) | Checks if a manufacturer / supplier info with the given short name exists. |
| Public Method | [ExistsPart](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExistsPart.html) | Checks if a part with the given part number exists. |
| Public Method | [ExportMDUserDefinedPropertyDefinitions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportMDUserDefinedPropertyDefinitions.html) | Exports parts user defined properties. |
| Public Method | [ExportParts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportParts.html) | Overloaded. Exports specified parts from the system's parts database. |
| Public Method | [ExportPartsDatabaseItems](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportPartsDatabaseItems.html) | Overloaded. Exports specified parts and other specified parts management items such as addresses, constructions, terminals, accessory lists and accessory placements from the system's parts database. |
| Public Method | [ExportUntranslatableWords](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportUntranslatableWords.html) | Export all untranslatable words from article database to file. |
| Public Method | [GetAccessoryList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetAccessoryList.html) | Gets a accessory list with the given name that is stored in the parts database. |
| Public Method | [GetAccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetAccessoryPlacement.html) | Gets a accessory placement with the given name that is stored in the parts database. |
| Public Method | [GetConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetConnectionPointInfo.html) | Gets a connection point info with the given name that is stored in the parts database. |
| Public Method | [GetConstruction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetConstruction.html) | Gets a construction with the given name that is stored in the parts database. |
| Public Method | [GetCustomer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetCustomer.html) | Gets a customers that ist stored in the parts database. |
| Public Method | [GetManufacturer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetManufacturer.html) | Gets a manufacturer with the given name that is stored in the parts database. |
| Public Method | [GetPart](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPart.html) | Overloaded. Gets the part with the given part number. If there are several variants of that part, the first one is taken. First means, that if you sort that parts by their variant that the topmost variant is taken. |
| Public Method | [GetParts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetParts.html) | Overloaded. Gets filtered parts. When the filter is empty, than all parts are read. |
| Public Method | [GetPartsWithFilterScheme](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartsWithFilterScheme.html) | Gets parts using the filter from GUI. |
| Public Method | [GetPartVariants](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartVariants.html) | Gets all part variants with the given part number. |
| Public Method | [GetPartVariantsByERPNumber](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartVariantsByERPNumber.html) | Gets all part variants with the given ERP number. |
| Public Method | [ImportMDUserDefinedPropertyDefinitions](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ImportMDUserDefinedPropertyDefinitions.html) | Imports parts user defined properties. |
| Public Method | [ImportParts](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ImportParts.html) | Overloaded. Imports parts to this database. |
| Public Method | [ImportToDictionary](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ImportToDictionary.html) | Imports parts database translations to the system dictionary (MDTranslationDatabase) |
| Public Method | [RemoveAccessoryList](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveAccessoryList.html) | Removes a accessory list out of the parts datbase. |
| Public Method | [RemoveAccessoryPlacement](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveAccessoryPlacement.html) | Removes a accessory placement out of the parts datbase. |
| Public Method | [RemoveAllTranslations](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveAllTranslations.html) | Removes all the translations form parts database |
| Public Method | [RemoveConnectionPointInfo](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveConnectionPointInfo.html) | Removes a connection point info out of the parts database. |
| Public Method | [RemoveConstruction](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveConstruction.html) | Removes a construction out of the parts database. |
| Public Method | [RemoveCustomer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveCustomer.html) | Removes a customer out of the parts database. |
| Public Method | [RemoveManufacturer](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveManufacturer.html) | Removes a manufacturer out of the parts database. |
| Public Method | [RemovePart](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemovePart.html) | Removes the given part from the parts database. |
| Public Method | [RemoveTranslation](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~RemoveTranslation.html) | Removes translations form parts database |
| Public Method | [Translate](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Translate.html) | Translates all multilingual texts in an article database |
| Public Method | [UpdateScheme](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~UpdateScheme.html) | Updates the scheme of the database. |


