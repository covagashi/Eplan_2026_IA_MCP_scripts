# ProjectParserParameter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ProjectParserParameter.html

---

Project Parameter Class for the usage with UnitParser. Configure the unit and the look of the Parser result.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)  
      **Eplan.EplApi.DataModel.Graphics.ProjectParserParameter**

Syntax

**C#**



public class ProjectParserParameter : Eplan.EplApi.Base.ParserParameter

public ref class ProjectParserParameter : public Eplan.EplApi.Base.ParserParameter

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectParserParameter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ProjectParserParameter~_ctor.html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [GridSize](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~GridSize.html) | The grid size in millimeters. p.e. "4#" means 4 times grid size (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [Group](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Group.html) | The UnitGroup Property. When first UnitID is set,the group is automatically defined by the unit. While setting a Group also the Unit can be changed to the first Unit in new Group if: - new Group is different than the Group of assigned Unit - there is no Unit and Group assigned When new assigned Group is the same like Unit Group, nothing will change. The unitparser can never convert units of different groups (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [HideUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~HideUnit.html) | Hide the unit of the parsed result. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [HideValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~HideValue.html) | Hide the value of the parsed result, all other texts (units and additional texts) will remain. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [OnlyFirstValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~OnlyFirstValue.html) | Display only the first Value. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [OnlyUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~OnlyUnit.html) | Display only the Unit. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [Precision](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Precision.html) | Set the precision of the result (Values used for calculation: 0 up to 8) (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [SpaceBetweenUnitAndValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~SpaceBetweenUnitAndValue.html) | Add a space between Unit and the value (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [SuppressFloatingZeroes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~SuppressFloatingZeroes.html) | Suppress the last zeroes of a floating result. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [UnitFromParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~UnitFromParameter.html) | Get if the unit needs extra parameter to get resolved. Use the project dependend parameter class if this is true. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [UnitID](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~UnitID.html) | The UnitId Property. Set or get the unit of the parameters. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Property | [WithoutLimiters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~WithoutLimiters.html) | The unit is NOT separated by one of this chars: blank (){}[].,:;!?/\\ (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CanParse](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~CanParse.html) | Parsing can start when the unitid is not empty (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter~Dispose().html) | Destructor for deterministic finalization of ParserParameter object. (Inherited from [Eplan.EplApi.Base.ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html)) |
| Public Method | [SetParameter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ProjectParserParameter~SetParameter.html) | Set the Parameter to resolve the project dependent units, p.e. Length\_Project\_cable |


