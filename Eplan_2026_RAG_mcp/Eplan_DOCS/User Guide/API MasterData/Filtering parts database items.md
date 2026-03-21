# Filtering parts database items

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/FilteringParts.html

---

The following example shows how to filter the parts database using the  MDObjectFilter()  class:

**C#**

```


using (MDPartsDatabase partsDatabase = new MDPartsManagement().OpenDatabase())

{

    // Get all parts with part number beginning with "SIE"

    MDObjectFilter mDObjectFilter = new MDObjectFilter();           

    mDObjectFilter.AddPropertyCondition(22001, MDObjectFilter.CompareOperator.OperatorEqual, "SIE*"); //22001 - enum Properties.MDPartsDatabaseItem

    MDPart[] arrParts = partsDatabase.GetParts(mDObjectFilter);       

    partsDatabase.ExportParts("C:\\exportDirectory\\exportFile.xml", MDPartsDatabase.DataFormat.XML, arrParts);

}

```

Filtering the parts database using a  Linq  query:

**C#**

```


using (MDPartsDatabase partsDatabase = new MDPartsManagement().OpenDatabase())

{

    // Export only parts modified today

    var today = DateTime.Today;

    var partsModifiedToday = partsDatabase.Parts.Where(item => item.Properties.PART_LASTCHANGE_DATE.ToTime() > today);

    partsDatabase.ExportPartsDatabaseItems("C:\\exportDirectory\\exportFile.xml", MDPartsDatabase.DataFormat.XML, partsModifiedToday);

}

```