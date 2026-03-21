# MDInvalidHandleException

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidHandleException.html

---

Throw when internally used handle is not valid. May occur if the user has several objects pointing to the same place in project, and on one of them calls for example ::Delete or ::Remove, In such situation , properties returned by another objects will throw InvalidHandleException.

Inheritance Hierarchy

[System.Object](#)  
   [System.Exception](#)  
      [System.SystemException](#)  
         [System.ArgumentException](#)  
            [Eplan.EplApi.MasterData.MDInvalidArgumentException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidArgumentException.html)  
               **Eplan.EplApi.MasterData.MDInvalidHandleException**

Syntax

**C#**



public class MDInvalidHandleException : MDInvalidArgumentException

public ref class MDInvalidHandleException : public MDInvalidArgumentException

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDInvalidHandleException Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidHandleException~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Data](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HelpLink](#) | (Inherited from [System.Exception](#)) |
| Public Property | [HResult](#) | (Inherited from [System.Exception](#)) |
| Public Property | [InnerException](#) | (Inherited from [System.Exception](#)) |
| Public Property | [Message](#) | (Inherited from [System.ArgumentException](#)) |
| Public Property | [ParamName](#) | (Inherited from [System.ArgumentException](#)) |
| Public Property | [Source](#) | (Inherited from [System.Exception](#)) |
| Public Property | [StackTrace](#) | (Inherited from [System.Exception](#)) |
| Public Property | [TargetSite](#) | (Inherited from [System.Exception](#)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [GetBaseException](#) | (Inherited from [System.Exception](#)) |
| Public Method | [GetObjectData](#) | (Inherited from [System.ArgumentException](#)) |
| Public Method | [GetType](#) | (Inherited from [System.Exception](#)) |
| Public Method | [ToString](#) | (Inherited from [System.Exception](#)) |


