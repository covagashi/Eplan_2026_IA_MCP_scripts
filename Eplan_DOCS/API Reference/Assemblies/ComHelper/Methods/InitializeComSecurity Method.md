# InitializeComSecurity Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.ComHelper~InitializeComSecurity.html

---

initialize the DCOM security which needed to connect to license manager (ELM).

Syntax

**C#**



public void InitializeComSecurity()

public:

void InitializeComSecurity();


Remarks

sample: static class Program { //The main entry point for the application. [STAThread] static void Main() { Eplan.EplApi.Starter.ComHelper cHelper; cHelper.InitializeComSecurity(); .. .. Application.Run(....); }
