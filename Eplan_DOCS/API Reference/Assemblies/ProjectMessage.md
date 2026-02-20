# ProjectMessage

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage.html

---

Base class for project messages.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.EServices.BaseProjectMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage.html)  
      **Eplan.EplApi.EServices.ProjectMessage**

Syntax

**C#**



public class ProjectMessage : BaseProjectMessage

public ref class ProjectMessage : public BaseProjectMessage


Remarks

To get [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) or [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) associated with this message, it is necessary to get first associated object and gain needed information from it.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectMessage Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~_ctor(ProjectMessageHandle).html) |  |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CreationType](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~CreationType.html) | Shows the method by which the message was created. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage~Dispose().html) | destructor (Inherited from [Eplan.EplApi.EServices.BaseProjectMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage.html)) |
| Public Method | [Equals](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage~Equals.html) | Determines whether the specified `BaseProjectMessage` is equal to the current `BaseProjectMessage`. (Inherited from [Eplan.EplApi.EServices.BaseProjectMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage.html)) |
| Public Method | [GetAdditionalInfo](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetAdditionalInfo.html) | Overridden. Returns an additional text if any |
| Public Method | [GetCategory](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetCategory.html) | Returns the error level of the message. |
| Public Method | [GetDone](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetDone.html) | checks if message has been marked as solved |
| Public Method | [GetEplanVersion](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetEplanVersion.html) | Returns the creation version of the message |
| Public Method | [GetErrorTextParameter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetErrorTextParameter.html) | Overridden. The replacement text for this message. |
| Public Method | [GetGroup](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetGroup.html) | Overridden. Returns the region associated with the message. |
| Public Method | [GetId](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetId.html) | Overridden. Returns the Id of the message. |
| Public Method | [GetObject1](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetObject1.html) | Overridden. Returns the first object associated to the message if any |
| Public Method | [GetObject2](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetObject2.html) | Overridden. Returns the second object associated to the message if any |
| Public Method | [GetPartNumber](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetPartNumber.html) | Overridden. Returns the part number associated to the message if any. |
| Public Method | [GetPartVariant](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetPartVariant.html) | Overridden. Returns the part variant associated to the message if any. |
| Public Method | [GetText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetText.html) | Returns the the complete text of the message. Parameters has been substituted. |
| Public Method | [GetTime](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetTime.html) | Returns the creation time of the message |
| Public Method | [GetUser](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~GetUser.html) | Returns the computer name of the user, who has been created the message |
| Public Method | [SetDone](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.ProjectMessage~SetDone.html) | Marks message as solved or not. |


