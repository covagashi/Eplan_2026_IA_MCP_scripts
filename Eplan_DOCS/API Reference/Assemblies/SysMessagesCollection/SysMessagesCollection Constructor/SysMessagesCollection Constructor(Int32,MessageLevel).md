# SysMessagesCollection Constructor(Int32,MessageLevel)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~_ctor(Int32,MessageLevel).html

---

Constructor. The collection contains a section of the system message tree.

Syntax

**C#**



public SysMessagesCollection( 

   int nBookmarkID,

   MessageLevel nErrLevel

)

public:

SysMessagesCollection( 

   int nBookmarkID,

   MessageLevel nErrLevel

)


#### Parameters

*nBookmarkID*
:   only messages with this value or higher will be regarded; if nBookmark = 0 no filter for bookmarks is set

*nErrLevel*
:   only messages of this severity or higher will be analyzed; if nErrLevel = MessageLevel::Trace all messages will be received
