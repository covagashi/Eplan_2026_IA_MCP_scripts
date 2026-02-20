# Basic operations on parts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/BasicPartOperations.html

---

The following example shows how to work with parts in the parts database:

**C#**

```


// Get all parts

var listOfAllParts = partsDatabase.Parts;

// Export all parts to the EDZ format

if (partsDatabase.ExportParts("D:\\exportDirectory\\export.edz", MDPartsDatabase.DataFormat.EDZ))

    new Decider().Decide(EnumDecisionType.eOkDecision, "Part export successful", "Export Part", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Add a new part variant

string partName = "MyTestPart-123";

if (!partsDatabase.ExistsPart(partName))

{       

    var part = partsDatabase.AddPart(partName, "2");       

}

// Get a part, export it and remove it

if (partsDatabase.ExistsPart(partName));

{

    // Get a part by name

    var part = partsDatabase.GetPart(partName);

    new Decider().Decide(

    EnumDecisionType.eOkDecision,

    "Part number: " + part.PartNr + " \nVariant: " + part.Variant,

    "Part Loaded",

    EnumDecisionReturn.eOK,

    EnumDecisionReturn.eOK); 

    // Export selected part(s) to XML

    MDPart[] partsToExport = new MDPart[] { part };

    partsDatabase.ExportParts("C:\\exportDirectory\\exportFile.xml", MDPartsDatabase.DataFormat.XML, partsToExport);          

    // Remove part

    partsDatabase.RemovePart(part);

    if (!partsDatabase.ExistsPart(partName)) ;

        new Decider().Decide(EnumDecisionType.eOkDecision, "Part Removed", "Part Removed", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

// Export all database items: parts(true), addresses(true), constructions(true), terminals(true), accessory lists(true), accessory placements(true) to XML

if (partsDatabase.ExportPartsDatabaseItems("C:\\exportDirectory\\exportFile.xml", MDPartsDatabase.DataFormat.XML, true, true, true, true, true, true))

     new Decider().Decide(EnumDecisionType.eOkDecision, "Export successful", "Export Part", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

```

These operations are also available for  AccessoryPlacement,  ConnectionInfoPoint,  Construction,  Customer,  Manufacturer  and  AccessoryList.

For example, to add or remove  AccessortList  use:

**C#**

```


// Add AccessoryList

MDAccessoryList accessoryList = partsDatabase.AddAccessoryList("accessoryListName");

// Remove AccessoryList

partsDatabase.RemoveAccessoryList(accessoryList);

```