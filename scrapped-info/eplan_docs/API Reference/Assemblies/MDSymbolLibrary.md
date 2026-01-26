# MDSymbolLibrary

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary.html

---

This class is a interface to manage symbols libraries

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)  
      **Eplan.EplApi.MasterData.MDSymbolLibrary**

Syntax

**C#**



[DefaultMember("Symbol")]

public class MDSymbolLibrary : PropertiesAndHandleObject

[DefaultMember("Symbol")]

public ref class MDSymbolLibrary : public PropertiesAndHandleObject


Remarks

Object becomes invalid when a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) is open and closed.

Example

It is possible to get MDSymbol object from MDSymbolLibrary, by indexer :

**C#**

```
MDSymbolLibrary lib = ....

MDSymbol smbl = lib["XEDU"];
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Properties](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Properties.html) | .NET Property enabling access to P8 properties of the MDSymbolLibrary object. |
| Public Property | [Symbol](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Symbol.html) | Index operator to get a symbol by its name. |
| Public Property | [Symbols](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Symbols.html) | Gets a read only list of all Symbols in the library |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddSymbol](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~AddSymbol.html) | Creates a new symbol with a unique Id and a unique strName. |
| Public Method | [Close](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Close.html) | Closes (and saves) the symbol library. |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Create.html) | Creates a new SymbolLibrary |
| Public Method | [Dispose()](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject~Dispose().html) | Destructor for deterministic finalization of MDSymbolLibrary object. (Inherited from [Eplan.EplApi.MasterData.PropertiesAndHandleObject](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObject.html)) |
| Public Method | [GetSymbol](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~GetSymbol.html) | Gets a Symbol object out of the library. |
| Public Methodstatic (Shared in Visual Basic) | [Open](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Open.html) | Overloaded. Opens an existing symbol library. |
| Public Method | [Remove](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Remove.html) | Removes the symbol library. |


