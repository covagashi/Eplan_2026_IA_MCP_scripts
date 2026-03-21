---
title: "Model-driven configuration"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_model_driven_configuration.htm"
file: "concept_k_model_driven_configuration"
category: "concept"
---

# Model-driven configuration

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Model-driven configuration

As illustrated in the previous section, functional configuration requires that machines and plants be treated in an interdisciplinary manner. However, because project documents are created using different specialized systems, the existing systems have to be integrated so that overarching relationships can be mapped consistently.

The following diagram presents a comparison of alternative approaches to integration.

Most present-day approaches to integration are based on a **bridge solution:** Import/export interfaces are set up between individual systems to create bridges for information flow, thus eliminating manual data transfer. Initial success is often rapidly achieved using this approach. If an attempt is made to expand this initial approach to integration, however, a fundamental problem with the approach becomes clear: When integrating additional systems, more and more bridge solutions to already existing systems have to be set up. This quickly leads to unjustifiably high integration costs.

This problem can be avoided by integrating via a **superordinate system**. Such a system is responsible for the exchange of information between existing systems and facilitates centralized depiction of overarching relationships in functional configuration. Each new system is integrated by means of just a single additional interface.

Functional configuration is therefore based on integration via a superordinate system: EEC.

Specific project documents for the integrated systems and for further processing are issued from the EEC.

The fundamental task is to represent the **information model**, in which components and configured projects with functional and discipline-specific structures are depicted.

When functional configuration is implemented using the approach presented here, the result is to shift the focus of activities from work with existing systems to the generation of a consistent information model of machines and plants. Since the goal is to create project data based as exclusively as possible on the model, this implementation of functional configuration is referred to as **model-driven configuration**.
