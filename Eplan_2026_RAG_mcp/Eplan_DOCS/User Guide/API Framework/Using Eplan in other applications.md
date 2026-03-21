# Using Eplan in other applications

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/EplanInOtherApplications.html

---

This topic describes various options for using Eplan functions outside of  a script or an Eplan add-in.

Basically, there are three options to use Eplan functionality in other applications:

1. Calling Eplan with [command line parameters](Command line parameters.html)
2. Using parts of Eplan (modules/DLLs) in other processes. Only the functionality of Eplan is used; no main frame and - with some exceptions - no dialogs of Eplan will be shown.
3. Eplan runs as a separate process and functions, objects in this process are called by another process. (ActiveX automation, out-of-process server, EXE server) In this case, Eplan can be visible or invisible.

If you want to use the Eplan API together with office applications (e.g. Excel), you should consider the following order of choice when planning your code architecture:

1. Create an Eplan add-in and use the other application as managed code via COM interop.
2. Use Visual Studio Tools for Office (VSTO) together with managed Eplan API assemblies. (Eplan is in-process server or remoting client).