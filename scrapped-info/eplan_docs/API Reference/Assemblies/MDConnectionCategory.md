# MDConnectionCategory

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory.html

---

Represents connection category

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      **Eplan.EplApi.MasterData.MDConnectionCategory**

Syntax

**C#**



public struct MDConnectionCategory : System.ValueType

public value class MDConnectionCategory : public System.ValueType


Remarks

There are 2 kinds of connection categories:  
'¢ Build in, stored as strings in resources  
'¢ User-defined, stored internally as multi-langual strings in setting COMPANY.PartsManagementGui.TypeOfTerminal  
To access default connection category of a MDConnectionPointInfo, please use MDConnectionPointInfo.ConnectionCategoryDefault property To access connection category of a MDConnectionPointPosition, please use MDConnectionPointInfo.ConnectionCategory property

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDConnectionCategory Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~_ctor(Int32).html) | Initializes new connection category with internal number |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AsLong](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~AsLong.html) | Internal representation of connection category (as a long value) |
| Public Property | [AsMultiLangString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~AsMultiLangString.html) | Representation of connection category as a mult-lang string |
| Public Property | [AsString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~AsString.html) | Representation of connection category as a string |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~Create.html) | Overloaded. Creates new connection category at specific position |
| Public Methodstatic (Shared in Visual Basic) | [GetAll](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~GetAll.html) | Overloaded. Returns a list of possible categories of connections. |
| Public Method | [Remove](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~Remove.html) | Removes user-defined category |
| Public Method | [ToString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDConnectionCategory~ToString.html) | Returns a string that represents the current object. |


