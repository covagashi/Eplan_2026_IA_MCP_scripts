# NameOfRecord Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~NameOfRecord.html

---

Gets/Sets the name of a record, specified by its index.

Syntax

**C#**



public virtual string NameOfRecord( 

   int nIndex

) {get; set;}

public:

virtual property String^ NameOfRecord {

   String^ get(int nIndex);

   void set (int nIndex, String^ value);

}


#### Parameters

*nIndex*
:   Index of the record. (zero based)

#### Property Value

Name of the record.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments, e.g. if the index does not exist. |
