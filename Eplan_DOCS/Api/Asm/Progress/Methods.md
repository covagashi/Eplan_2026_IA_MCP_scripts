# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress_methods.html

---

For a list of all members of this type, see [Progress members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [BeginPart](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~BeginPart.html) | Starts a new segment. All parallel segments should result in a sum of 100%. |
| Public Method | [Canceled](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~Canceled.html) | Queries whether the operation was canceled. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~Dispose().html) | Destructor for deterministic finalization of Progress object. |
| Public Method | [EndPart](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~EndPart.html) | Overloaded. Ends segment and closes the window when it is not used. Don't forget to call it at the end, otherwise a progress dialog may lock P8. |
| Public Method | [GetProgress](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~GetProgress.html) | For internal use only. |
| Public Method | [SetActionText](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetActionText.html) | Sets a new action text. |
| Public Method | [SetAllowCancel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetAllowCancel.html) | Allows canceling. |
| Public Method | [SetAskOnCancel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetAskOnCancel.html) | Asks to confirm the cancel request. |
| Public Method | [SetNeededParts](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetNeededParts.html) | Specifies how many segments are required. |
| Public Method | [SetNeededSteps](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetNeededSteps.html) | Indicates how many steps are required to reach 100%. E.g. used for loops. |
| Public Method | [SetOverallActionText](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetOverallActionText.html) | Sets a new action text. |
| Public Method | [SetTitle](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetTitle.html) | Sets the title of the progress bar. |
| Public Method | [ShowImmediately](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~ShowImmediately.html) | Shows the progress bar without any further delay. When ShowImmediately isnt't called the dialog appears later (with delay), it prevents the dialog to show unnecessarily (to prevent that the progress flickers up for a short running actions). |
| Public Method | [ShowLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~ShowLevel.html) | Specifies the nesting level up to which a display is made. |
| Public Method | [Step](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~Step.html) | Uses a step |


