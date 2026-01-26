# EplanCloudResourceDeprecationEvent Event

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1734.html

---

Event raised when an Eplan Cloud resource is deprecated

Syntax

**C#**



[Nullable(Mono.Cecil.CustomAttributeArgument[])]

event EventHandler<EplanCloudResourceDeprecationArgs> EplanCloudResourceDeprecationEvent

[Nullable(Mono.Cecil.CustomAttributeArgument[])]

event EventHandler<EplanCloudResourceDeprecationArgs^>^ EplanCloudResourceDeprecationEvent


Event Data

The event handler receives an argument of type [EplanCloudResourceDeprecationArgs](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.EplanCloudResourceDeprecationArgs.html) containing data related to this event. The following **EplanCloudResourceDeprecationArgs** properties provide information specific to this event.

| Property | Description |
| --- | --- |
| [Deprecation](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.EplanCloudResourceDeprecationArgs~Deprecation.html) | Deprecation Date of the Eplan Cloud resource |
| [Link](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.EplanCloudResourceDeprecationArgs~Link.html) | Available alternates to the deprecated resource |
| [Sunset](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.EplanCloudResourceDeprecationArgs~Sunset.html) | Date when the Eplan Cloud resource is expected to become unresponsive |
| [Uri](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.EplanCloudResourceDeprecationArgs~Uri.html) | Uri of the Deprecated Eplan Cloud resource |
