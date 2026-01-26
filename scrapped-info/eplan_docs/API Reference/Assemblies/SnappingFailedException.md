# SnappingFailedException

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException.html

---

Throw when snap operation has failed.

Inheritance Hierarchy

[System.Object](#)  
   [System.Exception](#)  
      [System.ApplicationException](#)  
         [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html)  
            [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html)  
               **Eplan.EplApi.DataModel.SnappingFailedException**

Syntax

**C#**



public class SnappingFailedException : DataModelException

public ref class SnappingFailedException : public DataModelException

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SnappingFailedException Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException~_ctor.html) | Overloaded. |



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


