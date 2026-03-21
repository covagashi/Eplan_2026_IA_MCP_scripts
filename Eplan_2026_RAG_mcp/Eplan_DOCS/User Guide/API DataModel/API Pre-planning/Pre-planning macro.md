# Pre-planning macro

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Pre-planning_macro.html

---

For a Pre-planning module, the new  PrePlanningMacro  class has been created to represent macros.

These macros are created as follows:

```csharp
string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
 PrePlanningMacro oPrePlanningMacro = new PrePlanningMacro();
 oPrePlanningMacro.Create(new[] {oPlanningSegment1, oPlanningSegment2}, strMacroPath, oMultiLangString);
```

Inserting macros requires parameters such as the parent planning segment, the path to macro and the project object:

```csharp
string strMacroPath = m_oDir.FullName + "\\TestMacro.emv";
 StorableObject[] arrInsertedPlaObjects = new Insert().PrePlanningMacro(strMacroPath, m_oTestProject, oPlanningSegment1);
```