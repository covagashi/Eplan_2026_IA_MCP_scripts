# Count Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection~Count.html

---

Gets the number of elements contained in the `SysMessagesCollection`.

Syntax

**C#**



public virtual int Count {get;}

public:

virtual property int Count {

   int get();

}


Remarks

Consecutive messages with the same text (i.e. error description) are joined into one item in the system's message tree. Therefore the count of messages in the collection may be different then the count of generated messages.
