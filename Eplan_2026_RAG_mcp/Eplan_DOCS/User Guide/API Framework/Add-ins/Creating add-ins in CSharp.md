# Creating add-ins in CSharp

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/CSharpAddins.html

---

This section shows how to create an Eplan add-in in C#. In order to show that the installation of the .NET Framework already provides all the necessary tools (C-Sharp compiler, etc.), the add-in is not created as a Visual Studio project, but simply using a text editor and the command line tools of the .NET Framework.

### a) Getting started:

First, it is useful to create a directory to store the source code for your add-in. For this example we create a folder named "SimpleCSharpAddIn".

Now start your text editor of choice, e.g. notepad, and start writing the source code.

### b) Creating the module class:

Every Eplan add-in, including the C# add-in we are going to create, requires a certain class for managing the add-in. This class must implement the functions declared by the  IEplAddIn  interface:

```csharp
public class AddInModule: Eplan.EplApi.ApplicationFramework.IEplAddIn
        {
             public bool OnRegister(ref System.Boolean bLoadOnStart)
             {
                   bLoadOnStart=true;
                   return true;
              }
             public bool OnUnregister()
             {
                   return true;
             }
             public bool OnInit()
             {
                   return true;
             }
             public bool OnInitGui()
             {
                   return true;
             }
             public bool OnExit()
             {
                   return true;
             }
       }
```

Now save this source code in the folder "SimpleCSharpAddIn" as a file named "AddInModule.cs".

### c) Compiling the assembly (DLL)

Now it is time to use the C-Sharp compiler. The compiler is located in the directory of the .NET Framework, for example  C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727. This folder should be in the search path. Open your favorite shell and change to the "SimpleCSharpAddInwhere" directory where you just saved "AddInModul.cs".

Run the C-Sharp compiler (csc.exe) with the following parameters:

csc /target:library /reference:..\..\..\..\bin\Eplan.EplApi.AFu.dll /out: Eplan.EplAddin.SimpleCSharp.dll AddinModule.cs 

What is the meaning of these parameters?

1. /taget:library:  We want to create a DLL and no  exe  file.
2. /reference:..\..\..\..\bin\Eplan.EplApi.AFu.dll:  Search in  Eplan.EplApi.AFu.dll  for all missing data (e.g.  IEplAddIn)
3. /out: Eplan.EplAddin.SimpleCSharp.dll:  Name of the DLL to build is "Eplan.EplAddin.SimpleCSharp.dll"
4. AddinModul.cs:  Name of the source file to compile

If nothing went wrong with the compilation, you'll now find the DLL "Eplan.EplAddin.SimpleCSharp.dll" in the folder "SimpleCSharpAddIn". Copy this file to the Eplan platform  bin  folder.

### d) Loading an add-in in Eplan

Now start Eplan. If the following system extensions are loaded in Eplan (which should normally be the case):  EplanEplApiModuleu.erx,  EplanEplApiModuleGUIu.erx.   
Click on the ribbon File > Extras > Interfaces. > API > Manage.

After clicking on Manage, a dialog ' as shown below ' will appear. After pressing the button Load, you can select "Eplan.EplAddin.SimpleCSharp.dll" from the  bin  directory.

Our add-in now appears in the list of the API modules dialog and will be loaded when Eplan is started.That is about all it can do. What we need now is an action!

### e) Adding an Action to the C-Sharp add-in

Therefore, create a second source file and save it as "SimpleCSharpAction.cs" in your source directory. To create an action, we need a class that implements the  IEplAction  interface. For a more detailed explanation, see the "[Actions](Actions.html)" topic.

```csharp
using Eplan.EplApi.ApplicationFramework;
 public class CSharpAction: IEplAction
 {
       public bool Execute(ActionCallingContext ctx )
       {
             new Decider().Decide(EnumDecisionType.eOkDecision, "CSharpAction was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
             return true;
       }
       public bool OnRegister(ref string Name, ref int Ordinal)
       {       
             return true;
       }
       public  void GetActionProperties(ref ActionProperties actionProperties)
       {                  
       }
 }
```

Now the compiler call needs to be slightly extended:

csc /target:library /reference:..\..\..\..\bin\Eplan.EplApi.AFu.dll /reference:..\..\..\..\bin\Eplan.EplApi.Baseu.dll /out:SimpleCSharpAddIn.dll AddinModule.cs SimpleCSharpAction.cs 

If you added an action to an already loaded add-in, the add-in needs to be unloaded and loaded again for the changes to take effect.

So you just open the API modules dialog again, select the add-in in the list and click the Unload button. Then load the add-in again.

Now, you can call your new action in Eplan via a command line call:

W3u.exe CSharpAction 

When you start the action, the  Execute()  function of the  CSharpAction  is called. This function just shows a message box with the text "CSharpAction was called!". (new Decider().Decide(EnumDecisionType.eOkDecision, "CSharpAction was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);).

### Remarks

Please mind that users may start Eplan in QUIET mode using  W3u.exe /Quiet  or the API could be initialized by an [offline program](UsingEplanAssemblies.html). Because of this, it is not recommended to show any message boxes in the methods of the  IEplAddIn  interface. If you encounter some problem during registering or initializing an add-in, just create and throw a  BaseException  or use  BaseException.FixMessage(...)  to add the message to the system messages list.
