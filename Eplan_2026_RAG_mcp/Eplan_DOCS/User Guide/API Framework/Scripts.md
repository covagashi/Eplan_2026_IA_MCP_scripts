# Scripts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Scripts.html

---

You can run scripts in Eplan without having licensed the Eplan API. Scripts are executable program code, written in C# (\*.cs files) or Visual Basic.NET (\*.vb files). Scripts always exist as source code. When you start a script, it will be loaded into the system, compiled and then executed.

For scripting, go to the ribbon item File > Extras > Interfaces. You will find the category Scripts.

After calling File > Extras > Interfaces > Scripts > Run, a file dialog appears and a script file to execute can be selected.

The following assemblies can be used in scripts:

- System
  - Namespace System
- System.Drawing
- System.Windows.Forms
  - Namespace System.Windows.Forms
- System.Net.Http
  - Namespace System.Net.Http
- System.IO.Compression.FileSystem
- System.Xml.LINQ
- System.Xml
- System.Core
  - Namespace System.Linq
- Newtonsoft.Json

Also these Eplan assemblies are referenced by default:

- Eplan.EplApi.Baseu
  - Namespace Eplan.EplApi.Base
- Eplan.EplApi.ApplicationFrameworku
  - Namespace Eplan.EplApi.ApplicationFramework
  - Namespace Eplan.EplApi.Scripting
- Eplan.EplApi.Guiu
  - Namespace Eplan.EplApi.Gui
  - NameSpace Eplan.EplApi.Scripting
- Eplan.EplApi.MasterDatau
  - Namespace Eplan.EplApi.MasterData
- Eplan.IdentityClient.Authentification
  - Namespace Eplan.IdentityClient.Authentification
- Eplan.IdentityClient.Types
  - Namespace Eplan.IdentityClient

**There is no way to reference additional assemblies (.NET Framework, Eplan or other providers)!**

This feature is only available for Eplan API developers having "Eplan API Extension" license.