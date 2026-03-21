# SystemConfiguration Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~SystemConfiguration.html

---

System configuration scheme name.

Syntax

**C#**



public string SystemConfiguration {get; set;}

public:

property String^ SystemConfiguration {

   String^ get();

   void set (    String^ value);

}


Remarks

A system configuration scheme defines paths to user, station company settings, master data and rights database in the SystemConfiguartion.xml file. These paths are set by default by Eplan setup and could be overwritten using a system configuration scheme.
