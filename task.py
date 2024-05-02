#functions
import datetime
from speek import say
#2 types of functions
 #1-non input functions
 #eg time date speed test

def Time():
    time= datetime.datetime.now().strftime("%H:%M")
    say(time)

def Date():
    date= datetime.date.today()
    say(date)

def Day():
    day= datetime.datetime.now().strftime("%A")
    say(day)

def NonInputExecution(query):
    query =str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()


 #2-input funtions

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("about","").replace("what is","").replace("wikipedia","").replace("who is","")
        import wikipedia
        try:
            # Search for the topic first
            search_results = wikipedia.search(name)
            if search_results:
                # Get the first search result and fetch its summary
                result = wikipedia.summary(search_results[0])
                say(result)
            else:
                say("Sorry, I couldn't find any information on that topic.")
        except wikipedia.exceptions.DisambiguationError as e:
            # Handling disambiguation error if multiple pages found
            options = ", ".join(e.options[:5])  # Displaying up to 5 options
            say(f"There are multiple options for {name}. They are: {options}. Please be more specific.")
        except wikipedia.exceptions.PageError:
            say("Sorry, I couldn't find any information on that topic.")
        except Exception as ex:
            say(f"An error occurred: {ex}")

    # other conditions...

    
    elif "google" in tag:
        query= str(query).replace("google","").replace("search","")
        import pywhatkit
        pywhatkit.search(query)

import os
import subprocess


# def open_application(application_name):
#     try:
#         # Replace 'application_name.exe' with the actual executable name of the application
#         # Adjust the paths as needed
#         if os.path.exists(f'C:\\Program Files\\Microsoft\Windows\Start Menu\Programs\{application_name}\\{Word 2016}.exe'):
#             subprocess.Popen([f'C:\\Program Files\\Microsoft\Windows\Start Menu\Programs{application_name}\\{application_name}.exe'])
#         elif os.path.exists(f'C:\\Program Files (x86)\\{application_name}\\{application_name}.exe'):
#             subprocess.Popen([f'C:\\Program Files (x86)\\{application_name}\\{application_name}.exe'])
#         else:
#             say(f"{application_name} is not installed on your computer. Please install it first.")
#     except Exception as e:
#         print(f"Error opening {application_name}: {e}")

