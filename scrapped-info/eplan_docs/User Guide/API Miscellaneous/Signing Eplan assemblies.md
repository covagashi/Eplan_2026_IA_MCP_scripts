# Signing Eplan assemblies

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Signing_EPLAN_assembies.html

---

As a part of your EADN (Eplan API Developer Network) partnership with Eplan GmbH & Co. KG, you get the opportunity to sign your software interface with our products. This allows you (or your customer) to use the API assembly without having an Eplan API developer license on his workstations. Instead, he receives ' through you ' a runtime license for an API interface.

This chapter describes how you (or your developers) should proceed, to get properly signed EADN modules.

## **What is possible with API licenses?**

At first there should be clarified why signing is necessary. There are 2 kinds of API licenses:

**a)** **API developer license** ' It should be used only for development and testing of an API interface. Normally it has a limitation of a maximum size of Eplan projects to 5 pages. Only unsigned API programs can be loaded using it.

**b)** **API runtime license** ' In this case there can be used only signed API programs, so we need to sign it. The routine how to do it is described bellow.

A user can check available licenses and select one by starting Eplan with shift key (then the Select license dialog will appear). When Eplan is already running, the current license can be retrieved from:

**a)** the About Eplan dialog

**b)** in the API using the  EplApplication.License  property and the  License  class.

## **The Concept of EADN / API Runtime signing**

EADN / API Runtime signing uses a concept of combining standard .NET strong-naming with additionally including an Eplan license option to the software.  
To achieve this combination, please follow the instructions in this chapter.

## **Requirements**

After you have concluded your EADN contract or purchased an API Runtime license and you created a new software interface with Eplan, the main administrator of your Eplan cloud organization will get informed about a new entitlement for using the cloud-based EADN Signing service. Additionally, you will receive a file containing the public part of a standard signature key, normally used for strong-naming a .NET assembly. We created this key especially for your software.

For using the Eplan-Cloud based signing service, you have to be member of the regarding organization and got assigned the role **User** to the application **EADN Singing**:

### Check available licenses inside active organization

Public pre-signing keyfiles (e.g.  1234\_public.snk, refer to [*Delay sign the assemblies*](#anchorDelaySignTheAssemblies)) that are used inside a Visual Studio project must match the used Eplan Cloud organization.  
To verify which pre-signing keyfiles can get used inside the active Eplan Cloud organization, authorize (refer to [*Authorize manual usage of EADN-Signing*](#anchorAuthorizeManualUsage)) and use the endpoint GET /licenses  and check the result.

1. Click on endpoint GET /licenses   
   ' Section gets expanded and shows more details
2. Click on Try out
3. Click on Execute
4. Check Response of server in section Code

The above example shows property  optionId  with the value **1234**, which means assemblies with the used pre-signing keyfile  1234\_public.snk  would be allowed to get signed inside the active Eplan Cloud organization.

Example of response if no pre-signing key is assigned to the current organization ' organization not allowed to sign assemblies.

**Notice:**  
In case no valid license (optionId) is shown, please use [Eplan Global Support Portal](https://www.eplan.de/services/eplan-global-support/) for getting help.

## **How to proceed**

Take the following steps to get your application EADN / API Runtime signed:

### Modify the AssemblyInfo

In your software projects, you need to add an additional attribute to your  AssemblyInfo  files of all the assemblies that are referencing Eplan API Assemblies. The  EplanSignedAssemblyAttribute  is implemented in the  Eplan.EplApi.Starter.dll, which you always have to reference in your API application. The following example shows how to use the attribute in your  AssemblyInfo  file:

```csharp
using System.Reflection;
 using System.Runtime.CompilerServices;
 using System.Runtime.InteropServices;
 using Eplan.EplApi.Starter;
 //..
 [assembly: EplanSignedAssemblyAttribute(true)]
```

**Important:**  
Eplan checks the signature for **all DLLs and exe files that directly or indirectly use Eplan API functions**. Therefore, please ensure to add the  EplanSignedAssembly  attribute in the  AssemblyInfo.cs  files of every DLL and exe file using Eplan API functionality directly or indirectly.

### Delay sign the assemblies

The easiest way for delay signing your assemblies (DLL  or  exe) is entering the public key file in the signing properties of your software projects in Visual Studio. Check Sign the assembly and activate the Delay sign only flag. See the following image:

The delay signing is done, when building the software project and with it creating the assembly.

Alternatively, you can use Microsoft's Assembly Linker  Al.exe  to manually delay sign assemblies. Please refer to respective MSDN documentation.

### Upload files manually

Log in to the Eplan Cloud Developer Portal [https://developer.eplan.com](https://developer.eplan.com/).

**Notice:**  
An Eplan Cloud account is required to access the Developer Portal.

**Notice:**  
Manual signing via the Developer Portal is intended only for testing. The main purpose of the service is **automatic signing** (refer directly to [*Fully automated signing process*](#anchorFullyAutomatedSigning)).

### Authorize manual usage of EADN-Signing

1. Select **EADN-Signing** in available list of APIs
2. Click on **Authorize**  
     ' The authorization dialog opens
3. Click the drop-down list and select **EADN Signing**
4. Click on **Authorize**  
     ' The API is allowed for manual usage via **Try it out** feature
5. Click on **Close**  
     ' The authorization dialog is closed  
     ' Activated authorization is shown via closed lock symbol 

After successful authorization, the entry USER is displayed as active role:

Example when authorization was **not** successful:

**Tip:**  
In case no valid role USER is shown, please refer to *[Requirements](#anchorRequirements)* or contact the administrator of your Eplan Cloud organization. Same method can get used to verify, if a PAT is (still) valid. Just use the authorization method PAT instead of Interactive (OAuth2, x-delegation).

**Notice:**  
When a different API is selected in the list of available APIs, an active authorization is discarded. Repeat the above steps to perform an authorization again.

### Upload pre-signed assemblies / executables

1. Click on endpoint **POST /assemblies**  
     ' Section gets expanded and show more details
2. Click on **Try it out**  
     ' Enables value entry in the **Request Body** section
3. Click on **Add file item**  
     ' Adds a new **Choose file** row
4. Click on **Choose file**  
     ' File selection dialog opens  
     ' Select pre-signed assembly  
     ' Confirm with **Open** to add local file for upload  
     ' Repeat steps 3 and 4 for each file which needs to get signed
5. (Optional) Add personal Comment for full upload-job  
     ' The authorization dialog is closed
6. Click on **Execute**  
     ' All selected files will get uploaded and tried to get signed
7. Check Response of server in column **Code**
8. Select and copy value of **ID** in **Response body**, for later usage of all files

### Check status of uploaded files

Log in to the Eplan Cloud Developer Portal [https://developer.eplan.com](https://developer.eplan.com/).  
If required, perform *[Authorize manual usage of EADN-Signing](#anchorAuthorizeManualUsage)*.  
Make sure you have the **ID** of the desired upload process handy (see also [*Select and copy value of **ID** in **Response body***](#anchor1)).

**Notice:**  
Use the endpoint **GET /assemblies** to return a list of all existing uploaded packages inside your organization and determine the required ID.

1. Click on endpoint **GET /assemblies/{id}/status**  
     ' Section gets expanded and show more details
2. Click on **Try it out**  
     ' Enables value entry in the **Parameters** section
3. Insert previous copied ID into parameter **Id of the uploaded package**
4. Click on **Execute**  
     ' Details about given signing job are getting returned
5. Check response of server in section **Responses** and get details about results of signing process

### Receive the signed Assemblies manually

Log in to the Eplan Cloud Developer Portal [https://developer.eplan.com](https://developer.eplan.com/).  
If required, perform *[Authorize manual usage of EADN-Signing](#anchorAuthorizeManualUsage)*.  
Make sure you have the **ID** of the desired upload process handy (see also [*Select and copy value of **ID** in **Response body***](#anchor1)).

**Notice:**  
Use the endpoint **GET /assemblies** to return a list of all existing uploaded packages inside your organization and determine the required ID.

1. Click on endpoint **GET /assemblies/{id}**  
     ' Section gets expanded and show more details
2. Click on **Try it out**  
     ' Enables value entry in the **Parameters** section
3. Insert previous copied ID into parameter **Id of the uploaded package**
4. Click on **Execute**  
     ' Download request is getting executed
5. Click on **Download file** in section **Responses**  
     ' **Save file** selection dialog opens  
     ' Confirm with **Save** to download the file

### Delete uploaded files manually

Log in to the Eplan Cloud Developer Portal [https://developer.eplan.com](https://developer.eplan.com/).  
If required, perform *[Authorize manual usage of EADN-Signing](#anchorAuthorizeManualUsage)*.  
(see also [*Limitations*](#anchor3) below)  
Make sure you have the **ID** of the desired upload process handy.  
(see also [*Select and copy value of **ID** in **Response body***](#anchor1))

**Notice:**  
Use the endpoint **GET /assemblies** to return a list of all existing uploaded packages inside your organization and determine the required ID.

1. Click on endpoint **DELETE /assemblies/{id}**  
     ' Section gets expanded and show more details
2. Click on **Try it out**  
     ' Enables value entry in the **Parameters** section
3. Insert previous copied ID into parameter **Id of the uploaded package**
4. Click on **Execute**  
     ' Delete request is getting executed
5. Check result request in column **Code** in section **Responses**

### Fully automated signing process

**Preparations / prerequisites**

To take advantage of fully automated signing of assemblies during the build process of Visual Studio, you must create a personal access token (further called **PAT**) for the application **EADN Signing** inside the profile editor of your Eplan Cloud organization.

See Eplan Cloud help:  
   '¢ [Open My Settings](https://www.eplan.help/en-us/Infoportal/Content/Cloud/Content/htm/Cloud_h_Settings_Open.htm?tocpath=My)  
   '¢ [Add personal access token (PAT)](https://www.eplan.help/en-us/Infoportal/Content/Cloud/Content/htm/Cloud_h_Settings_PAT.htm?tocpath=My settings|Sign-in|Personal access token (PAT)|_____1)  
   '¢ [Roles and permissions](https://www.eplan.help/en-us/Infoportal/Content/Cloud/Content/htm/Cloud_k_RolesRights.htm)

**Notice:**  
Without assigned role **User** to **EADN Service**, no **PAT** creation is available for the user.  
Removing already assigned role **User** from **EADN** **Signing** makes existing PAT invalid.  
No prolonging of already created **PAT** (*new one needed after expiration*)  
E-Mail notification is automatically sent from Eplan Cloud.

Download the provided PowerShell script from the [Developer Portal](https://developer.eplan.com/)  [EADN Singing](https://developer.eplan.com/apis/eadn-signing_v1_0) for using it in Post-build event of Visual Studio.

An example for calling the script including available parameters can be found inside the script itself:

|  | Copy Code |
| --- | --- |
| ``` 
 # Example command line:
 #
 # powershell -ExecutionPolicy Bypass -file "<YourFolderName>\PostBuildScript.ps1"
 ``` | |

**Notice:**  
Depending on your IT guidelines, calling PowerShell scripts without bypassing executions policy may return an error.  
The active policy can get checked via running command  Get-ExecutionPolicy -List

**Tip:**  
See also [Microsoft documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2).

### Parameter description

| Parameter name | Mandatory | Description |
| --- | --- | --- |
| baseUrl | No | Only for signing in Chinese environment; use parameter value\*:  <https://api.eplan.com.cn/eadn-signing/v1.0> |
| comment | No | Comment for complete upload job |
| accessToken | Yes | PAT which was created in User profile |
| assemblies | Yes | Filename(s) of assemblies / executables which have to get signed |
| destinationPath | Yes | Local target folder for downloading result-package (*via PowerShell script target directory is tried to get created if missing*) |
| deleteAfterwards | No | Delete upload-job after tried signing automatically (*Note: storage quota limitations*) |

\**current baseUrl can be viewed at any time in the [Developer Portal](https://developer.eplan.com)*

### Examples for all countries except China

**Example:**  
Command line call for signing **a single file (not China!)**  
powershell -ExecutionPolicy Bypass  
-file "<YourFolderName>\PostBuildScript.ps1"  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-assemblies "<SourceFolderWithPreSignedFiles>\$(TargetFileName)"  
-destinationPath "<TargetFolder>"  
-deleteAfterwards

**Example:**  
Command line call for signing **multiple files ' no subfolders** in ZIP result**(not China!)**  
powershell -ExecutionPolicy Bypass  
-file "<YourFolderName>\PostBuildScript.ps1"  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-assemblies "<SourceFolder1>\<YourFile1.dll>,<SourceFolder2>\<YourFile2.dll>"   
-destinationPath "<TargetFolder>"  
-deleteAfterwards

**Example:**  
Command line call for signing **multiple files ' with subfolders** in ZIP result **(not China!)**  
powershell -ExecutionPolicy Bypass  
-file "<YourFolderName>\PostBuildScript.ps1"  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-rootDirectory "<RootSourceFolder>"  
-assemblies "<RelativeFolder1>\<YourFile1.dll>,<RelativeFolder2>\<YourFile2.dll>"   
-destinationPath "<TargetFolder>"  
-deleteAfterwards

This allows, for example, files with the same name to be processed in one signing operation.

### Examples for China only

**Example:**  
Command line call for signing **a single file (China only!)**  
powershell -ExecutionPolicy Bypass  
-file "<YourFolderName>\PostBuildScript.ps1"   
-baseUrl <https://api.eplan.com.cn/eadn-signing/v1.0>  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-assemblies "<SourceFolderWithPreSignedFiles>\$(TargetFileName)"  
-destinationPath "<TargetFolder>"  
-deleteAfterwards

**Example:**  
Command line call for signing **multiple files ' no subfolders** in ZIP result**(China only!)**  
powershell -ExecutionPolicy Bypass  
-file "<YourFolderName>\PostBuildScript.ps1"  
-baseUrl <https://api.eplan.com.cn/eadn-signing/v1.0>  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-assemblies "<SourceFolder1>\<YourFile1.dll>,<SourceFolder2>\<YourFile2.dll>"  
-destinationPath "<TargetFolder>"  
-deleteAfterwards

**Example:**  
Command line call for signing **multiple files ' with subfolders** in ZIP result**(China only!)**  
powershell -ExecutionPolicy Bypass -file "<YourFolderName>\PostBuildScript.ps1"  
-baseUrl <https://api.eplan.com.cn/eadn-signing/v1.0>  
-comment "This is a test comment from $(USERNAME)"  
-accessToken "<YourPATforEADNSigningService>"  
-rootDirectory "<RootSourceFolder>"  
-assemblies "<RelativeFolder1>\<YourFile1.dll>,<RelativeFolder2>\<YourFile2.dll>"  
-destinationPath "<TargetFolder>"  
-deleteAfterwards

### Adopt command line for PostBuild-event in Visual Studio

1. Click on **Build events**  
     ' Pre- and Post-build details of Visual Studio are shown
2. Click on **Edit Post-build'¦**  
     ' Post-build Event Command Line dialog opens
3. Paste required command line call
4. Click on **OK**  
     ' Post-build Command Line dialog is closed

Output console will show details after building:

All files (no matter if singing process was successful or not) will get extracted to the given folder in the  destinationPath  parameter.

### Limitations

  '¢ The filenames in one upload have to be unique. Adding the same filename multiple times (on the same folder level) is not allowed, because it can not be reflected in the ZIP-file for download.  
  
  '¢ Each upload job can have a max. total file size of ~40 MB  
  
  '¢ There is an upload limit of max. 9999 kept upload jobs for each organization.  
  
  '¢ No automatic 'cleanup' is done in organization storage.  
  
  '¢ If upload limit is reached, older uploaded files have to get deleted before new uploads are possible.

**Tip:**  
It is recommended to delete uploaded files directly after signing (no matter if signing was successful or not), to avoid reaching the upload limit at all.

**Notice:**  
Further details can be also found in the Developer Portal: [ProblemTypes of EADN signing](https://developer.eplan.com/problemtypes/eadn-signing)

## **Special cases**

### How to sign automatically generated serialization DLLs

If you use an automatically created serialization DLL for your classes, you need to delay-sign them via the  sgen.exe  tool. This tool can be found the SDK directory of your development environment.

**Example:**  
"C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\bin\sgen.exe" /compiler:/delaysign+ /assembly:"MyDllToBeSerialized.dll" /proxytypes  
/reference:"Eplan.EplApi.AFu.dll" /reference:<'¦all further references you need> /compiler:/keyfile:"D:\MyPublicKey.snk"

### Signing of your own COM interop DLLs

As you probably know, any strong-named .NET assembly can only reference / load other strong-named assemblies. In case your application registers COM DLLs, the development environment normally automatically creates so-called interop DLLs, which contain the .NET wrapping of the respective COM methods. Normally, these DLLs are not signed. To create these assemblies in an already delay-signed way Microsoft provides the command line tool tlbimp.exe ' also to be found in the SDK directory of your development environment. See the following example, how it is used:

**Example:**  
"C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\Bin\tlbimp.exe" yourComInterface.dll /delaysign /publickey:C:\YourKeyFilePublic.snk /out:Interop.yourComInterface.dll

## **What to do in case of problems**

If you encounter issues with the signing process, please contact the [Eplan Global Support Portal](https://www.eplan.de/services/eplan-global-support/).