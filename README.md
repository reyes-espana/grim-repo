# grim-repo



## Industry Standards 

- **ISO 27001 Certification** - contains more than a dozen standards that provide requirements for an information security management system

- **SOC 2** - AKA Systems & Organizational Control 2; Specifically desinged to minimize risk and exposure of data for service providers who store customer data in the cloud.

- **OWASP Top 10** - covers some of the most common application vulnerabilities while the **SANS Top 25** covers the most dangerous software errors. 

- **NIST Framework** - consists of five key functions (Identify, Protect, Respond, Recover) that provide a comprehensive view of the lifecycle for managing cybersecurity risk over time. It's built off of practices that are known to be effective, it helps to better integrate and align cybersecurity risk management with broader enterprise risk management processes, and it also fosters communication among both internal and external stakeholders about cybersecurity. 





## OWASP Top 10


**1st** - First on the list is **BROKEN ACCESS CONTROL** 

Since access control is essentially making sure users cannot act outside of their intended permissions,

if its function is broken, it can lead to unauthorized information disclosure, modification, destruction of data or even performing a critical business function.

<sup> Access control is only effective in trusted server-side code or server- less   API, where the attacker cannot modify the access control check or metadata. </sup>




**2nd** - **CRYPTOGRAPHIC FAILURE** is caused by using old or weak cryptographic algorithms, 
unenforced encryption, and using insecure cryptographic hash functions.

Minimizing the scope of the data that is stored and implementing a classifying data process can help prevent this vulnerability.




**3rd** - The **INJECTION** vulnerability now includes the XXS vulnerability (otherwise known as Cross-Site Scripting).

Since applications and commands are written in code, it’s up to the interpreter to determine which pieces of code are data and which pieces of code are commands. 

Normally, an application is supposed to control the commands and the user is supposed to provide the data. In an injection attack, if a user is able to specify a command, they can direct the system to perform an action that could lead to data exposure.

Ultimately, source code review and input validation are some of the best methods to defend against it.




**4th** - **VULNERABLE AND OUTDATED COMPONENTS** was previously known as Using Components with Known Vulnerabilities. 

To defend against this vulnerability, it helps to know the versions of all components you use, keep software up to date, and conduct regular vulnerability scanning. 

To prevent it, remove unused dependencies, monitor for libraries and components, and continuously inventory the versions of both client-side and server-side components <sup>(e.g., frameworks, libraries).</sup>




**5th** - **INSECURE DESIGN** is a NEW Category that focuses on risks related to design and architectural flaws like missing or ineffective control design.

The reason it is **not** the source of all other categories is because it has more to do with design rather than  implementation, each of which have their own root causes and remediations.

All This means is that in order to have secure software, a Secure Development Life Cycle that includes threat modeling, secure design patterns-and-principles, and reference architectures is required.

<sup>Reference Architectures: secured component library, tooling, threat modeling
**EXAMPLE:** the credential recovery workflow, otherwise known as the “Forgot my password” workflow when it includes questions and answers that can be bypassed.</sup>




**6th** - **SECURITY MISCONFIGURATION**  is a result of shifts into highly configurable software.

A repeatable hardening process, a segmented application architecture, and the removal of unnecessary features help prevent this vulnerability.




**7th** - **IDENTIFICATION AND AUTHENTICATION FAILURES** Involves confirmation of the user's identity, authentication, and session management are critical to protecting against authentication-related attacks.

 So Things like Multi-Factor Authentication, weak password checks, and hardened pathways (registration, credential recovery, and API) help to protect against this vulnerability.
 
 
 
 
**8th** - **SOFTWARE AND DATA INTEGRITY FAILURES** is another new category that now encompasses Insecure Deserialization and relates to code and infrastructure that does not protect against integrity violations.
 
For **EXAMPLE:** many applications now include auto-update functionality, where updates are downloaded without sufficient integrity verification and applied to the previously trusted application.

This means that Attackers could potentially upload their own updates to be distributed and run on all installations.




**9th** - **SECURITY LOGGING AND MONITORING** FAILURES was previously known as Insufficient Logging & Monitoring. It has been expanded to include more types of failures which can directly impact accountability, visibility, incident alerting, and forensics. 

The idea is to help detect, escalate, and respond to active breaches in a timely manner.




**10th** - **SERVER SIDE REQUEST FORGERY**; You can also call it XSRF or Session Riding. This vulnerability is caused during the implementation of an architectural security tactic.

This usually happens because a web app is fetching a remote resource without validating the user-supplied URL. If there’s nothing in place to verify that that request was sent intentionally, the attacker can send a crafted request to an unexpected destination by making the web server believe it’s authentic even when protected by a firewall, VPN, or other types of Network Access Control.

 The consequences vary, but since the attacker takes on the identity of the victim it is possible for the attacker to target a privileged user and obtain complete control over the web app. This includes having the power to steal or delete data, uninstalling the product, or using the product to conduct other attacks against the product’s users.
 

