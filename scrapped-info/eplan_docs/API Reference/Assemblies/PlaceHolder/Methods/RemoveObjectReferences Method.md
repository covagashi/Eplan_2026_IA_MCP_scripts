# RemoveObjectReferences Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~RemoveObjectReferences.html

---

Removes object references from a PlaceHolder.

Syntax

**C#**



public virtual void RemoveObjectReferences( 

   StorableObject[] pObjects

)

public:

virtual void RemoveObjectReferences( 

   array<StorableObject^>^ pObjects

)


#### Parameters

*pObjects*
:   List of objects, of which the references will be removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |
