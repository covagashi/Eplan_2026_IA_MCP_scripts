# 3D macros

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/3D_macros.html

---

The standard  WindowMacro  class is used to represent both 3D and 2D window macros. It has been extended with methods that cover 3D functionality.

Creating 3D window macros:

```csharp
MultiLangString oMultiLangString = new MultiLangString();
 oMultiLangString.AddString(ISOCode.Language.L_en_US, "Window macro 3D description");
 string strWindowMacro3DFilePath = m_oTestProject.ProjectDirectoryPath + "\\test_window_macro3D.ema";
 
 WindowMacro oWMacro = new WindowMacro();
 oWMacro.Create(strWindowMacro3DFilePath, 0, new Placement3D[] { oComponent1, oComponent2, oComponent3 }, true, oMultiLangString);

```

Inserting:

```csharp
// Preparing transformation 
 Matrix3D oMatrix = new Matrix3D(); 
 Quaternion oQaternion = new Quaternion(new Vector3D(1.0, 1.0, 1.0), 0.2); 
 oMatrix.Rotate(oQaternion); 
 // Preparing WindowMacro object 
 string strWindowMacroName = "c:\\SIE.3LD9 284-1B.ema"; 
 WindowMacro oWMacro = new WindowMacro(); 
 oWMacro.Open(strWindowMacroName, m_oTestProject, 0); 
 // Insert macro into an InstallationSpace 
 Insert3D oInsert3D = new Insert3D(); 
 StorableObject[] arrStorableObjects = oInsert3D.WindowMacro(oWMacro, nVariant, oInstallationSpace, 
 oMatrix, Insert3D.MoveKind.Absolute, WindowMacro.Enums.NumerationMode.None);

```