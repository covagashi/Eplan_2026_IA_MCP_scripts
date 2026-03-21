# AddToSearchDB(StorableObject) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~AddToSearchDB(StorableObject).html

---

FÃ¼gt ein Objekt der Suchdatenbank hinzu. Es wird die aus den Einstellungen gesetzte Suchdatenbank verwendet.

Syntax

**C#**



public void AddToSearchDB( 

   StorableObject pObject

)

public:

void AddToSearchDB( 

   StorableObject^ pObject

)


#### Parameters

*pObject*

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Wenn Argumente nicht Ã¼bergeben wurden. |
| **ArgumentException** | Wenn Argumente nicht gÃ¼ltig. Zum Beispiel wenn das angegebene Projekt nicht existiert bzw. nicht gÃ¼ltig ist. |
| **ApplicationException** | Die Schnittstelle fÃ¼r die Suche kann nicht erzeugt werden. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Suche konnte nicht korrekt durchgefÃ¼hrt werden. |
