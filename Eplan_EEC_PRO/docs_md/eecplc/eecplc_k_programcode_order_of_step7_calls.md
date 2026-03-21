---
title: "Sequence of calls for STEP 7"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_programcode_order_of_step7_calls.htm"
file: "eecplc_k_programcode_order_of_step7_calls"
category: "eecplc"
---

# Sequence of calls for STEP 7

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Sequence of calls for STEP 7

The following diagram provides an example of a dependency structure for PLC function blocks.

In the STEP 7 structure of the EEC model, calls are modeled via the hierarchy of the PLC components. In STEP 7 code, there are calls to the error handler. EEC cannot identify these calls automatically, because with SIMATIC controls the call takes place indirectly via the assignment list. It is nevertheless important that the Error handler function block be translated before FBAxis and ST07Transfer (compiling sequence).

The calls implemented in STEP 7 code must therefore be modeled in EEC via the Called POEs editor page (POE = Program Organization Entity, e.g. FB, FC, etc.), so that EEC can create the STEP 7 project in such a way as to ensure that the compiling sequence is correct.

The following diagram indicates the model for calls to the error-handler. Each function block that calls the error handler registers the handler as a called POE.

Modeling effort can be reduced by registering the error handler only for the OB1.

In this example, the error handler is not compiled until after FBAxis and ST07Transfer, which results in errors when compiling FBAxis and ST07Transfer.

In order to automatically insert the calls implemented in S7 into the compiling sequence with minimum modeling effort, the compiling-sequence parameter is evaluated here as well.

Unlike with the project components, however, no calculation is possible here; the value must therefore be provided as an integer constant.

The following example indicates the steps necessary for setting the Compiling-sequence parameter name model variable:

    1. Select Model > Model variables.
    2. Specify the Compiling-sequence parameter name (for example, CompilerLevel).

For the simplified model, this entails the following procedure:

    3. On the parameter page, insert the parameter for the compiling sequence into the error handler (for example, CompilerLevel).

    4. Specify a value for the CompilerLevel parameter for the Errorhandler (for example, 23).
    5. On the Called POEs editor page, insert the error handler for the OB1.

Called POEs for OB1

The following screenshot displays the result created without (left) and with (right) the compiling-sequence parameter:
