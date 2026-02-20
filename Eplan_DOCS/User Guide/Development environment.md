# Development environment

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/DevelopmentEnvironment.html

---

The preferable way to develop Eplan API applications is to reference the API assemblies directly in a .NET project using CLI programming languages like C# (C Sharp), Visual Basic .NET, C++/CLI.  You could do this by just using a text editor and calling the compiler from a DOS box ' like described in the topics "[Creating add-ins in CSharp](CSharpAddins.html)" or "[Creating add-ins in Visual Basic .NET](VisualBasicAddins.html)".

The much more convenient way of developing involves the use of an Integrated Development Environment (IDE). We recommend the use of Microsoft Visual Studio, but there are also free development environments like SharpDevelop. How to start an API project in the Visual Studio is described in the topic "[Eplan .NET API](EplanApiDotNet.html)".

The Eplan API has explicitly been tested and released for Microsoft Windows 7, 8 and 10.

It is not recommended to use Eplan API in separate child threads. This could lead to problems because such configuration wasn't tested nor predicted by API designers.

### Debugging applications

Currently, when debugging applications, the  w3u.exe  process is detached at the beginning of the debug. This happens because  w3u.exe  from the "Electric P8" folder calls  eplan.exe  from the "Platform" folder. In order to continue debugging, please attach to the process  eplan.exe  from "Platform" folder. Another solution is to start debugging  eplan.exe  in the "Platform" folder, with the  Variant  argument, for example:

/Variant:"Electric P8"