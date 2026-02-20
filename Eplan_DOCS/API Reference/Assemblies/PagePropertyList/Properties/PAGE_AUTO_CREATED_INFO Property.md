# PAGE_AUTO_CREATED_INFO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_AUTO_CREATED_INFO().html

---

Automatically generated # 11006.

Syntax

**C#**



public PropertyValue PAGE_AUTO_CREATED_INFO {get; set;}

public:

property PropertyValue^ PAGE_AUTO_CREATED_INFO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether the page has been automatically generated, and provides information about the author:

0 = No

1 = Single-line representation (PLC schematic generation)

2 = Multi-line representation (PLC schematic generation)

3 = I/O overview (PLC schematic generation)

4 = Rack overview (PLC schematic generation)

5 = Eplan Engineering Configuration

6 = Schematic generator (ESG)

7 = Report

8 = Pre-planning.
