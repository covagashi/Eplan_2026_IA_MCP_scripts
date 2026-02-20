# PlcDcXMLExchangerUniversal

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/PlcDcXMLExchangerUniversal.html

---

```
Imports or exports PLC data in the system database from or to the PIB format. The supported file extension is "*.pbf".

```

**Remarks**

```
Export format version can be selected via setting USER.PlcGui.PlcExport.StandardConverterFileVersion


Export to version V1.0 (compatibility mode) can be achieved by ...StandardConverterFileVersion = 0


Export to version V2.0 (new, extended format) can be achieved by ...StandardConverterFileVersion = 1


Visible name = "PLC standard echange format"


Required for methods ExportData(), ImportData()

```