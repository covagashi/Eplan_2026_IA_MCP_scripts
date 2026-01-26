# ReuseMessages Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~ReuseMessages.html

---

Determines whether new message can be duplicated in collection. Default value is `true`.

Syntax

**C#**



public bool ReuseMessages {get; set;}

public:

property bool ReuseMessages {

   bool get();

   void set (    bool value);

}


Remarks

If `true` and message of same id, region and assign objects exists in collection then no new message will be added to collection. If `false` new message is always added to collection.
