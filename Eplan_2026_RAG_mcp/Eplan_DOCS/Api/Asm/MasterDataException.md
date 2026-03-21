# MasterDataException

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MasterDataException.html

---

Base class for exceptions thrown from MasterData.

Inheritance Hierarchy

[System.Object](#)  
   [System.Exception](#)  
      [System.ApplicationException](#)  
         [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)  
            **Eplan.EplApi.MasterData.MasterDataException**  
               [Eplan.EplApi.MasterData.MDCanNotAddSymbolPosition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDCanNotAddSymbolPosition.html)  
               [Eplan.EplApi.MasterData.MDDatabaseConnectionException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDDatabaseConnectionException.html)  
               [Eplan.EplApi.MasterData.MDDatabaseReadOnlyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDDatabaseReadOnlyException.html)  
               [Eplan.EplApi.MasterData.MDEmptyPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDEmptyPropertyException.html)  
               [Eplan.EplApi.MasterData.MDIncorrectNameFormatException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDIncorrectNameFormatException.html)  
               [Eplan.EplApi.MasterData.MDIndexedPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDIndexedPropertyException.html)  
               [Eplan.EplApi.MasterData.MDNotIndexedPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDNotIndexedPropertyException.html)  
               [Eplan.EplApi.MasterData.MDObjectCreationException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectCreationException.html)  
               [Eplan.EplApi.MasterData.MDPropertyAlreadyExistsException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyAlreadyExistsException.html)  
               [Eplan.EplApi.MasterData.MDSettingValueFailedException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSettingValueFailedException.html)

Syntax

**C#**



public class MasterDataException : Eplan.EplApi.Base.BaseException

public ref class MasterDataException : public Eplan.EplApi.Base.BaseException

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MasterDataException Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MasterDataException~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Data](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HelpLink](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HResult](#) | (Inherited from [System.Exception](#)) |
| Public Property | [InnerException](#) | (Inherited from [System.Exception](#)) |
| Public Property | [Message](#) | (Inherited from [System.Exception](#)) |
| Public Property | [MessageLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~MessageLevel.html) | Returns the level of message as [Eplan.EplApi.Base.MessageLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MessageLevel.html). (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Property | [NumberOfOccurrences](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~NumberOfOccurrences.html) | Returns number of repetitions of consecutive messages with the same text (i.e. error description) which are joined into one item in the system's message tree. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Property | [Source](#) | (Inherited from [System.Exception](#)) |
| Public Property | [StackTrace](#) | (Inherited from [System.Exception](#)) |
| Public Property | [TargetSite](#) | (Inherited from [System.Exception](#)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~Dispose().html) | Destructor for deterministic finalization of BaseException object. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [FixMessage](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~FixMessage.html) | Method enters a message in the system-wide message tree. (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetBaseException](#) | (Inherited from [System.Exception](#)) |
| Public Method | [GetBookmarkID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetBookmarkID.html) | Sets a label in the system error message management for getting a section of the 'message tree' (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetMessageIndex](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetMessageIndex.html) | returns the identifying S- number of a system message (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetMessageText](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetMessageText.html) | Returns the text of the system message without the index (Inherited from [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)) |
| Public Method | [GetObjectData](#) | (Inherited from [System.Exception](#)) |
| Public Method | [GetType](#) | (Inherited from [System.Exception](#)) |
| Public Method | [ToString](#) | (Inherited from [System.Exception](#)) |


