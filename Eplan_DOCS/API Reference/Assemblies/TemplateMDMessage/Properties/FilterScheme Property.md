# FilterScheme Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.TemplateMDMessage~FilterScheme.html

---

Gets/sets filter scheme on a template of Parts Database message.

Syntax

**C#**



public string FilterScheme {get; set;}

public:

property String^ FilterScheme {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown by setter when TemplateMDMessage wasn't created in the context of a Parts database, Parts database is invalid or template of Parts database message is visible with "No filter" filter in GUI. |
| **InvalidArgumentException** | Thrown by setter when parameter sFilterSchemeName is empty or null. |

Remarks

Using this property requires TemplateMDMessage to be created in the context of a Parts database. In order to do this MDPartsMessagesRegisteredCollection have to be created with oMDPartsdb parameter. Property returns empty string when TemplateMDMessage was not created in the context of a Parts Database or template of Parts Database message is visible with "No filter" filter in GUI.
