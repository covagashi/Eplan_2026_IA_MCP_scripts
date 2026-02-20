# SetStrings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetStrings.html

---

Sets the array filled with strings from the context. (Additional to the parameters)

Syntax

**C#**



public virtual void SetStrings( 

   string[] stringArray

)

public:

virtual void SetStrings( 

   array<String^>^ stringArray

)


#### Parameters

*stringArray*
:   the string array to set

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `stringArray` is `null`. |
