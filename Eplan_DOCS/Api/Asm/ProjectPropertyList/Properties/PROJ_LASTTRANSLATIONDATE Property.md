# PROJ_LASTTRANSLATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_LASTTRANSLATIONDATE().html

---

Last translation: Date # 10024.

Syntax

**C#**



public PropertyValue PROJ_LASTTRANSLATIONDATE {get; set;}

public:

property PropertyValue^ PROJ_LASTTRANSLATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

The date of the last foreign language translation. How the date is displayed can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
