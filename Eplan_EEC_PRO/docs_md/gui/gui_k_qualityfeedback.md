---
title: "Create Eplan support request"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/gui_k_qualityfeedback.htm"
file: "gui_k_qualityfeedback"
category: "gui"
---

# Create Eplan support request

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create Eplan support request Even with careful testing prior to shipping, programming errors can never be ruled out entirely. Fixing such an exception error requires your assistance. Depending on the respective license, the data recorded with the Eplan support request wizard and a description which is required for reproduction and rectification of the error is sent to the e-mail address [support@eplan.de](mailto:support@eplan.de) or to an e-mail address that is stored in the model variables under Eplan support request > E-mail address deviating from the Eplan support for the Eplan support request.
     * Model variable without specification or a developer license is active: Eplan support request is sent to the e-mail address [support@eplan.de](mailto:support@eplan.de).
     * License Config: Eplan support request is sent to the e-mail address that is stored in the model variable E-mail address deviating from the Eplan support.
The following data can be attached to the Eplan support request:
     * The complete model. Please take into account the maximum file size that is possible as an attachment of an e-mail. This option is enabled by default.
     * Discipline resources. This option is required if resources are not managed internally in the model (see [Resources and their management](eecbase_k_resources_and_their_management.htm)). The resource files are only attached if the global path to the resources is specified (see [de.eplan.eec.global.resourcePath](admin_r_vmargs_global_resourcePath_new.htm)). This option is enabled by default.
     * Content of the \dropins folder. With this option plugins located in the /dropins folder are attached. This option is enabled by default.
     * Database queries. In order to reproduce errors better, there is an option to record database queries. It is recorded which query was sent to which database and which reply the database provided. This way, it is possible to trace the communication with databases, without having the content of all databases available. The recording of database queries has to be activated in the settings under Disciplines > Data sources. The evaluation of such records is basically only possible by Support.
