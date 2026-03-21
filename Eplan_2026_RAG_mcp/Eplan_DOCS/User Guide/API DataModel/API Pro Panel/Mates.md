# Mates

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Mates.html

---

It is also possible to transform 3D objects by snapping, i.e. by using auxiliary points called "**mates**".

There are 2 kinds of mates:

- **Source mates** ' Points of a source object that we want to transform. In the GUI they are grey.
- **Target mates** ' The ones that we snap to. In the GUI they are blue.

Another division is based on the purpose and the shape of the mates:

- **Point mates** (classes [PointMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate.html), [HandleMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate.html), [BasePointMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BasePointMate.html), [MountingPointMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPointMate.html), [PlacementAreaPointMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlacementAreaPointMate.html))
- **Line mates** (classes [LineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.LineMate.html), [MountingLineMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingLineMate.html))
- **Plane mates** (class [PlaneMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaneMate.html))

### Getting mates

Mates can be retrieved from a  Placement3D  using methods:

```csharp
PointMate[] GetSourceMates(Mate.Enums.PlacementOptions ePlacementOptions)
 PointMate FindSourceMate(string name, Mate.Enums.PlacementOptions ePlacementOptions)
 Mate[] GetTargetMates(bool bConsiderMountingClearance)
 Mate FindTargetMate(string name, bool bConsiderMountingClearance)
```

### Snapping

Snapping mates causes one object to be positioned close to the other, i.e. a source mate of one object is at the position of a target mate of another object. In this case, we need to find the relevant mates from both objects and then perform snapping usingm the SnapTo method. Here is an example of how to snap a cabinet to another one through a point target mate:

```csharp
Cabinet oCabinet2 = new Cabinet();
 oCabinet2.Create(oProject, "TS 8886.500", "1");
 // Placing a cabinet next to another cabinet with 0.0 offset
 oCabinet2.FindSourceMate("C3", Mate.Enums.PlacementOptions.None)
 .SnapTo(oCabinet.FindTargetMate("CUB4", false), 0.0);
```

Here are also examples of snapping to a line and a plane mate. They both are base mates, which means that snapping to them will automatically sets a source object as a child of a target. Also, the orientation of a source item is adjusted to a target:

```csharp
// Get front plane of mounting panel
 MountingPanel oMountingPanel = oCabinet.Children[1] as MountingPanel;
 Plane oFrontPlace = oCabinet.Planes[0];
 // Create a mounting rail with a length of 150
 MountingRail oRail = new MountingRail();
 oRail.Create(oProject, "TS 110_15", "1", 500.0);
 // Placing a rail by using a plane mate as a target (located 100,200 from start of mounting panel, 
 // Without any rotation)
 oRail.GetSourceMates(Mate.Enums.PlacementOptions.None)[2]
 .SnapTo(oFrontPlace.BaseMate, 0.0, 100.0, 200.0);
 // Creating a terminal
 Component oTerminal = new Component();
 oTerminal.Create(oProject, "SIE.4AV2400-2EB00-0A", "1");
 // Placing it on a mounting rail with offset 100 from the beginning of it. 
 // Target (oRail.BaseMate) is a line mate.
 oTerminal.FindSourceMate("M4", false).SnapTo(oRail.BaseMate, 100.0);

```

Please be aware that not all mates can be snapped to each other. This is determined by the [Mate.MatchingMateNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~MatchingMateNames.html) property. To make sure that one mate can be snapped to another, please use the [PointMate::CanSnapTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate~CanSnapTo.html) method.

### Creating custom mates

It is also possible to create a custom mate, for example a mounting point or a handle. In this case, a mate is first created as a transient object and then needs to be saved on a Placement3D:

```csharp
// Create a handle relative to placement area
 var transformationToPlacementArea = new Matrix3D();
 transformationToPlacementArea.Translate(new Vector3D(50.0, 500.0, 0.0));
 var transformation = transformationToPlacementArea * placement3D.PlacementArea.RelativeTransformation;
 var handle = new HandleMate();
 handle.Create(new MultiLangString(), transformation);
 placement3D.AddMatePersistent(handle);
 
 // Create a handle with extended logic 
 var handleWithExtendedLogic = new HandleMate();
 handleWithExtendedLogic.Create(new[] {"V1", "V2"}, new MultiLangString(), new Matrix3D());
 placement3D.AddMatePersistent(handleWithExtendedLogic);
 
 // Create a base point
 var basePoint = new BasePointMate();
 basePoint.Create(BasePointMate.Enums.Name.FrameProfileDownLeftRear, 
 new MultiLangString(),
 new Matrix3D {OffsetX = 200.0, OffsetY = 300.0});
 placement3D.AddMatePersistent(basePoint);
 
 // Create a mounting point
 var mountingPoint = new MountingPointMate();
 mountingPoint.Create("Test mounting point", 
 new MultiLangString(),
 new Matrix3D{OffsetY = 100.0, OffsetZ = 400.0});
 placement3D.AddMatePersistent(mountingPoint);
 
 // Create a mounting line
 var mountingLineMate = new MountingLineMate();
 mountingLineMate.Create("Test mounting line",
 new MultiLangString(),
 new PointD3D(10.0, 10.0, 10.0), new PointD3D(110.0, 210.0, 310.0));
 placement3D.AddMatePersistent(mountingLineMate);

```

Please be aware that the coordinates of a mate are relative until it is not persistent, i.e. without a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Placement.html) set. After calling [Placement3D::AddMatePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddMatePersistent.html), they are recalculated and become absolute.
