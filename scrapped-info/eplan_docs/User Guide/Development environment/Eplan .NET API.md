# Eplan .NET API

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/EplanApiDotNet.html

---

Eplan API was created using the Microsoft® .NET 4.8.1 technology.

To develop applications with the Eplan API, we recommend Microsoft Visual Studio 2022 or 2019. However it should also work with other development environments for the Microsoft .NET Framework 4.8.1. However, the Eplan API was not tested with IDEs other than the one mentioned above.

To start a new Eplan API project in Microsoft Visual Studio 2022, select File > New > Project... in the ribbon. In the Create Project dialog, first select the programming language you want to use (C#, Visual Basic, or C++).

Next step is to decide what type of application you want to write:

- For an [add-in](AddIns.html), you either select a "Class Library" project or you use the Add-in Wizard provided by Eplan. The procedure for using the Add-in Wizard is described in the topic "[Creating an add-in in Visual Studio](AddinInVisualStudio.html)". If you want to create an add-in without using the wizard, simply add the references to the API assemblies. At a minimum, you must reference  Eplan.EplApi.AF.dll  and  Eplan.EplApi.Base.dll. Read more about creating add-ins in the topics below "[Add-ins](AddIns.html)". In your project settings (for example in Visual Studio) under Configuration Properties > Debugging add the  w3u.exe  as startup program (or  eplan.exe  with the  Variant  parameter) and make sure the created DLL is copied into the Eplan platform  bin  folder after building it.
- For an offline-program, for example, create a new Windows Application project and proceed as described in the topic "[Using Eplan API assemblies in other processes](UsingEplanAssemblies.html)". Make sure that a path is set to the Eplan platform  bin  directory or the working directory of your code project is set respectively, otherwise the corresponding DLLs may not be found.

### Remarks

Working with an older Eplan API requires a suitable environment for this version of the framework.

For example version 2.8 of Eplan API was developed for the Microsoft .NET Framework 4.5.2.

Make sure that you don't mix up Eplan API assemblies that use different frameworks.