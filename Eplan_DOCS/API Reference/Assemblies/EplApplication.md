# EplApplication

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication.html

---

This class allows you to use Eplan functions in other processes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.System.EplApplication**

Syntax

**C#**



public class EplApplication

public ref class EplApplication


Remarks

External applications can use Eplan functions by generating an instance of this class and calling the [Init(String)](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Init(String).html) function.

Example

This example initializes and closes Eplan.

**C#**

```
namespace Eplan.Api.Offline

{

    public partial class MainDialog : Form

    {

        //EPLAN application object

        private EplApplication m_oEplApp = new EplApplication();

        //Flag to determine if initialization has already been done

        private bool m_bIsP8AlreadyInitialized = false;

        //Path to EPLAN product variant bin folder

        private string m_strEplanBinFolder = "";

        public MainDialog(String strEplanBinFolder)

        {

            //Remember path to EPLAN product variant bin folder

            m_strEplanBinFolder = strEplanBinFolder;

            //Initialize dialog components

            InitializeComponent();

        }

        //Method for handling event which fires on clicking a control.

        private void btnStart_Click(object sender, System.EventArgs e)

        {

            EPLInit();

        }

        //Method for handling event which fires when closing a form. 

        private void mainDialog_Closing(object sender, System.ComponentModel.CancelEventArgs e)

        {

            EPLExit();

        }

        //Method for initializing EPLAN

        private void EPLInit()

        {

            try

            {

                if (!m_bIsP8AlreadyInitialized)

                {

                    if (!String.IsNullOrEmpty(m_strEplanBinFolder))

                    {

                        m_oEplApp.EplanBinFolder = m_strEplanBinFolder;

                    }

                    m_oEplApp.Init("");

                    m_bIsP8AlreadyInitialized = true;

                }

            }

            catch (Exception)

            {

                //ToDo add an exception handling code here

            }

        }

        //Method for deinitialization EPLAN

        private void EPLExit()

        {

            try

            {

                if (m_bIsP8AlreadyInitialized)

                {

                    m_oEplApp.Exit();

                    m_bIsP8AlreadyInitialized = false;

                }

            }

            catch (Exception)

            {

                //ToDo add an exception handling code here

            }

        }

    };

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplApplication Constructor](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~_ctor.html) | Creates a new application class for Eplan |



Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Fieldstatic (Shared in Visual Basic) | [LicenseRuntimeCheckEvent](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~LicenseRuntimeCheckEvent.html) | License runtime check callback event |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [EplanBinFolder](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~EplanBinFolder.html) | Eplan product variant bin path. Path to the w3u.exe of the product variant you want to start. Setting this path is necessary to specify the variant to start for your offline application. |
| Public Propertystatic (Shared in Visual Basic) | [InOfflineMode](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~InOfflineMode.html) | When the P8 version is started offline, no P8 mainframe is available. Then this function returns TRUE. |
| Public Property | [License](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~License.html) | Gets application's license variant as string. |
| Public Property | [LicenseFile](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~LicenseFile.html) | Name of the File (inclusive path) containing the license to use or to borrow IMPORTANT: Set this path before calling Init! |
| Public Property | [Password](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Password.html) | Set user password |
| Public Property | [QuietMode](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~QuietMode.html) | Quiet mode in which Eplan P8 has been started. |
| Public Property | [SystemConfiguration](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~SystemConfiguration.html) | System configuration scheme name. |
| Public Property | [User](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~User.html) | Set user name |
| Public Property | [Variant](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Variant.html) | Gets application's variant as string (Basic, Trial, Developer, etc.). |
| Public Property | [Version](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Version.html) | Gets version from the application. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Exit](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Exit.html) | Exits the Eplan runtime system. |
| Public Method | [Init](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~Init.html) | Overloaded. Initializes the Eplan runtime system. |
| Public Method | [InitGuiLanguage](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~InitGuiLanguage.html) | Sets application's GUI language. Used before calling Init method. |
| Public Method | [OpenProjectDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~OpenProjectDlg.html) | Displays the Eplan Open project dialog and opens the selected project. |
| Public Method | [ResetQuietMode](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ResetQuietMode.html) | When a mainframe is set for API offline programs some dialogs which are normally hidden in API add-ins are shown. Calling this method will automatically hide them like in add-ins. |
| Public Method | [SetMainFrame](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~SetMainFrame.html) | Sets a new Mainframe for API offline program. API offline program will show all dialogs which are normally hidden in add-ins. It is possible to hide such dialogs using [ResetQuietMode](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ResetQuietMode.html) method. |
| Public Method | [ShowApiAddInDialog](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowApiAddInDialog.html) | Displays the Eplan API add-ins dialog. |
| Public Method | [ShowPartSelectionDialog](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowPartSelectionDialog.html) | Overloaded. Selects parts from the current parts database |
| Public Method | [ShowSettingDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowSettingDlg.html) | Displays the Eplan settings dialog. |
| Public Method | [ShowSystemErrorDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowSystemErrorDlg.html) | Displays the Eplan System error messages dialog. |


