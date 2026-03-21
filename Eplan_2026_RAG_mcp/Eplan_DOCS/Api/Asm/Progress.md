# Progress

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress.html

---

This class enables you to access the functions of the progress bar in EPLAN.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Progress**

Syntax

**C#**



public class Progress

public ref class Progress


Remarks

There are different kinds of progress bars. It can be created by functions and passed to another function as a parameter object (often in a Context). Please call Progress::EndPart(true) at the end to close the dialog. Please don't use steps (SetNeededSteps and Step methods) when a nested EPLAN progress (i.e. from API method) could be called afterwards.

Example

Example of using Progress class

**C#**

```


using (var progress = new Progress("SimpleProgress"))

{

    progress.ShowImmediately();

    //part 1

   progress.BeginPart(25.0, "");

   progress.SetActionText("part1");

   progress.SetNeededSteps(1);

   progress.Step(1);

   System.Threading.Thread.Sleep(2500);    // TODO: Some processing

   progress.EndPart(false);

   //part 2

   progress.BeginPart(30.0, "");

   progress.SetNeededSteps(3);            // call SetNeededSteps with the count of steps following

   progress.SetActionText("part2 step1");

   progress.Step(1);

   System.Threading.Thread.Sleep(1000);    // TODO: Some processing

   progress.SetActionText("part2 step2");

   progress.Step(1);

   System.Threading.Thread.Sleep(1000);    // TODO: Some processing

   progress.SetActionText("part2 step3");

   progress.Step(1);

   System.Threading.Thread.Sleep(1000);    // TODO: Some processing

   progress.EndPart(false);

   //part 3

   progress.BeginPart(45.0, "");          // Here is a sum of 100% reached!

   progress.SetActionText("part3");

   progress.SetNeededSteps(1);

   progress.Step(1);

   System.Threading.Thread.Sleep(4500);    // TODO: Some processing

   progress.EndPart(true);

}

```

**C#**

```


using (var progress = new Progress("SimpleProgress"))

{

    progress.SetAllowCancel(true);

    progress.SetAskOnCancel(true);

    progress.SetTitle("Replace parts");

    progress.ShowImmediately();

    var finder = new DMObjectsFinder(oProject);

    var articleReferences = finder.GetArticleReferences(null);

    var nIteration = 0;

    var progressPartInPercentage = 100.0 / articleReferences.Length;

    foreach (var articleReference in articleReferences)

    {

        // Set new values

        progress.BeginPart(progressPartInPercentage, $"Iteration : {nIteration++}");

        articleReference.PartNr = "New part number";

        articleReference.VariantNr = "New variant";

        articleReference.StoreToObject();

        new DeviceService().UpdateDevice(articleReference.ParentObject);

        progress.EndPart();

    }

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Progress Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~_ctor.html) | Overloaded. |



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


