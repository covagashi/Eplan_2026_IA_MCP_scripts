# SysMessagesCollection Constructor(Int32,Int32,MessageLevel)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~_ctor(Int32,Int32,MessageLevel).html

---

Constructor. The collection contains a section of the system message tree.

Syntax

**C#**



public SysMessagesCollection( 

   int nBookmarkIDStart,

   int nBookmarkIDEnd,

   MessageLevel nErrLevel

)

public:

SysMessagesCollection( 

   int nBookmarkIDStart,

   int nBookmarkIDEnd,

   MessageLevel nErrLevel

)


#### Parameters

*nBookmarkIDStart*
:   only messages starting from this value will be regarded;

*nBookmarkIDEnd*
:   the endpoint to which messages will be taken;

*nErrLevel*
:   only messages of this severity or higher will be analyzed; if nErrLevel = MessageLevel::Trace all messages will be received
