# INSTRUCTIONS.md


In order to run our chatbot, the user must ensure of the following;

1: The user has the latest version of Python installed on their machine. (https://www.python.org/downloads/)

2: The user has an account for OpenAI and has credits on that account. (https://openai.com/)

3: The user has a preferred text editor downloaded on their machine. (We reccomend Sublime Text Editor)

 (https://www.sublimetext.com/)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



The user must also make sure that in their command line, they run the following commands to download the neccesary packages to run the chatbot.

  ```bash
    $ pip install customtkinter
  ```
& 

  ```
    $ pip install openai
  ```

Following these steps, the user must download the chat.py file found in the main branch of this repository. The file should be located in an easily found directory (We used the music directory). 

This is how our directory looks; Yours should look similar (at least the chat.py file)

![File_Directory_Image](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/184b7019-1758-478e-8cdd-0d42ae582981)


Once the user has this python file, they will need to navigate to that file within their command line. Once there, the user must run; 

*Description of this command*

  ```
    $ python -m venv virt
  ```
Following this, if the user runs an "ls" command, they should notice next to their "chat.py" file, there is a ne directory called "virt/"

![virt_image](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/e53d47a7-dfae-48f4-92f8-061d180bd1f3)

Now that the user has this directory in their sights, they will need to run the command;

  ```
    $ source virt/Scripts/activate
  ```
Followed by

  ```
    $ python chat.py
  ```
  
This should look something like this;

![Last_command_I_Think](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/aab6eedd-c63c-47b2-a97a-cf09e5baa5bd)

Congratulations! You've now gotten your chatbot to run on your python script in your local (or virtual) machine!

Your chatbot should appear as such.

![Chatbotbox](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/f0f23dbd-9a5b-4a8a-a14c-189069b4646b)

The user will need navigate to https://platform.openai.com/overview and click the button that says "Update API Key" in their personal tab under their name.

![API_Key](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/b647bd21-45f3-4f6b-8a3a-ff44f3d6a8e5)

Once navigated to this page, the user will create an API key if they have not already.

*** NOTE!!! THIS KEY WILL ONLY BE PRODUCED FOR YOU TO COPY ONCE! IF YOU FORGET IT OR DO NOT HAVE IT WRITTEN DOWN YOU WILL NEED CREATE A NEW API KEY!! STORE THIS KEY CAREFULLY! ***

![apikey2](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/c5ed6caf-9187-498c-99c3-8d2a73dbbc4b)

With the API key created and stored safely by the user, the last task before using our bot is to make sure that we still have credit on our OpenAI account. 

The user will navigate to https://platform.openai.com/account/usage in order to see their remaining credits. If the user has no more credits they will need to buy as much as they see fit.

![usage](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/ad8a0d57-8004-4f61-909f-41fefb3e1874)

With all of our ducks in a row, the user can now paste their API key into our chatbot. 

![Pasted API key](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/22d3cb78-d1ab-4290-92a3-674d3fec9ada)

And with this we can use our chatbot to our own delight! Enjoy!

![Chatbot](https://github.com/adamrichardfranklin/BOOTCON_Custom_AI/assets/133983501/644f8c40-4931-4b44-9af3-657beb066d74)








