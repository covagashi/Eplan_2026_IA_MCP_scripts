---
title: "Importing EOX files for SIMATIC STEP 7"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task1_preparation_import.htm"
file: "tutstep7_h_task1_preparation_import"
category: "tutstep7"
---

# Importing EOX files for SIMATIC STEP 7

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Importing EOX files for SIMATIC STEP 7 Requirement:  
     * The file <EEC installation folder>\install\Tutorial\Step7\Tutorial_Step7.zip is unzipped in the same folder.
     * EEC is started.
Based on the initial situation, various EOX files that contain the corresponding libraries must be imported.
    1. The model is empty, i.e., only the system libraries are available (also see [Filter](eecbase_k_filter.htm)).
Import the following EOX files:
    
        <EEC-Installationsordner>\install\Tutorial\Mechatronic\Mechatronic.eox
    <EEC-Installationsordner>\install\Tutorial\Step7\Step7_Ui.eox
    <EEC-Installationsordner>\install\Tutorial\Step7\Step7_IOGenerator_Ui.eox

    1. The model contains T_Mechatronic_Architecture and T_Mechatronic_ModularSystem.
Import the following EOX files:
    
        <EEC-Installationsordner>\install\Tutorial\Step7\Step7_Ui.eox
    <EEC-Installationsordner>\install\Tutorial\Step7\Step7_IOGenerator_Ui.eox

Read more
     * [Importing libraries/projects as an EOX file](eecbase_k_eox_exchange_library_import.htm)
