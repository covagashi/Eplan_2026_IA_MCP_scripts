# Placing window macros

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/HE_PlaceMacros.html

---

An Eplan macro is a piece of schematics that can be introduced into a project ' onto a page or as a page. Eplan uses file macros. They can have the extension  \*.ema  for window macros,  \*.emp  for page macros, and  \*.ems  for symbol macros.

For placing macros, the Eplan API provides the class  Eplan.EplApi.HEServices.Insert. This class basically contains three overloaded methods for placing each type of macro. A window or symbol macro can be placed on a page either with absolute coordinates or with an offset relative to its original position.

The following example shows how to place a macro on a page at a given position:

```csharp
Insert oInsert = new Insert();
 oInsert.WindowMacro("$(MD_MACROS)\BECK.KL1012.ema", 0, m_oTestProject.Pages[9], new PointD(70.0, 0.0), Insert.MoveKind.Relative);
```

### Placing macros and assigning value sets

If there are  PlaceHolder  objects in a macro, you can assign value sets using the result of the  Insert.WindoMacro  function:

```csharp
Insert oInsert = new Insert();
         StorableObject[] oInsertedObjects = oInsert.WindowMacro(@"$(MD_MACROS)MacroWithPlaceholder.ema", 0, m_oTestProject.Pages[9], new PointD(70.0, 0.0), Insert.MoveKind.Relative);
 
         foreach (StorableObject oSOTemp in oInsertedObjects)
         {
             // We are searching for PlaceHolder "Three-Phase" in the results
              PlaceHolder oPlaceHoldeThreePhase = oSOTemp  as Eplan.EplApi.DataModel.Graphics.PlaceHolder;
             if((oPlaceHoldeThreePhase != null)
                 &&
                 (oPlaceHoldeThreePhase.Name == "Three-Phase")
                 )
              {
                  oPlaceHoldeThreePhase.ApplyRecord("Motor 0,75 KW");
              }
         }
```