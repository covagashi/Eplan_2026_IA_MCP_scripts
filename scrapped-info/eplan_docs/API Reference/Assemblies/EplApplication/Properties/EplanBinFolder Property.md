# EplanBinFolder Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~EplanBinFolder.html

---

Eplan product variant bin path. Path to the w3u.exe of the product variant you want to start. Setting this path is necessary to specify the variant to start for your offline application.

Syntax

**C#**



public string EplanBinFolder {get; set;}

public:

property String^ EplanBinFolder {

   String^ get();

   void set (    String^ value);

}


Remarks

p.e. C:\Program Files (x86)\EPLAN\Electric P8\2.1.0\BIN IMPORTANT: Set this path before calling Init!
