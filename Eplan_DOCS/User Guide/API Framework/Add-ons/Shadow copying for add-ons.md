# Shadow copying for add-ons

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ShadowCopying.html

---

### Introduction

Since version 2.6, Eplan API assemblies are shadow copied, i.e. they are saved in a temporary folder during registration and loaded from there.

The benefit of the shadow copy technique is that the original assemblies are not locked, so that newer versions can be distributed via a network share even if they are currently being used by other workstations.

This applies to both add-ons and add-ins. For more information regarding add-ins, please refer to the [Shadow copying for add-ins](ShadowCopyingAPIAssemblies.html) chapter.

### Process for add-ons

For add-ons, the **entire  bin  directory** of the add-on with its subdirectories is copied to the user application roaming directory. The path of this shadow directory is:

%appdata%\EPLAN\ShadowCopyAssemblies\Process-ID\Addon-Name

Example:

This means that all files (\*.dll  and  \*.exe) and all  bin  subdirectories (language subdirectories, etc.) are also copied. This is done when Eplan is started and an add-on is registered or when an add-on is registered manually from the Add-ons dialog.

Eplan loads the assemblies of the add-on from the shadow directory and not from the original add-on directory. This allows an add-on to be updated without the need to stop all Eplan instances using the add-on.

### What exactly does Eplan do?

At any start of Eplan, the registry or the path for server add-ons is scanned for new add-ons. The  install.xml  is read and the following things are done:

- Does this add-on fit to the main version?
- Is the correct license option booked?
- Is the version correct?

When everything is done so far, Eplan then registers the new add-on:

- All  \*.xml  files from the  CFG  folder are read. The settings are copied to the settings of the main version.
- The  eplset<applicationmodifer>.xml  is read: All binaries defined there are loaded now.
- The API modules are loaded.
- The API references are registered.
- The scripts are registered.
- The base data of the add-on is copied to the base data of Eplan.

### Possible issues and troubleshooting

**Using an assembly in different versions**  
Conflicts can arise when multiple add-on projects in a solution refer to an assembly with a namespace and class of the same name, but different versions. The following scenario illustrates the problem:  
Let's assume that you use the  Write  library of version 1.0.0 in one project (Project1) and the  Write  library of version 2.0.0 in the other project (Project2). This will lead to unwanted behavior in your solution: Depending on which project ' be it Project1 or Project2 ' you call first, it will be executed correctly and will reference the correct library. If you then execute the other project, it will reference the previous library, the first version is executed.

**Solution**: To work around this behavior, sign the library versions independently of each other. You can then use the library with different versions at will. Signing gives the library a specific key token or "strong name" that helps distinguish the libraries.
