# Add-ins

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/AddIns.html

---

Eplan has a modular architecture. It is possible to add functionality to Eplan and to change existing functionality.

These different means to modify the system are implemented in modules, which can be loaded by Eplan, so-called add-ins. So if you want to add functionality to Eplan, you first need to create an add-in.

You can enhance existing functionality for example by:

- Adding new GUI items, such as ribbon buttons
- Adding new actions, verifications, interactions, messages, XML processors
- Handling Eplan events and raising ones

An add-in is an assembly, written in one of the .NET Framework programming languages. There are different ways to create such an assembly. Basically, you just need a simple text editor and the compiler provided by the .NET Framework. The rather more convenient way to create an add-in is by using an integrated development environment (IDE), like Visual Studio.

### Remarks

Add-in assemblies should be named like  <YourCompanyName>.EplAddin.<NameOfTheProject>.dll.   
The add-in and all its references should be stored in a separate folder.
