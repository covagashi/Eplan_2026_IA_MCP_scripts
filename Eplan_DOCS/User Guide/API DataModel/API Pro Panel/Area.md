# Area

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Area.html

---

The  Area  is a part of the mounting surface on which 3D placements can not be placed. As soon as a parts placement is put into a restricted placing area, an error is generated (by verification no. 026012).

```csharp
MountingPanel oMountingPanel = new MountingPanel();
 oMountingPanel.Create(m_oTestProject, 500.0, 500.0, 2.0);
 oMountingPanel.Parent = m_oInstallationSpace;
 MultiLangString oFunctionDefinitionName = new MultiLangString();
 
 oFunctionDefinitionName.AddString(ISOCode.Language.L_en_US, "Restricted mounting area");
 MultiLangString oGroup = new MultiLangString();
 oGroup.AddString(ISOCode.Language.L_en_US, "Restricted area");
 FunctionDefinition oFunctionDefinition = new FunctionDefinition(m_oTestProject, Function.Enums.Category.AreaDefinition, oGroup, oFunctionDefinitionName); Area oArea = new Area();
 oArea.Create(m_oTestProject, oFunctionDefinition);
 oArea.Parent = oMountingPanel.Planes[0];
 oArea.Size = new PointD(200.0, 250.0);
```

