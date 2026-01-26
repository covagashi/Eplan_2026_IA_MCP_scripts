# Shadow copying for add-ins

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ShadowCopyingAPIAssemblies.html

---

### Introduction

Since version 2.6, Eplan API assemblies are shadow copied, i.e. they are saved in a temporary folder during registration and loaded from there.

The benefit of the shadow copy technique is that the original assemblies are not locked, so that newer versions can be distributed via a network share even if they are currently being used by other workstations.

This applies to both add-ins and add-ons. For more information regarding add-ons, please refer to the [Shadow copying for add-ons](ShadowCopying.html) chapter.

### Process for add-ins

When an add-in is loaded by Eplan start or via API > Manage option, the **add-in** and its **referenced DLLs** (including all subdirectories) are copied to a user application roaming directory. The path of this shadow directory is:

%appdata%\EPLAN\ShadowCopyAssemblies\Process-ID\Addin-Name\bin

Example:

This means that all referenced files (\*.dll  and  \*.exe) and all subdirectories that also contain references (language subdirectories, etc.) are also copied. After resolving, they will be copied to the shadow directory.

### Possible issues and troubleshooting

**Referencing relative paths**  
The shadow copy technique could lead to errors if the add-in references data from other directories using a relative path to the original add-in directory.

**Solution**: Use the  [IEplAddInShadowCopy](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy.html)  interface, that allows you to get the original path of an add-in.

**Using an assembly in different versions**  
In addition, conflicts can arise when multiple add-in projects in a solution refer to an assembly with a namespace and class of the same name, but different versions. The following scenario illustrates the problem:  
Let's assume that you use the  Write  library of version 1.0.0 in one project (Project1) and the  Write  library of version 2.0.0 in the other project (Project2). This will lead to unwanted behavior in your solution: Depending on which project ' be it Project1 or Project2 ' you call first, it will be executed correctly and will reference the correct library. If you then execute the other project, it will reference the previous library, the first version is executed.

**Solution**: To work around this behavior, sign the library versions independently of each other. You can then use the library with different versions at will. Signing gives the library a specific key token or "strong name" that helps distinguish the libraries.
