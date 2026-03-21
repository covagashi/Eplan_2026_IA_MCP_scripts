# Item Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProjectsCollection~Item.html

---

Gets the element at the specified index.

Syntax

**C#**



public SubProject this[ 

   int index

]; {get;}

public:

property SubProject^ default [int] {

   SubProject^ get(int index);

}


#### Parameters

*index*

Exceptions

| Exception | Description |
| --- | --- |
| [System.IndexOutOfRangeException](#) | The exception that is thrown when an attempt is made to access an element of an array with an index that is outside the bounds of the array. |
