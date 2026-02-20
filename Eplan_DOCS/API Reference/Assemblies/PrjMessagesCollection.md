# PrjMessagesCollection

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html

---

Collection of project messages of the last check run (See ribbon "Tools>Review>Check" or [!!OVERLOADED\_VerifyProject\_Eplan::EplApi::HEServices:](check.html) ).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.PrjMessagesCollection**

Syntax

**C#**



public class PrjMessagesCollection

public ref class PrjMessagesCollection


Remarks

Adding message to or removing messages from this collection, will update the messages visible in message management of EPLAN.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PrjMessagesCollection Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~_ctor(Project).html) | constructor. initializes the matching enumerator. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Count](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Count.html) | Gets the number of elements contained in the PrjMessagesCollection. |
| Public Property | [IsReadOnly](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~IsReadOnly.html) | Gets a value indicating whether the PrjMessagesCollection is read-only. |
| Public Property | [ReuseMessages](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~ReuseMessages.html) | Determines whether new message can be duplicated in collection. Default value is `true`. |
| Public Property | [ShowImmediately](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~ShowImmediately.html) | If true, added messages will be immediately displayed in message management window. Default value is false. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Add](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Add.html) | Adds an item to the `PrjMessagesCollection`. |
| Public Method | [AddMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~AddMessage.html) | Overloaded. Adds a new message associated with part number to the project's message management window. |
| Public Method | [Clear](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Clear.html) | Removes all items from the `PrjMessagesCollection`. |
| Public Method | [Contains](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Contains.html) | Determines whether the `PrjMessagesCollection` contains a specific value. |
| Public Method | [CopyTo](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~CopyTo.html) | Copies the elements of the `PrjMessagesCollection` to an Array, starting at a particular Array index. |
| Public Method | [GetEnumerator](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~GetEnumerator.html) | Returns an enumerator that can iterate through a collection. |
| Public Method | [GetEnumerator2](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~GetEnumerator2.html) | Returns an enumerator that can iterate through a collection. |
| Public Method | [GetPrjMsgEnumerator](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~GetPrjMsgEnumerator.html) | Returns a typed enumerator that can iterate through a collection. |
| Public Method | [Remove](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Remove.html) | Removes the first occurrence of a specific object from the `PrjMessagesCollection`. |


