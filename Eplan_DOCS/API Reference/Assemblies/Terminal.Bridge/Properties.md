# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge_properties.html

---

For a list of all members of this type, see [Terminal.Bridge members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsVertical](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~IsVertical.html) | Returns information whether the bridge is 'vertical', i.e. whether it connects only different levels of the same multi-level terminal. Note: this property is valid only if the bridge object has been obtained through the TerminalStrip.Bridges\_Split property of a terminal strip object. Otherwise, this property returns FALSE. |
| Public Property | [Kind](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Kind.html) | A [Terminal.Bridge.Kinds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge+Kinds.html) of the bridge (i.e. internal, external, small, saddleslot 3, saddleslot 4 or saddleslot 5). |
| Public Property | [Terminals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Terminals.html) | An array of all terminals that the bridge connects. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Type.html) | A type of the bridge. Corresponds to the function definition tag of the bridge's connections. |


