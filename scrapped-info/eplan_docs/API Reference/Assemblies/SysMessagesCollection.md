# SysMessagesCollection

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html

---

Class that represents the system-wide message tree. The collection contains the system messages as BaseException objects.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.SysMessagesCollection**

Syntax

**C#**



public class SysMessagesCollection

public ref class SysMessagesCollection


Remarks

It is called a message tree, because each message (BaseException) may contain a further inner exception. Only messages of type "Message", "Warning", "Error", and "Fatal Error" are listed. "Assert" and "Trace" are not added to the SysMessagesCollection. Normally Consecutive messages with the same text (i.e. error description) are joined into one item in the system's message tree. Therefore the count of messages in the collection may be different then the count of generated messages. The contents of the collection does not depend on the logging mode, which you can configure either by the "Diagnose dialog" in EPLAN or by the ELogFileConfigToolu.exe in the bin folder of the respective product variant. The logging mode only influences the EplLog.txt file. In advanced logging mode the EplLog.txt file also contains Asserts and Traces. If the logging is set to immediate mode, identical consecutive messages are not joined.

Example

Example of looping over the SysMessagesCollection For further examples, see also in SysMessagesEnumerator class.

**C#**

```
// check, whether errors occurred

int nBookmark = new Eplan.EplApi.Base.BaseException().GetBookmarkID();

Eplan.EplApi.Base.SysMessagesCollection colSysMsg = new Eplan.EplApi.Base.SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);

foreach(Eplan.EplApi.Base.BaseException osysMsg in colSysMsg)

{

	if (osysMsg != null)

	{

		Console.WriteLine("Fehler: " + osysMsg.ToString());

	}

}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SysMessagesCollection Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [BookmarkIDEnd](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~BookmarkIDEnd.html) |  |
| Public Property | [BookmarkIDStart](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~BookmarkIDStart.html) |  |
| Public Property | [Count](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~Count.html) | Gets the number of elements contained in the `SysMessagesCollection`. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [GetEnumerator](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~GetEnumerator.html) | Returns an enumerator that can iterate through a collection. |
| Public Method | [GetSysMsgEnumerator](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~GetSysMsgEnumerator.html) | Returns a typed enumerator that can iterate through a collection. |


