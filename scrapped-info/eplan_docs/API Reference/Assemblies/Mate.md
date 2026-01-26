# Mate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html

---

Mate is a class that helps to define the position of 3D placements. One or more Mates belong to an object of type Placement3D.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.E3D.Mate**  
      [Eplan.EplApi.DataModel.E3D.GridMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate.html)  
      [Eplan.EplApi.DataModel.E3D.LineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate.html)  
      [Eplan.EplApi.DataModel.E3D.PlaneMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaneMate.html)  
      [Eplan.EplApi.DataModel.E3D.PointMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate.html)

Syntax

**C#**



public class Mate

public ref class Mate


Remarks

There are two different types of mates: stored in database and generated in runtime. First can be created by user and assign to a [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html). Name of generated mate depends on type of object. Mate named 'V1'is placed on first vertex (lowest left in local coordinate system of the object). Numeration of those mates is done in counterclockwise direction. Very similar are mates which name starts with 'M', only those mates are placed in the middle of edges and the first on is the lowest one (in the local coordinate system). Third type of mate that can be found is named "C". This one is placed in the center of object. Check mate description for more information about current mate.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Mate Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~_ctor().html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Description.html) | Description of this mate. |
| Public Property | [IsBaseMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsBaseMate.html) | Return true, if mate is base mate. |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsReadOnly.html) | Determines if Mate can be modified. |
| Public Property | [IsUserDefined](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsUserDefined.html) | Returns true, if mate is used defined. |
| Public Property | [MatchingMateNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~MatchingMateNames.html) | Names of mates that can be snapped to this one separated by '#'. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Name.html) | Name of this mate. |
| Public Property | [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Placement.html) | [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) to which this mate is assign. |
| Public Property | [Rotation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Rotation.html) | Angle by which the components are to be rotated when they are placed on the mounting point. |
| Public Property | [RotationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~RotationType.html) | Rotation type which this mate force while snapping. |
| Public Property | [Source](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Source.html) | Returns object from which the mate was returned or changed by: Placement3D.GetTargetMates, Placement3D.GetSourceMates, Placement3D.AddMatePersistent or BaseMate property. |
| Public Property | [Transformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transformation.html) | Position and rotation relative to the parent placement represented by transformation matrix. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Dispose().html) | Destructor for deterministic finalization of Mate object. |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Equals.html) | Operator of comparison implementation. Checks if two mates have same name and belongs to the same object. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Remove.html) | Removes the Mate object. |
| Public Method | [StoreToObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~StoreToObject.html) | Stores changes into a project database. |
| Public Method | [Transform](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transform.html) | Transform mate position. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~op_Equality.html) | Operator of comparison implementation. Checks if two mates have same name and belongs to the same object. |
| public Operator [Inequality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~op_Inequality.html) | Operator of comparison implementation. Checks if two mates have different name or not belongs to the same object. |


