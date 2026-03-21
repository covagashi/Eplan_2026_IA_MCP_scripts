---
title: "Installation of the SAP Java connector"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_h_installation_sap_javaconnector.htm"
file: "admin_h_installation_sap_javaconnector"
category: "admin"
---

# Installation of the SAP Java connector

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Installation of the SAP Java connector

Requirements:

  * EEC 2.4 or higher
  * Installation of the optional function [EEC SAP RFC Add-On](admin_h_installation_optionalfeature_sap.htm)



Because the Java Connector provided free by SAP may not be passed on to third parties due to licensing reasons, the customers must obtain this themselves.

The package is provided for download in the customer area of the SAP Service Marketplace.

Requirement:

An SAP account is required to access the SAP customer area.

Here are the steps to download the SAP Java Connector.

  1. Start Microsoft Internet ExplorerÂ©.
  2. Navigate to SAP Support Portal (service.sap.com/connectors).
  3. Click SAP Java Connector > Tools & Services > Download SAP JCo Release 3.1.
  4. Download the SAP JCo 3.1.x files in accordance with your operating system.



The downloaded files include the file sapjco3.dll. This file has to be unpacked and copied to the following directory:

<EEC installation folder>\plugins\de.eplan.sap_<Build-Nummer>\os\win32\x86_64
