# XCabCalculateEnclosureTotalWeightAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCabCalculateEnclosureTotalWeightAction.html

---

```
Calculates the total weight of a cabinet and writes it to the "Total weight" property (#36108 - FUNCTION3D_CABINET_TOTALWEIGHT)

```

| Parameter | Description |
| --- | --- |
| ``` ProjectName
 ``` | ``` Project name with full path (optional input parameter for the "All cabinets" mode).
  When the specified project is not open, this action opens it and closes it automatically after this action is executed.
  If the project is invalid, the current project will be used.
 ``` |
| ``` DatabaseId
 ``` | ``` Database ID of the project to be used (optional input parameter for the "All cabinets" mode).
  When using this parameter, the project must be opened in P8 beforehand. If the project is invalid, the current project will be used.
  If the ProjectName parameter is specified, the DatabaseId parameter is not taken into account.
 ``` |
| ``` CabinetTotalWeight
 ``` | ``` Total weight of a single cabinet (optional output parameter for the "One cabinet" mode). If the mode is "One cabinet", this parameter contains the result of the calculation.
 ``` |

**Remarks**

```
 "All cabinets" mode:

 If a project is specified in the calling context (parameter "ProjectName" or parameter "DatabaseId" is set), all weights of all cabinets in the project are calculated.

 The results are stored in the "Total weight" property (#36108 - FUNCTION3D_CABINET_TOTALWEIGHT) of each cabinet.

 If no project is specified in the calling context, the currently selected project is being used.

 "One cabinet" mode:

 As an alternative to setting the ProjectName or DatabaseId, a single Cabinet object can be passed through a special DMBaseHandleContext.

 In this case, only the total weight of this cabinet will be calculated.

 In this mode, the "Total weight" property (#36108 - FUNCTION3D_CABINET_TOTALWEIGHT) is not set,

 instead the result is set in the calling context to the output parameter "CabinetTotalWeight".

 For the "One cabinet" mode, the project must be opened in P8 beforehand.

```

**Example**

```
        "All cabinets" mode:

                XCabCalculateEnclosureTotalWeightAction /DatabaseId:28

                XCabCalculateEnclosureTotalWeightAction /ProjectName:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

        "One cabinet" mode: A Cabinet object selected in GUI is passed by the context.

                // Create special calling context

                StorableObjectContext context = new StorableObjectContext();

                // Get selected cabinet from GUI

                SelectionSet selectionSet = new SelectionSet();

                StorableObject[] storableObjects = selectionSet.Selection;

                if (storableObjects.Length > 0)

                {

                        Cabinet selectedCabinet = (Cabinet)Array.Find(storableObjects, storableObject = > storableObject.TypeIdentifier == 179); // 179: TYPEID_DMCABINET

                        // Set selected cabinet to context

                        context.StorableObject = selectedCabinet;

                        // Execute Action

                        if (new CommandLineInterpreter().Execute("XCabCalculateEnclosureTotalWeightAction", context))

                        {

                                // Get cabinet weight from context

                                string weight = "";

                                context.GetParameter("CabinetTotalWeight", ref weight);

                                System.Windows.Forms.MessageBox.Show("Total weight of cabinet '" + selectedCabinet.Name + "': " + weight);

                        }

                }

```