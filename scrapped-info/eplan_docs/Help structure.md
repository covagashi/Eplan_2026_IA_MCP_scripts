# Help structure

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Help structure.html

---

The documentation you are reading is divided into two sections:

**1. User Guide**  
The User Guide section introduces you into how to set up a development environment and start developing or use more advanced functionality.

**2. API Reference**  
The API Reference section lists and describes in detail all the namespaces, classes, methods, etc. of the Eplan API.

API Support setup installs the API Help in HTML and Microsoft Help Viewer format. In this way, it can be accessed online or locally from a disk (i.e. in offline mode).

### API Help formats

In offline mode, API Help can be accessed by the shortcut on a desktop (HTML format) or from Visual Studio (Microsoft Help Viewer).

The later one is the standard help system format used by Visual Studio. It can thus be accessed as another VS help installed locally, i.e. by pressing the [F1] key.

Sometimes the setup cannot correctly register the help correctly in Visual Studio. In this case it can be done manually using the following steps:

a) Start the Microsoft Help Viewer using Help > Add and Remove Help Content from Visual Studio.

b) In the Manage Content tab, please select Disk installation source, then browse for the  helpcontentsetup.msha  file in the directory where the API Help was installed.  
By default it should be in  %ProgramData%\EPLAN\O\_Data\API-Support\<Eplan version>\doc.

c) Select the Add link and press the Update button.

d) Make sure that the help is registered by browsing the Eplan API content in the Microsoft Help Viewer.

e) In order to use the help integrated with Visual Studio, please set the preferred help to the Help Viewer:

Please note that as of Visual Studio 2017, Microsoft Help Viewer is an optional installation component, so it must be additionally added by the Visual Studio Installer.