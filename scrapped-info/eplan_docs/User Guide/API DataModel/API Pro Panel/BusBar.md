# BusBar

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/BusBar.html

---

The  BusBar  class represents "Busbar (bending)" items in Pro Panel.

BusBar  object using an article with a graphical macro.

**C#**

```


// InstallationSpace

var oInstallationSpace = new InstallationSpace();

oInstallationSpace.Create(oProject, "BusBar_InstallationSpace_1");

// CopperBundle

var copperBundle = CopperBundle.Create(oProject, new List<Placement3D>());

copperBundle.Parent = oInstallationSpace;

copperBundle.Properties.COPPERBUNDLE_DESIGNATION = "Connector kit below L1_3D 1 -BusBar";

// BusBar

var article = "Connector kit below L1_3D";

var variant = "1";

BusBar.Create(copperBundle, article, variant);

```

BusBar  object with more parameters, e.g. bending radius and a path to a  \*.fp1  file containing copper form.

**C#**

```


// InstallationSpace

var oInstallationSpace = new InstallationSpace();

oInstallationSpace.Create(oProject, "BusBar_InstallationSpace_2");

// CopperBundle

var copperBundle = CopperBundle.Create(oProject, new List<Placement3D>());

copperBundle.Parent = oInstallationSpace;

copperBundle.Properties.COPPERBUNDLE_DESIGNATION = "RIT.9684004_V - BusBar";

// BusBar

var fp1Path = "D:\\winkel.fp1";

var article = "RIT.9684004_V";

var variant = "1";

var bendingRadius = 5.0;

var listOfAdditionalObjects = new List<Placement3D>();

BusBar.Create(oProject, article, variant, fp1Path, bendingRadius, copperBundle, listOfAdditionalObjects);

```

BusBar with flat bendings set by API

**C#**

```


                var busBar = BusBar.Create(testProject, "RIT.3589005", "1","c:\\temp\\linie.fp1",

                    5.0, copperBundle, additionalObjects, 0);

                var points = new[]

                {

                    new PointD3D( 0.0, 0.0, 0.0),   //(start)

                    new PointD3D( 0.0, 47.0, 0.0),  // 1st bending point

                    new PointD3D( 0.0, 102.0, 0.0), // 2nd bending point

                    new PointD3D( 0.0, 245.0, 0.0), // 3rd bending point

                    new PointD3D( 0.0, 300.0, 0.0), //(end)

                };

                // Set bending points coordinates

                busBar.BendingPoints = points;

                // Set bending angles

                var degreesToRadiansMultiplier = Math.PI / 180.0;

                busBar.ChangeSegmentAngle(-45.0 * degreesToRadiansMultiplier, 1, 5); 

                busBar.ChangeSegmentAngle(45.0  * degreesToRadiansMultiplier, 2, 5);

                busBar.ChangeSegmentAngle(-90.0 * degreesToRadiansMultiplier, 3, 5);

```

BusBar with edgewise bendings set by API

**C#**

```


                var busBar = BusBar.Create(m_oTestProject, "RIT.3589005", "1","c:\\temp\\linie.fp1",

                    5.0, copperBundle, additionalObjects, BusBar.Enums.BendingType.Edgewise);

                var points = new[]

                {

                    new PointD3D( 0.0, 0.0, 0.0),   //(start)

                    new PointD3D( 0.0, 47.0, 0.0),  // 1st bending point

                    new PointD3D( 0.0, 102.0, 0.0), // 2nd bending point

                    new PointD3D( 0.0, 245.0, 0.0), // 3rd bending point

                    new PointD3D( 0.0, 300.0, 0.0), //(end)

                };

                // Set bending points coordinates

                busBar.BendingPoints = points;

                // Set bending angles

                var degreesToRadiansMultiplier = Math.PI / 180.0;

                busBar.ChangeSegmentAngle(-45.0 * degreesToRadiansMultiplier, 1, 5, BusBar.Enums.BendingType.Edgewise);

                busBar.ChangeSegmentAngle(45.0 * degreesToRadiansMultiplier, 2, 5, BusBar.Enums.BendingType.Edgewise);

                busBar.ChangeSegmentAngle(-90.0 * degreesToRadiansMultiplier, 3, 5, BusBar.Enums.BendingType.Edgewise);

```