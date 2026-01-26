# GetBookmarkID Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~GetBookmarkID.html

---

Sets a label in the system error message management for getting a section of the 'message tree'

Syntax

**C#**



public int GetBookmarkID()

public:

int GetBookmarkID();


#### Return Value

a serial number. save this value for later use

Example

get all messages which have been declared since the given bookmark was set

**C#**

```
int nBookmark = new Eplan.EplApi.Base.BaseException().GetBookmarkID(); //Starting point which sets the new bookmark

...

BaseException oBaseException = new BaseException("Exception message", MessageLevel.Error);

oBaseException.FixMessage(); //This error will be saved under nBookmark

SysMessagesCollection colSysMsg = new SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);

SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
```
