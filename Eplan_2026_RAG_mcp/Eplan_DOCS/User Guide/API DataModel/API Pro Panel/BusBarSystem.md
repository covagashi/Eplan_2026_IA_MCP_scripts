# BusBarSystem

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/BusBarSystem.html

---

BusBarSystem  class represent "Busbar system" items in Pro Panel.

### 

**C#**

```


// InstallationSpace

var oInstallationSpace = new InstallationSpace();

oInstallationSpace.Create(oProject, "BusBarSystem_InstallationSpace");

// CopperBundle

var copperBundle = CopperBundle.Create(oProject, new List<Placement3D>());

copperBundle.Parent = oInstallationSpace;

copperBundle.Properties.COPPERBUNDLE_DESIGNATION = "RIT.BBS.RiLine60_1_ECu15x05_2400 - BusBarSystem";

// BusBarSystem

var oBusBarSystem = new BusBarSystem();

var article = "RIT.BBS.RiLine60_1_ECu15x05_2400";

var variant = "1";

var numberOfHolders = 3;

var length = 240;

oBusBarSystem.Create(oProject, article, variant, numberOfHolders, length);

oBusBarSystem.Parent = copperBundle;

```

