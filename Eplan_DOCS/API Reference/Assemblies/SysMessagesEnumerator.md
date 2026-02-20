# SysMessagesEnumerator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator.html

---

supports a simple iteration over [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.SysMessagesEnumerator**

Syntax

**C#**



public class SysMessagesEnumerator

public ref class SysMessagesEnumerator


Example

iterate over the complete system message tree get all errors and fatal errors of the system message tree since nBookmark was set; how to get a bookmark see [BaseException.GetBookmarkID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetBookmarkID.html)

**C#**

```
SysMessagesCollection colSysMsg = new SysMessagesCollection();

SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();

int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 

{

BaseException osysMsg = itSysMsg.Current as BaseException;

if (osysMsg != null)

{

	nNr++;

}					

} while(itSysMsg.MoveNext());
```

**C#**

```
SysMessagesCollection colSysMsg = new SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);

SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();

int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 

{

BaseException osysMsg = itSysMsg.Current as BaseException;

if (osysMsg != null)

{

	nNr++;

}					

} while(itSysMsg.MoveNext());
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SysMessagesEnumerator Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Current](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Current.html) | gets the current element in [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Dispose().html) |  |
| Public Method | [GetCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~GetCount.html) |  |
| Public Method | [MoveNext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~MoveNext.html) | Advances the enumerator to the next element of [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |
| Public Method | [Reset](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator~Reset.html) | Sets the enumerator to its initial position, which is before the first element in [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |


