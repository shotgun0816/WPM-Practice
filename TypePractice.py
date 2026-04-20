from pynput import keyboard
import time
import os
import random
from pathlib import Path

text_list=[]
word_list=[]
user_list=[]
text_chosen=''
word_count=[]
display=''

def get_file():
    global text_chosen, word_list, word_count
    dir_path=Path(os.path.dirname(__file__))
    root=dir_path/'text_1.txt'
    with open(root, 'r', encoding='utf-8') as file:
        for line in file:
            text_list.append(line.strip())
    text_chosen=text_list[random.randint(0,len(text_list)-1)]
    word_count=len(text_chosen.split(' '))
    word_list=list(text_chosen)
    print(f'{text_chosen}\n\nAnswer:')

def on_press(key):
    global display, text_chosen
    if key==keyboard.Key.esc:
            return False
    try:
        user_list.append(key.char)
        check(key.char)
    except AttributeError:
        if key==keyboard.Key.space:
            if display==text_chosen:
                return False
            user_list.append(' ')
            check(key.char)
        
def check(word):
    global word_list, user_list, text_chosen, display
    os.system('cls||clear')
    progress=len(user_list)-1
    print(f'{text_chosen}\n')
    if user_list[progress]!=word_list[progress]:
        user_list.pop()
    else:
        progress+=1
    display=''.join(user_list)
    print(f'Answer:\n{display}')

os.system('clear||cls')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
    os.system('cls||clear')
get_file()
listener=keyboard.Listener(on_press=on_press)
start=time.time()
listener.start()
listener.join()
end=time.time()
time_used=(end-start)/60
wpm=word_count/time_used
print(f'Completed. Your WPM is {wpm}.')