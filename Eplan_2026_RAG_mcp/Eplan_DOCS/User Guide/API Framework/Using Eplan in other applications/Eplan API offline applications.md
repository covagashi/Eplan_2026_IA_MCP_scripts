# Eplan API offline applications

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/UsingEplanAssemblies.html

---

The easiest way to use Eplan API objects in your program is to directly use the functionally of the API DLLs in your code. It is even easier, if your program is a .NET application: You just reference the managed Eplan API assemblies in your project. This type of application, we call an "**offline application**".

Then ' in the appropriate place (e.g. in the main form) ' you create an instance of the  Eplan.EplApi.System.EplApplication  class and initialize it:

**C#**
```csharp
private Eplan.EplApi.System.EplApplication m_oEplApp;

public MainForm()

{

   //

   // Required for Windows Form Designer support

   //

   InitializeComponent();

   m_oEplApp = new Eplan.EplApi.System.EplApplication();

   System.String strAppModifier="";

   m_oEplApp.Init(strAppModifier);

}

Private m_oEplApp As Eplan.EplApi.System.EplApplication

   InitializeComponent()

   m_oEplApp = New Eplan.EplApi.System.EplApplication()

   m_oEplApp.Init(strAppModifier)
```

The string parameter  strAppModifier  determines, which configuration file is used and thus which modules will be loaded. If you pass an empty string like in the above example, the  eplset.xml  of the standard version of the current user will be loaded.

After executing the  Init()  function, all functions / objects of the Eplan API are available, with the exception of those that expose GUI functionality such as modal dialogs, docked dialogs or MDI windows. The API classes and methods, etc. are then used in the same way as if programming a normal Eplan add-in. A few selected modal dialogs of Eplan are provided by special methods of classes in  Eplan.EplApi.System.EplApplication.

When you no longer need the Eplan API in your program, you should call the  Exit()  function of your  EplApplication  object to unload the API.

### Usage with Windows Forms

In case of an offline application using Windows Forms, it is possible that the application changes its size after  EplApplication::Init. It happens if the font size in OS is set to other than 100%, which happens quite often in case of large monitors. Because of this, please set DPI awarness in  .config  file of the application, in order to avoid rescaling:

|  | Copy Code |
| --- | --- |
| ``` 
 <System.Windows.Forms.ApplicationConfigurationSection>
      <add key="DpiAwareness" value="PerMonitorV2" />
 </System.Windows.Forms.ApplicationConfigurationSection>
 ``` | |

Also, please assure your  .manifest  file is Windows 10 compatible:

|  | Copy Code |
| --- | --- |
| ``` 
 <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
   <application>
     <!-- Windows 10 compatibility -->
     <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}" />
   </application>
 </compatibility>
 ``` | |

### How to make sure, that the API assemblies are directly loaded from the Eplan platform BIN folder?

As briefly mentioned in the topic "[Eplan .NET API](EplanApiDotNet.html)", a path must be set to the  <Eplan main path>\Platform\<version>\BIN  folder. More precisely, you need to make sure to load the Eplan API assemblies from exactly this folder. The reason for this is, that the API assemblies have statically linked unmanaged dependencies, which need to be loaded directly from the current directory.

This is also the reason why it generally does not work to register the Eplan API DLLs in  GAC. The directory from which the references of your Visual Studio project are added has no influence on where the DLLs are actually loaded from.

You can make sure, the API assemblies are loaded from the correct  BIN  directory by different means:

1. This is the easiest way: You can just copy the executable of your offline application to the  <Eplan main path>\Platform\<version>\BIN  folder.
2. Use Eplan API offline wizard. Then your assemblies will be bound to the correct Eplan variant by means of the  Eplan.EplApi.Starter  library:

```csharp
// Use the finder to find the correct Eplan version if not yet known
 EplanFinder oEplanFinder = new EplanFinder();
 String strBinPath = oEplanFinder.SelectEplanVersion(true);
 
 // Check if the user has selected any Eplan variant (Electric P8, etc.)
 if (String.IsNullOrEmpty(strBinPath))
     return;
 
 // Use the AssemblyResolver to let the program know where all Eplan variants can be found.
 AssemblyResolver oResolver = new AssemblyResolver();
 oResolver.SetEplanBinPath(strBinPath);
 
 // Now pin to Eplan. This way all referenced Eplan assemblies are loaded from the platform BIN path.
 oResolver.PinToEplan();
 
 // Use a separate class to initialize EplApplication. Pass the path to the Eplan product variant BIN directory in order to set the EplApplication.EplanBinFolder property
 Form1 oForm = new Form1();
 oForm.EplanBinFolder = oResolver.GetEplanBinPath();
 Application.Run(oForm);
```

3. Publish the codebases of all needed API assemblies in the application  config  file. (An XML file, which is named like your executable with an additional extension  .config, e.g. "MyApplication.exe.config"). The following code shows an example for the contents of such a config file.

| XML | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0"?>
 <configuration>
   <runtime>
     <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.Systemu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.Systemu.dll" />
       </dependentAssembly>
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.AFu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.AFu.dll" />
       </dependentAssembly>
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.Baseu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.Baseu.dll" />
       </dependentAssembly>
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.DataModelu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.DataModelu.dll" />
       </dependentAssembly>
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.HEServicesu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.HEServicesu.dll" />
       </dependentAssembly>
       <dependentAssembly>
         <assemblyIdentity name="Eplan.EplApi.EServicesu" publicKeyToken="57aaa27e22f7b107" />
         <publisherPolicy apply="yes" />
         <codeBase version="1.0.0.0" href="file:///C:\Program Files\EPLAN\Platform\2.2.0\Bin\Eplan.EplApi.EServicesu.dll" />
       </dependentAssembly>
     </assemblyBinding>
   </runtime>
 </configuration>
 ``` | |

> 4. Last but not least, you can implement an  AssemblyResolve  event handler in your offline application, where you explicitly load the assemblies you are looking for. You will also need to set the current directory of the application to the respective  BIN  directory. The following code shows an example for this:

```csharp
[STAThread]
         static void Main()
         {
             Application.EnableVisualStyles();
             Application.SetCompatibleTextRenderingDefault(false);
             Environment.CurrentDirectory = @"C:\program files\EPLAN\platform\x.x.x\BIN\"; // x.x.x = your desired Eplan version
             AppDomain appDomain = AppDomain.CurrentDomain;
             appDomain.AssemblyResolve += new ResolveEventHandler(MyResolveEventHandler);
 
             Application.Run(new Form1());
         }
         static Assembly MyResolveEventHandler(object sender, ResolveEventArgs args)
         {
             Console.WriteLine("Resolving...");
             string sAssemblyName = args.Name.Split(',')[0];
             Assembly ass = Assembly.LoadFile(@"C:\program files\EPLAN\platform\x.x.x\BIN\" + sAssemblyName + ".dll");
             return ass ;
         }
     }
```

In Visual Studio Tools for Office (**VSTO**) projects, the assembly resolver or the application  config  file is not working. Office still tries to copy the Eplan API assemblies to a temporary folder before loading. VSTO applications will only work, if you set the codebases of the API assemblies in the  machine.config  file, which is usually located in the  C:\WINDOWS\Microsoft.NET\Framework\v4.0.30319\CONFIG  directory.

### Remarks

If you want to use any object from the namespaces beginning with  Eplan.EplApi.DataModel, you need to open a LockingStep, before you e.g. open an Eplan project.

Make sure to call  Exit()  only one time in your application. It is currently not possible to use  Init("")  after  Exit(), while the application is still running.

The  EplApplication  instance should be explicitly de-initialized by the main thread. If the  <c>Exit</c>  method is called by the garbage collector thread or after leaving the main function of the application, it will cause the application to crash.