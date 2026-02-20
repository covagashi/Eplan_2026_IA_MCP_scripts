# ICustomFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html

---

This is an interface that can be used for user-defined filtering in [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html). User has to implement "IsMatching" method by himself.

Syntax

**C#**



public interface ICustomFilter

public interface class ICustomFilter


Example

**C#**

```
class MyFilter : ICustomFilter

{

	public bool IsMatching(StorableObject obj)

	{

		Function f = obj as Function;

		if (f != null)

		{

			return (f.IsMainFunction && f.SubFunctions.Length != 0);

		}

		return false;

	}

}

Project proj;//a valid project

DMObjectsFinder finder = new DMObjectsFinder(proj);

Function[] functions = finder.GetFunctionsWithCF(new MyFilter());

//now as a result we have main functions having at least one subfunction.
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [IsMatching](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter~IsMatching.html) | This method should be overridden in order to implement the filter. |


