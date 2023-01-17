# grim-repo



Industry Standards 

- ISO 27001 Certification - contains more than a dozen standards that provide requirements for an information security management system

- SOC 2 - AKA Systems & Organizational Control 2; Specifically desinged to minimize risk and exposure of data for service providers who store customer data in the cloud.

- OWASP Top 10 - covers some of the most common application vulnerabilities while the SANS Top 25 covers the most dangerous software errors. 

- NIST Framework - consists of five key functions (Identify, Protect, Respond, Recover) that provide a comprehensive view of the lifecycle for managing cybersecurity risk over time. It's built off of practices that are known to be effective, it helps to better integrate and align cybersecurity risk management with broader enterprise risk management processes, and it also fosters communication among both internal and external stakeholders about cybersecurity. 





OWASP Top 10


1st - First on the list is BROKEN ACCESS CONTROL 

Since access control is essentially making sure users cannot act outside of their intended permissions,

if its function is broken, it can lead to unauthorized information disclosure, modification, destruction of data or even performing a critical business function.

// Access control is only effective in trusted server-side code or server- less   API, where the attacker cannot modify the access control check or metadata.




2nd - CRYPTOGRAPHIC FAILURE 
 is caused by using old or weak cryptographic algorithms, 
unenforced encryption,
 and using insecure cryptographic hash functions.

Minimizing the scope of the data that is stored and implementing a classifying data process can help prevent this vulnerability.




3rd - The INJECTION vulnerability now includes the XXS vulnerability (otherwise known as Cross-Site Scripting).

Since applications and commands are written in code, it’s up to the interpreter to determine which pieces of code are data and which pieces of code are commands. 

Normally, an application is supposed to control the commands and the user is supposed to provide the data. In an injection attack, if a user is able to specify a command, they can direct the system to perform an action that could lead to data exposure.

Ultimately, source code review and input validation are some of the best methods to defend against it.




