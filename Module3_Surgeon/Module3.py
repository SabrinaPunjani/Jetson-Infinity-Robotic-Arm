#created on 2023-03-29 author @sabrina

#---------------importing modules-----------------
import speech_recognition as sr
import xarm #robotic arm module
import time 
#------------coordinates--------------------------
#surgeon
surgeon_angle = 500


#cleaning bucket
clean_angle = 660

#toolA
toolA_angle = 405
#toolB
toolB_angle = 0

#-------------------------------------------------

arm = xarm.Controller('USB')

userVoiceRecognizer = sr.Recognizer() #user voice input 

print("Surgery in Progress!")

#function for the arm to grab tool and give it to surgeon
def getTool(angle1, angle2):
    """
    Parameters:
    angle1 (int) : angle from surgeon
    angle2 (int) :angle to tool

    Returns:
    None

    """
    arm.setPosition([[1,240],[2, 515],[3,840],[4,280],[5,475],[6,angle1]])
    time.sleep(3)
    arm.setPosition([[1,240],[2, 515],[3,840],[4,280],[5,620],[6,angle1]])
    time.sleep(3)
    arm.setPosition([[1,550],[2, 515],[3,840],[4,280],[5,620],[6,angle1]])
    time.sleep(3)
    arm.setPosition([[1,550],[2, 515],[3, 840],[4,425],[5,335],[6,angle2]])
    time.sleep(2)
  

#function for the arm to grab tool and clean it 
def cleanTool(angle1, angle2):
    """
    Parameters:
    angle1 (int) : angle from surgeon
    angle2 (int) :angle to cleaning bucket

    Returns:
    None

    """
    arm.setPosition([[1,290],[2, 515],[3, 195],[4,425],[5,335],[6,angle1]])
    time.sleep(3)
    arm.setPosition([[1,665],[2, 515],[3, 195],[4,425],[5,335],[6,angle1]])
    time.sleep(2)
    arm.setPosition([[1,665],[2, 515],[3,840],[4,280],[5,475],[6,angle2]])
    time.sleep(3)
    for i in range(3): #dip tool in cleaning bucket 3 times to clean
        arm.setPosition([[1,665],[2, 515],[3,840],[4,280],[5,520],[6,angle2]])
        time.sleep(1)
        arm.setPosition([[1,665],[2, 515],[3,840],[4,280],[5,450],[6,angle2]])
        time.sleep(1)
        
        
surgery = 1 #we start surgery loop

 
#constantly checking for mic input
while(surgery):
    arm.setPosition([[1,290],[2, 515],[3, 195],[4,425],[5,335],[6,surgeon_angle]]) #idle arm position
    try:
        with sr.Microphone() as inputVoiceSource:
            
            userVoiceRecognizer.adjust_for_ambient_noise(inputVoiceSource, duration = 0.5)
            
            #listening to the voice input from mic
            userVoiceInput = userVoiceRecognizer.listen(inputVoiceSource)
            
            #get text using google voice recognition API 
            voice_to_text = userVoiceRecognizer.recognize_google(userVoiceInput)
            
            #put string into lower case for easier text matching
            voice_to_text = voice_to_text.lower()
            #print(voice_to_text)
            if voice_to_text == "grab tool":
                getTool(surgeon_angle, toolA_angle) #grab tool A
            
            if voice_to_text == "clean tool":
                cleanTool(surgeon_angle,clean_angle) #clean the tool and 
            
            if voice_to_text == "turn off medical robot":
                surgery = 0 #we are done opperating
    except sr.UnknownValueError:
        pass
        
print("Surgery is done")