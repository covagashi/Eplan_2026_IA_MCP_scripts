# Getting 3D objects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Getting_3d_objects.html

---

Getting 3D objects

The  DMObjectsFinder  class was enhanced with methods for searching 3D objects.

```csharp
// Searching 3D functions with the name '=EB3+ET1-U1'
 string str3DFunction = "=EB3+ET1-U1";
 Functions3DFilter oFunctions3DFilter = new Functions3DFilter();
 Function3DPropertyList oFunction3DPropertyList = new Function3DPropertyList();
 oFunction3DPropertyList.FUNC_FULLDEVICETAG = str3DFunction;
 oFunctions3DFilter.SetFilteredPropertyList(oFunction3DPropertyList);
 Function3D[] oFunctions3D = new DMObjectsFinder(m_oEplanDemoProject).GetFunctions3D(oFunctions3DFilter);
 // Searching 3D and 2D functions with the name '=EB3+ET1-Q1'
 FunctionsFilter oFunctionsFilter = new FunctionsFilter();
 oFunctionsFilter.ExactNameMatching = true;
 oFunctionsFilter.Name = "=EB3+ET1-Q1";
 Functions3DFilter oFunctions3DFilter = new Functions3DFilter();
 Function3DPropertyList oFunction3DPropertyList = new Function3DPropertyList();
 oFunction3DPropertyList.FUNC_FULLNAME = "=EB3+ET1-Q1";
 oFunctions3DFilter.SetFilteredPropertyList(oFunction3DPropertyList);
 IFunctionBase[] oAllWithTheSameName = new DMObjectsFinder(m_oEplanDemoProject).GetFunctions(oFunctionsFilter, oFunctions3DFilter);
 // Searching 3D placements
 Placements3DFilter oPlacements3DFilter = new Placements3DFilter();
 oPlacements3DFilter.Category = Function.Enums.Category.AreaDefinition;
 Placement3D[] oPlacements3D = new DMObjectsFinder(oProject).GetPlacements3D(oPlacements3DFilter);

```