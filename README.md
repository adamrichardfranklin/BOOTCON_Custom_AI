# BOOTCON_Custom_AI (chat.py)

The objective of this project was to create a custom GUI chatbot that integrates with OpenAI to automate script writing. The chatbot was developed using Python and run in a local virtual Python environment. The chat interface was designed using the Sublime Text Editor and Tkinter. The chatbot used OpenAI's API key to generate scripts based on user input. These scripts will be used to automate tasks such as file transfers, backups, and data analysis. The chatbot will be able to save these scripts and generate cronjobs to schedule their execution. 

Because our chatbot is hosted in a local python environment an intruder on our machine will be unable to see any sensitive information we may have input to our chatbot through our web history. Without our private API key our information is secure from those same attackers as well due to the nature of the encrpytion for these API keys.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Introduction
This whitepaper provides a detailed overview of a project that aimed to develop a custom GUI chatbot, which integrated with OpenAI to automate script writing. The document outlines the project's objectives, roles and responsibilities of the team members, and the timeline for project completion.

# Project Overview
The objective of the project was to create a custom GUI chatbot using Python that interacted with users and generated scripts based on their input. The chatbot leveraged OpenAI's API key to generate scripts for automating tasks such as file transfers, backups, and data analysis. These scripts were saved and could be scheduled for execution using cronjobs.

2.1 Technology Stack
The project utilized the following technologies:
Python: The chatbot was developed using the Python programming language.
OpenAI API: OpenAI's API key was integrated to leverage its capabilities in script generation. The chatbot used OpenAI's powerful language models to generate accurate and context-aware scripts.
Tkinter: The graphical user interface (GUI) for the chatbot was developed using Tkinter, a Python library known for creating interactive interfaces. Tkinter provided the foundation for designing the chatbot's intuitive and user-friendly interface.
Roles and Responsibilities
The project team consisted of three members who collaborated to deliver the chatbot solution.

3.1 Project Leads
Brandon Stockdale, Rosario Moreno, and Adam Franklin led the project, overseeing the overall development process, and ensuring the successful integration of OpenAI's API with the chatbot. They coordinated the project's activities, ensured effective communication, and provided guidance to the team members.

3.2 Chat Interface Development
Rosario Moreno, Adam Franklin, and Brandon Stockdale were responsible for designing and developing the chat interface using the Sublime Text Editor and Tkinter. They utilized Tkinter's extensive widget library to create an aesthetically pleasing and user-friendly interface. Custom features were added to enhance the user experience and facilitate seamless interaction with the chatbot.

3.3 Whitepaper and Testing
Adam Franklin and Rosario Moreno created the official whitepaper for the project, detailing the project's objectives, technical specifications, and implementation details. They conducted thorough testing, ensuring the chatbot's functionality, accuracy, and reliability. Any identified issues or vulnerabilities were addressed to deliver a robust solution.

3.4 Functionality Testing and Demonstration
Brandon Stockdale was responsible for testing the chatbot's functionality. He ensured that the integration with OpenAI's API was seamless, and the chatbot generated accurate scripts based on user input. Brandon created a recorded demonstration showcasing the chatbot's capabilities, highlighting its accurate script generation and user-friendly interface.
Timeline
The project followed the following timeline:

4.1 Day 1-2: Project Planning and Environment Setup
During the initial two days, the team focused on project planning, defining requirements, and setting up the local virtual Python environment. They installed necessary libraries, including OpenAI's Python library, to facilitate integration with OpenAI's API.

4.2 Day 2-4: OpenAI API Integration and Script Generation
In this phase, the team integrated OpenAI's API key into the chatbot application. They developed the functionality to generate scripts based on user input using OpenAI's language models. Extensive testing was conducted to ensure the accuracy, coherence, and relevance of the generated scripts.

4.3 Day 5-6: Chat Interface Development and Script Scheduling
During this phase, the team focused on designing and developing the chat interface using the Sublime Text Editor and Tkinter. Tkinter's widget library was utilized to create an intuitive and visually appealing interface. Additionally, the functionality for scheduling generated scripts
