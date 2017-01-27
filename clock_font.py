# -*-coding: utf-8 -*-
from os import system


def translate(text):
    text = str(text)
    letters = []
    for letter in text:
        letters.append(LETTERS[letter])
    for i in range(5):
        for letter in letters:
            print "\t\t" + letter.splitlines()[i],
        print
    # clear()


def clear():
    system("clear")


LETTERS = {
" ":u"""\






""",
"1":u"""\
  ██  
████  
  ██  
  ██  
██████""",
"2": u"""\
██████
    ██
██████
██    
██████""",
"3":u"""\
██████
    ██
██████
    ██
██████""",
"4":u"""\
██  ██
██  ██
██████
    ██
    ██""",
"5":u"""\
██████
██    
██████
    ██
██████""",
"6":u"""\
██████
██    
██████
██  ██
██████""",
"7":u"""\
██████
    ██
    ██
    ██
    ██""",
"8":u"""\
██████
██  ██
██████
██  ██
██████""",
"9":u"""\
██████
██  ██
██████
    ██
██████""",
"0":u"""\
██████
██  ██
██  ██
██  ██
██████""",
":":u"""\
      
  ██  
      
  ██  
      
    """}


LETTERS1 = {
  "1":u"""\
    ▄▄▄▄     
  ▄█░░░░▌    
 ▐░░▌▐░░▌    
  ▀▀ ▐░░▌    
     ▐░░▌    
     ▐░░▌    
     ▐░░▌    
     ▐░░▌    
 ▄▄▄▄█░░█▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀""",
  "2":u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀""",

  "3": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀
  """,

  "4": u"""\
 ▄         ▄
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
          ▐░▌
           ▀
  """,

  "5": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀
  """,

  "6": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀
  """,
  "7": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
         ▐░▌ 
        ▐░▌  
       ▐░▌   
      ▐░▌    
     ▐░▌     
    ▐░▌      
   ▐░▌       
    ▀        
  """,
  "8": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
 ▐░░░░░░░░░▌ 
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀
  """,
  "9": u"""\
 ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌
          ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀
  """,
  "0": u"""\
  ▄▄▄▄▄▄▄▄▄
 ▐░░░░░░░░░▌
▐░█░█▀▀▀▀▀█░▌
▐░▌▐░▌    ▐░▌
▐░▌ ▐░▌   ▐░▌
▐░▌  ▐░▌  ▐░▌
▐░▌   ▐░▌ ▐░▌
▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄█░█░▌
 ▐░░░░░░░░░▌
  ▀▀▀▀▀▀▀▀▀
  """,
  ":": u"""\
            
            
            
██╗         
╚═╝         
██╗         
╚═╝         
            
            
            
            
  """,
  " ": u"""\
            
            
            
            
            
            
            
            
            
            
            
  """,
}