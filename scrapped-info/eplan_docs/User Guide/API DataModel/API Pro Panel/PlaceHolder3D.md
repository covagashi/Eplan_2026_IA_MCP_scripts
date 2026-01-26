# PlaceHolder3D

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/PlaceHolder3D_-_placeholder_in_3D_space.html

---

A new placeholder object has been created in EPLAN Pro Panel. A corresponding class  Placeholder3D  has been created in the APIt. This class  Placeholder3D  inherits from  StorableObject  and the  IPlaceHolder  interface.

The methods are similar to those of the standard  PlaceHolder:

```csharp
PlaceHolder3D oNewPlaceHolder3D = new PlaceHolder3D();
 oNewPlaceHolder3D.Create(m_oTestInstallationSpace);
 oNewPlaceHolder3D.Name = "016PlaceHolder3DService_Test008";
 oNewPlaceHolder3D.AddReference(oComponent);
 MultiLangString mlTest = new MultiLangString();
 mlTest.AddString(ISOCode.Language.L_en_US, "<Test123_en>");
 mlTest.AddString(ISOCode.Language.L_de_DE, "<Test123_de>");
 oNewPlaceHolder3D.SetPropertyEntry(oComponent, 20011, mlTest);
 oNewPlaceHolder3D.AddRecord("Record1");
 oNewPlaceHolder3D.AddRecord("Record2");
 
 // Setting values for English
 oNewPlaceHolder3D.set_Value("Record1", "Test123_en", "Value 1");
 oNewPlaceHolder3D.set_Value("Record2", "Test123_en", "Value 2");
 
 // Setting values for German
 oNewPlaceHolder3D.set_Value("Record1", "Test123_de", "Wert 1");
 oNewPlaceHolder3D.set_Value("Record2", "Test123_de", "Wert 2");
 oNewPlaceHolder3D.ApplyRecord("Record1");
```

