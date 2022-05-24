import pyttsx3  #thư viện để nó có thể nói được những gì mình đánh vào trong code
import datetime #thư viện để import giờ vào
import speech_recognition as sr #cái thư viện này quan trọng để có thể nhận dạng và xử lý sơ bộ giọng nói đầu vào của mình
import webbrowser as wb
import os
import playsound
import time
import requests
from playsound import playsound#mình import cái này để nó có thể phát âm thanh
import msvcrt as m
def wait():
    m.getch()

PTNK_AI_assistant=pyttsx3.init()  # khởi động text sang giọng nói ^^
voice=PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0' #đây là đường dẫn trong registry của Microsoft Windows của giọng nữ Microsoft Zira
PTNK_AI_assistant.setProperty('voice',assistant_voice_id)

def speak(audio):
    print('PTNK_AI_assistant: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()


def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p') #giải thích nè ^^: %I là giờ loại 12 tiếng, %M là phút, %p là AM hay PM
    speak('It is')
    speak(Time)
def date():
    url= f'https://timesles.com/en/calendar/weeks/days/today/'
    wb.get().open(url)
    speak('This is the date today')
    

def welcome(): #đây là mình tạo một cái function chào hỏi dựa theo thời gian mỗi khi khởi động PTNK_AI_ASSISTANT
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning boss')
    elif hour >=12 and hour <18:
        speak('Good afternoon boss')
    elif hour >=18 and hour <21:
        speak('Good evening boss')
    elif hour >=21 and hour <24:
        speak('Good night and have a nice dream boss!')
    elif hour >=0 and hour <3:
        speak('It is late boss, let us take a nap')
    speak('How can I help you now')

internetstatus=0
url = "https://www.google.com/"
timeout = 1.5
try:
	request = requests.get(url, timeout=timeout)
	internetstatus=1
except (requests.ConnectionError, requests.Timeout) as exception:
	internetstatus=2

def command(): # Đây là mình tạo một cái function nghe và xử lý giọng nói của mình theo tiếng việt
    if internetstatus==1:
        print(' ')
        print('Listening . . .')
        print(' ')
        c=sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold=1
            audio=c.listen(source)    
        try:
            
            query = c.recognize_google(audio,language='en-US')#en-US #vi
            print('Boss: ' + query)
        except sr.UnknownValueError:
            print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
            query = str(input('your favor is: '))
        return query
    if internetstatus==2:
        print('No internet! If your pc have connected to the internet, type: internet')
        print('Or if your pc have not connected to the internet,')
        query = str(input('Try typing your command: '))
        return query





def thực_thi_trợ_lý_ảo_STEAM_PTNK():  # đây là phần quan trọng nhất. Đó là phần xử lý yêu cầu của mình
    os.system('cls')
    speak('successfully switch to online mode')
    playsound('assets/PTNK-on.mp3') #cái này mình có 1 file chào trong folder, tuyệt đối đừng xóa nếu không script sẽ bị lỗi !!!  Mỗi lần chạy con trợ lý này là nó khởi động âm thanh
    welcome()  #mình đã tạo một function chào nên giờ mình chỉ cần viết welcome ra thôi ^^
    while True:
        query=command().lower() #cái bước này là cái bước chuyển tất cả chữ viết hoa trong lời nói của mình thành chữ viết thường để máy dễ tra đúng hơn
        if "map" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://www.google.com/maps/'
            wb.get().open(url)
            speak(f'This is google maps')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif "hello" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'Hello my boss')
            speak(f'How can I help you now boss?')
        elif "how are you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'I am feeling good today. Thank you')
            speak(f'How can I help you now boss?')
        elif "maps" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://www.google.com/maps/'
            wb.get().open(url)
            speak(f'This is google maps')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif "glob" in query: #all global or globe returns to this code
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
            wb.get().open(url)
            speak(f'This is google earth')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif "earth" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
            wb.get().open(url)
            speak(f'This is google earth')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'translat' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.dict.cc/'
            wb.get().open(url)
            speak(f'This is german-english dictionary.')
            url2=f'https://jdict.net/'
            speak('...')
            speak('...')
            wb.get().open(url2)
            speak('this is Japanese-Vietnamese dictionary.')
            speak('...')
            url3=f'https://translate.google.com/'
            speak('...')
            wb.get().open(url3)
            speak('this is google translate.')
            url4=f'https://www.oxfordlearnersdictionaries.com/'
            speak('...')
            speak('...')
            wb.get().open(url4)
            speak(' and this is Oxford dictionary')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'dictionar' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.dict.cc/'
            wb.get().open(url)
            speak(f'This is german-english dictionary.')
            url2=f'https://jdict.net/'
            speak('...')
            speak('...')
            wb.get().open(url2)
            speak('this is Japanese-Vietnamese dictionary.')
            url3=f'https://translate.google.com/'
            speak('...')
            speak('...')
            wb.get().open(url3)
            speak('this is google translate.')
            url4=f'https://www.oxfordlearnersdictionaries.com/'
            speak('...')
            speak('...')
            wb.get().open(url4)
            speak(' and this is Oxford dictionary')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        
        elif 'google' in query: # ở đây mình làm theo kiểu xử lý theo từ khóa, tức là trong yêu cầu của mình chỉ cần có từ khóa đó là nó sẽ thực thi, tương tự với mấy cái phía dưới
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Google for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')


        elif 'weather' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'whether' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'climate' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'typ' in query: # luyện gõ, gõ máy, đánh chữ, bàn phím, gõ
            os.system('cls')
            print('Boss: ' + query)
            speak('Which language do you want to type?')
            search=command().lower()
            if 'english' in search:
                url=f'https://10fastfingers.com/typing-test/english'
                wb.get().open(url)
                speak(f'Try your best with this English typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'vietnam' in search:
                url=f'https://10fastfingers.com/typing-test/vietnamese'
                wb.get().open(url)
                speak(f'Try your best with this Vietnamese typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'german' in search:
                url=f'https://10fastfingers.com/typing-test/german'
                wb.get().open(url)
                speak(f'Try your best with this German typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'japan' in search:
                url=f'https://10fastfingers.com/typing-test/japanese'
                wb.get().open(url)
                speak(f'Try your best with this Japanese typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'french' in search:
                url=f'https://10fastfingers.com/typing-test/french'
                wb.get().open(url)
                speak(f'Try your best with this French typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'france' in search:
                url=f'https://10fastfingers.com/typing-test/french'
                wb.get().open(url)
                speak(f'Try your best with this French typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'russia' in search:
                url=f'https://10fastfingers.com/typing-test/russian'
                wb.get().open(url)
                speak(f'Try your best with this Russian typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'nether' in search:
                url=f'https://10fastfingers.com/typing-test/dutch'
                wb.get().open(url)
                speak(f'Try your best with this Dutch typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'neder' in search:
                url=f'https://10fastfingers.com/typing-test/dutch'
                wb.get().open(url)
                speak(f'Try your best with this Dutch typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'hol' in search:
                url=f'https://10fastfingers.com/typing-test/dutch'
                wb.get().open(url)
                speak(f'Try your best with this Dutch typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'chin' in search:
                speak('Chinese simplified or Chinese Traditional? ')
                chinesetype=command().lower()
                if 'simple' in chinesetype:
                    url=f'https://10fastfingers.com/typing-test/simplified-chinese'
                    wb.get().open(url)
                    speak(f'Try your best with this Chinese Simplified typing test!')
                    speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                    wait()
                    speak(f'what else you would like me to do, boss?')
                elif 'simplif' in chinesetype:
                    url=f'https://10fastfingers.com/typing-test/simplified-chinese'
                    wb.get().open(url)
                    speak(f'Try your best with this Chinese-Simplified typing test!')
                    speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                    wait()
                    speak(f'what else you would like me to do, boss?')
                elif 'tradition' in chinesetype:
                    url=f'https://10fastfingers.com/typing-test/traditional-chinese'
                    wb.get().open(url)
                    speak(f'Try your best with this Chinese-Traditional typing test!')
                    speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                    wait()
                    speak(f'what else you would like me to do, boss?')
            elif 'korea' in search:
                url=f'https://10fastfingers.com/typing-test/korean'
                wb.get().open(url)
                speak(f'Try your best with this Korean typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'ital' in search:
                url=f'https://10fastfingers.com/typing-test/italian'
                wb.get().open(url)
                speak(f'Try your best with this Italian typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'spa' in search:
                url=f'https://10fastfingers.com/typing-test/spanish'
                wb.get().open(url)
                speak(f'Try your best with this Spanish typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'portug' in search:
                url=f'https://10fastfingers.com/typing-test/portuguese'
                wb.get().open(url)
                speak(f'Try your best with this Portuguese typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'thai' in search:
                url=f'https://10fastfingers.com/typing-test/thai'
                wb.get().open(url)
                speak(f'Try your best with this Thai typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'arab' in search:
                url=f'https://10fastfingers.com/typing-test/arabic'
                wb.get().open(url)
                speak(f'Try your best with this Arabic typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')


########################################################################## Quang Bách

        

        elif 'search' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')



        elif 'web' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'facebook' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.facebook.com/'
            wb.get().open(url)
            speak(f'This is facebook for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'twitter' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://twitter.com/'
            wb.get().open(url)
            speak(f'This is twitter for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'browser' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')


        elif 'look up' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')



        elif "youtube" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search on youtube now boss?')
            search=command().lower()
            url = f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Youtube for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        
        elif "quit" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "stop" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "bye" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "see you later" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "see you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()


        elif 'time' in query:
            os.system('cls')
            print('Boss: ' + query)
            time()
            speak(f'what else you would like me to do, boss?')
        elif 'clock' in query:
            os.system('cls')
            print('Boss: ' + query)
            time()
            speak(f'what else you would like me to do, boss?')

        
        elif 'date' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'day' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        

        elif 'month' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'year' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'you can' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')
        elif 'abilit' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')
        elif 'function' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif 'create you' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('Mr. Bach created me. How can I help you now, boss?')
        elif 'created you' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('Mr. Bach created me. How can I help you now, boss?')
        elif 'made you' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('Mr. Bach created me. How can I help you now, boss?')
        elif 'make you' in query: # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('Mr. Bach created me. How can I help you now, boss?')
        elif 'help' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')
        elif 'instruct' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')
        elif 'how to use' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')


        elif 'relax' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')
            
        elif 'stress' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')

        elif 'hang out' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')


if __name__ =='__main__':
    thực_thi_trợ_lý_ảo_STEAM_PTNK() # nguyên một dãy code phía trên mình đã define 'thực_thi_trợ_lý_ảo_STEAM_PTNK nên giờ chỉ cần gọi nó ra ^^, để dấu () ở cuối để nó làm thành vòng lặp