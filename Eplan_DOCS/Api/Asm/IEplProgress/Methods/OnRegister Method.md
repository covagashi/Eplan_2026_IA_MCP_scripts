# OnRegister Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.IEplProgress~OnRegister.html

---

Register the progress

Syntax

**C#**



bool OnRegister( 

   ref string Name,

   ref int Ordinal,

   ref bool bNoMainFrame

)

bool OnRegister( 

   String^% Name,

   int% Ordinal,

   bool% bNoMainFrame

)


#### Parameters

*Name*
:   Name under which the action is registered in the system.

*Ordinal*
:   Overload level of progress

*bNoMainFrame*
:   Whether this progress needs a mainframe window.

#### Return Value

true: The return parameters are valid.
