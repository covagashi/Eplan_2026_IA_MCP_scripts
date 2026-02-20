# FilterScheme Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ElectroMessage~FilterScheme.html

---

Gets/sets filter scheme on a template of project message.

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
| **BaseException** | Thrown by setter when ElectroMessage wasn't created in the context of a project, project is invalid or template of project message is visible with "No filter" filter in GUI. |
| **InvalidArgumentException** | Thrown by setter when parameter sFilterSchemeName is empty or null. |

Remarks

Using this property requires ElectroMessage to be created in the context of a Project. In order to do this PrjMessagesRegisteredCollection have to be created with oProject parameter. Property returns empty string when ElectroMessage was not created in the context of a Project or template of project message is visible with "No filter" filter in GUI.
