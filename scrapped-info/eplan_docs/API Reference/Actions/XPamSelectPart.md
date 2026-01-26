# XPamSelectPart

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPamSelectPart.html

---

```
 Starts the part selection (using the configured database).

```

| Parameter | Description |
| --- | --- |
| ``` DatabaseId
 ``` | ``` ID of the database (optional input parameter).
 ``` |
| ``` SingleSelection
 ``` | ``` Determines whether multiple parts can be selected (optional input parameter).
  Possible values: 0 = No (Allows multiple selections) , 1 = Yes (Only allows a single selection). Default value = 1.
 ``` |
| ``` SelectedPartsCount
 ``` | ``` Number of selected parts (output parameter).
  If the parameter SingleSelection is set to 1, SelectedPartsCount can only be 1 or 0.
 ``` |
| ``` PartNr<nr>
 ``` | ``` PartNr of the selected part (output parameter). "<nr>" needs to be replaced with the index of the selected part (1, 2, ...).
 ``` |
| ``` Variant<nr>
 ``` | ``` Variant of the selected part (output parameter). "<nr>" needs to be replaced with the index of the selected part (1, 2, ...).
 ``` |
| ``` PartType<nr>
 ``` | ``` PartType of the selected part (output parameter). "<nr>" needs to be replaced with the index of the selected part (1, 2, ...).
 ``` |

**Remarks**

```
 The result of the output parameters is returned in the CallingContext.

 See also: "User Guide" > "API Framework" > "Add-Ins" > "Actions" > "Calling actions".

```

**Example**

```
 Enable selection of multiple parts. After calling the action, check the calling context for PartNr, Variant and PartType of the first selected part:

 String strAction = "XPamSelectPart";

 ActionManager oAMnr = new ActionManager();

 Eplan.EplApi.ApplicationFramework.Action oAction = oAMnr.FindAction(strAction);

 if (oAction != null)

 {

                ActionCallingContext actionCallingContext = new ActionCallingContext();

                actionCallingContext.AddParameter("SingleSelection", "false");

                bool bRet = oAction.Execute(actionCallingContext);

                if (bRet)

                {

                        string partNr1 = "";

                        string variant1 = "";

                        string partType1 = "";

                        actionCallingContext.GetParameter("PartNr1", ref partNr1);

                        actionCallingContext.GetParameter("Variant1", ref variant1);

                        actionCallingContext.GetParameter("PartType1", ref partType1);

                }

 }

```