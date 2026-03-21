# ContactImageType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ContactImageType.html

---

Gets or sets a value indicating where contact image is displayed for this function.

Syntax

**C#**



public ContactImage.Enums.ContactImageType ContactImageType {get; set;}

public:

property ContactImage.Enums.ContactImageType ContactImageType {

   ContactImage.Enums.ContactImageType get();

   void set (    ContactImage.Enums.ContactImageType value);

}


Remarks

If `None` value is assigned then contact image object is deleted with all its settings.
