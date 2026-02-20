# PlaceHolder

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html

---

Using the PlaceHolder object you can forward records of properties to the references objects. You also can get information about place holders in macros.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)  
            **Eplan.EplApi.DataModel.Graphics.PlaceHolder**

Syntax

**C#**



public class PlaceHolder : GraphicalPlacement, Eplan.EplApi.DataModel.IPlaceHolder, Eplan.EplApi.DataModel.IPropertyPlacementsContainer

public ref class PlaceHolder : public GraphicalPlacement, Eplan.EplApi.DataModel.IPlaceHolder, Eplan.EplApi.DataModel.IPropertyPlacementsContainer


Remarks

To reduce the number of displayed properties refer to two user settings. First is 'USER.MacrosGui.XMDlgPlaceholder.ShowOnlyFilled' which controls if properties with empty value in 'Variable' column are displayed. Second setting is 'USER.MacrosGui.XMDlgPlaceholder.ShowCurrentValueFilled' which controls if properties with empty value in 'Current value' column are displayed.

Example

The following example shows how to use class PlaceHolder. Here is example of PlaceHolder having IsChangeable property set.

**C#**

```


// Create PlaceHolder

PlaceHolder placeHolder = new PlaceHolder();

placeHolder.Create(oPage);

placeHolder.Location = new PointD(80.0, 200.0);

placeHolder.Name = "PlaceHolder 1";

// Add variables and set values to records

placeHolder.Variables.Add("X VAR");

placeHolder.ValueSets.Add("Set 1");

placeHolder.ValueSets.Add("Set 2");

//setting values

MultiLangString oMultiLangString = new MultiLangString();

oMultiLangString.AddString(ISOCode.Language.L___, "test string");

placeHolder.Values["X VAR", "Set 1"] = oMultiLangString;

// Set variable for FUNC_TEXT property

Eplan.EplApi.Base.MultiLangString funcText = new MultiLangString();

funcText.AddString(ISOCode.Language.L_en_US, "<X VAR>");

placeHolder.SetPropertyEntry(oFunction, Properties.Function.FUNCTION_MESSAGETEXT, funcText);

//Apply record

placeHolder.ApplyRecord("Set 1");

```

**C#**

```
//creating PlaceHolder

PlaceHolder oPlaceHolder = new PlaceHolder();

oPlaceHolder.Create(m_oTestPage);

oPlaceHolder.Variables.Add(new PlaceHolder.Variable(oPlaceHolder, "test variable 1"));

oPlaceHolder.Variables.Add("test variable 2");

oPlaceHolder.Variables.Add("test variable 3");

oPlaceHolder.Variables.Remove("test variable 2");

//adding value sets

oPlaceHolder.ValueSets.Add("value set 1");

oPlaceHolder.ValueSets.Add("value set 2");

oPlaceHolder.ValueSets.Add("value set 3");

oPlaceHolder.ValueSets.Remove("value set 1");

//setting values

MultiLangString oMultiLangString = new MultiLangString();

oMultiLangString.AddString(ISOCode.Language.L___, "test string");

oPlaceHolder.Values["test variable 1", "value set 3"] = oMultiLangString;

//setting IsChangeable

oPlaceHolder.Variables["test variable 3"].IsChangeable = !oPlaceHolder.Variables[0].IsChangeable;

oPlaceHolder.Variables.Add("test variable 2", true);

//clearing variables and value sets                 

oPlaceHolder.ValueSets.Clear();

oPlaceHolder.Variables.Clear();

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PlaceHolder Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~_ctor().html) | Default constructor |



Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [Values](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Values.html) | Represents values table of a placeholder |
| Public Field | [ValueSets](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~ValueSets.html) | Represents value sets of a placeholder |
| Public Field | [Variables](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Variables.html) | Represents variables of a placeholder |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArePagePropertiesDisplayed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~ArePagePropertiesDisplayed.html) | Activates the properties of the page for the place holder object. |
| Public Property | [AssignedObjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AssignedObjects.html) | Gets/Sets a list of StorableObject references to a PlaceHolder object. The originally assigned references are replaced. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Layer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Layer.html) | Gets PlaceHolder graphical layer. |
| Public Property | [LayerId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~LayerId.html) | Gets PlaceHolder layer id. |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Location.html) | Overridden. Get or set the placement's location. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Name.html) | Gets/Sets the name of the placeholder. |
| Public Property | [NameOfRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~NameOfRecord.html) | Gets/Sets the name of a record, specified by its index. |
| Public Property | [NumberOfRecords](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~NumberOfRecords.html) | Count of records. |
| Public Property | [NumberOfReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~NumberOfReferences.html) | Count of objects referenced by the PlaceHolder. |
| Public Property | [NumberOfVariables](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~NumberOfVariables.html) | Count of Variables. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Properties.html) | .NET Property enabling access to P8 properties of the PlaceHolder object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~PropertyPlacements.html) | Returns [PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the PlaceHolder. |
| Public Property | [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~SymbolVariant.html) | Specifies [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this PlaceHolder. |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Value](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Value.html) | Gets/Sets the value of a variable for a record. |
| Public Property | [VariableNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~VariableNames.html) | Names of all variables in the PlaceHolder. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AddRecord.html) | Adds a new record with the specified name to the PlaceHolder object. |
| Public Method | [AddReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AddReference.html) | Adds the reference of a Placement object to the placeholder. |
| Public Method | [AddVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AddVariable.html) | Adds a new variable to the PlaceHolder object. |
| Public Method | [ApplyRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~ApplyRecord.html) | Overloaded. Applies a record of values on a PlaceHolder object. |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~Create.html) | Creates a new PlaceHolder object on the specified Page. |
| Public Method | [CreateTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~CreateTransient.html) | Overridden. Creates transient and not placed PlaceHolder object. |
| Public Method | [DeleteRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~DeleteRecord.html) | Overloaded. Deletes a record. |
| Public Method | [DeleteUnusedVariables](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~DeleteUnusedVariables.html) | Deletes all unused variables. |
| Public Method | [DeleteVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~DeleteVariable.html) | Deletes a variable. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of PlaceHolder object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [FindRecord](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~FindRecord.html) | Finds a record by name. |
| Public Method | [FindReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~FindReference.html) | Finds an object in the list of object referenced by a PlaceHolder. |
| Public Method | [FindVariable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~FindVariable.html) | Finds a variable, specified by its name. |
| Public Method | [GetAllCurrentValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetAllCurrentValues.html) | Gets a list of all current values in Placeholder. |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetCurrentValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetCurrentValue.html) | Gets current value for given object, property and index. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetProjectPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetProjectPropertyEntry.html) | Gets a value or variable of Placeholder project property. |
| Public Method | [GetPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetPropertyEntry.html) | Gets a value or variable on a property of an object referenced by a PlaceHolder. |
| Public Method | [GetRecordNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetRecordNames.html) | \Returns the names of all records in the nIndex-th PlaceHolder of a Macro. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetValue.html) | Gets the value of a variable for a record. |
| Public Method | [GetValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetValues.html) | Returns the values of all variables in the nIndex-th PlaceHolder of a Macro variant for a given record. |
| Public Method | [GetVariableNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetVariableNames.html) | \Returns the names of all variables in the nIndex-th PlaceHolder of a Macro variant. |
| Public Method | [IsVariableValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~IsVariableValid.html) | Verifies the correctness if a variable name of a placeholder. If a variable name contains invalid characters, this method \returns false. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [RemoveInvalidObjectReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~RemoveInvalidObjectReferences.html) | Removes invalid (e.g. deleted) object references from a PlaceHolder. |
| Public Method | [RemoveObjectReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~RemoveObjectReferences.html) | Removes object references from a PlaceHolder. |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetProjectPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~SetProjectPropertyEntry.html) | Sets a value or variable on Placeholder project property. The reference of the object will be added to the Placeholder if necessary. |
| Public Method | [SetPropertyEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~SetPropertyEntry.html) | Sets a value or variable on a property of an object referenced by a PlaceHolder. The reference of the object will be added to the PlaceHolder if necessary. |
| Public Method | [SetValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~SetValue.html) | Sets the value of a variable for a record. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


