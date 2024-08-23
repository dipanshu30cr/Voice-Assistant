import pyttsx3
import speech_recognition as sr
import webbrowser
import salman
import atif
recognizer= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
        

    
    engine.setProperty('rate', 125)     # Setting up a new voice rate
                            
    engine.setProperty('volume', 1.0)       # Setting up volume level between 0 and 1

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processRequest(c):
    if "open google" in c.lower():
          webbrowser.open("https://www.google.co.in/")

    elif "open youtube" in c.lower():
          webbrowser.open("https://www.youtube.com")
    elif "open my portfolio" in c.lower():
          webbrowser.open("https://dipanshu30cr.github.io/myportfolio/")
    elif "open linkedin" in c.lower():
          webbrowser.open("https://www.linkedin.com")
    # elif c.lower().startswith("play"):
    #     song = c.lower().split("play ", 1)[1].strip().title()  # Convert to Title Case
    #     if song in salman.salman_khan_songs:
    #         link = salman.salman_khan_songs[song]
    #         webbrowser.open(link)
    #     else:
    #         speak("Sorry, I could not find the song in the database.")


    

if __name__=="__main__":
        speak("How can I help you")
        while True:
                

                # recognize speech using google
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listining....!")
                        audio = r.listen(source)
                    #print("i said ------------    " + r.recognize_sphinx(audio))
                    command= r.recognize_google(audio)
                    print(command)
                    processRequest(command)


                except sr.UnknownValueError:
                    print("System could not understand audio")
                except sr.RequestError as e:
                    print("System error; {0}".format(e))

                

        #Listen for the wake word "Dipanshu"