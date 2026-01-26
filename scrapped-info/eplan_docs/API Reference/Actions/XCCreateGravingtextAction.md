# XCCreateGravingtextAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XCCreateGravingtextAction.html

---

```
 Generates an engraving text from the DTs of the source and target of the cable.

 By default, the designation is abbreviated in accordance with the VASS standard (Volkswagen Audi Seat Skoda),

 i.e., structure identifiers having the same name of source and target are removed - starting from the left.

```

| Parameter | Description |
| --- | --- |
| ``` Complete
 ``` | ``` Retain mounting locations of the same name (optional, 0 = No, 1 = Yes). Default = 0
  If the parameter is not specified or set to 0, the designation is truncated in accordance with the VASS standard (Volkswagen Audi Seat Skoda),
  i.e., structure identifiers having the same name of source and target are removed - starting from the left.
  If this parameter is set to 1, mounting locations of the same name for the source and target remain.
 ``` |

**Remarks**

```
The project structure must conform to the VASS standard so that the abbreviation rules are executed correctly.

```

**Example**

```
                Generate engraving text with truncated designation

                XCCreateGravingtextActionXCCreateGravingtextAction /Complete:0

        Generate engraving text without truncation of designation

                XCCreateGravingtextAction /Complete:1

```