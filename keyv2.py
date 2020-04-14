from pynput.keyboard import Key, Controller, Listener

import accent_mapping


class Control:
    def __init__(self):
        self.indexVowel = -1 
        self.currentAccent = 'None'
        self.tempWord = []
        self.englishVowel=''
        self.priorityVowel=0
        self.keyboard = Controller()
        self.wordMap = {} 
        self.isAutoType=False
    
    def typeUni(self,uniText):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.shift)
        self.keyboard.press('u')
        self.keyboard.release('u')
        self.keyboard.type(uniText)
        self.keyboard.release(Key.ctrl)
        self.keyboard.release(Key.shift)

    
    def typeNor(self,char):
        self.isAutoType=True
        self.keyboard.press(char)
        self.keyboard.release(char)
        self.isAutoType=False

    def typeNewWord(self):
        self.isAutoType=True
        cnt = len(self.tempWord)
        while cnt>=0:
            self.keyboard.press(Key.backspace)
            self.keyboard.release(Key.backspace)
            cnt-=1
        if len(self.tempWord[self.indexVowel])>1:
            self.typeUni(self.tempWord[self.indexVowel])
        else:
            self.typeNor(self.tempWord[self.indexVowel])
        print(f'this temp vowel {self.tempWord[self.indexVowel]} and rest {self.tempWord[self.indexVowel+1:]}.')
        self.keyboard.type(''.join(self.tempWord[self.indexVowel+1:]))
        self.isAutoType=False
            
    def resetNew(self):
        self.indexVowel = -1
        self.currentAccent = 'None'
        self.englishVowel=''
        self.priorityVowel = 0
        self.tempWord = []
        self.keyboard = Controller()
        self.wordMap = {} 
        self.isAutoType=False


    def on_press(self,key):
        print(key)
        if key==Key.space:
            self.resetNew()
        elif key==Key.backspace:
            print(f'Backspace! and isAutoType={self.isAutoType}')
            if len(self.tempWord)>0 and not self.isAutoType:
                print('Get backspace!')
                #self.tempWord.pop()
        
        if hasattr(key,'char') and not self.isAutoType:
                        
            if self.indexVowel>=0:
                if key.char.lower() == self.englishVowel:
                    if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                    if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_SIGN.keys():
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_SIGN[self.tempWord[self.indexVowel]]
                    self.tempWord[self.indexVowel]=accent_mapping.ADD_UMSIGN[self.tempWord[self.indexVowel]]
                    self.typeNewWord()
                elif key.char.lower() == 'w':
                    if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                    if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_SIGN.keys():
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_SIGN[self.tempWord[self.indexVowel]]
                    self.tempWord[self.indexVowel]=accent_mapping.ADD_VSIGN[self.tempWord[self.indexVowel]]
                    self.typeNewWord()

                elif key.char.lower() == 'f':
                    if self.currentAccent!='GRAVE':
                        if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                            self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]

                        self.tempWord[self.indexVowel]=accent_mapping.ADD_GRAVE[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.currentAccent='GRAVE'
                    else:
                        print('Inside remove grave')
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.tempWord.append('f')
                        self.typeNor('f')
                elif key.char.lower() == 's':
                    if self.currentAccent!='ACUTE':
                        if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                            self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.tempWord[self.indexVowel]=accent_mapping.ADD_ACUTE[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.currentAccent='ACUTE'
                    else:
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.tempWord.append('s')
                        self.typeNor('s')
                elif key.char.lower() == 'r':
                    if self.currentAccent!='HOOK':
                        if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                            self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.tempWord[self.indexVowel]=accent_mapping.ADD_HOOK[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.currentAccent='HOOK'
                    else:
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.tempWord.append('r')
                        self.typeNor('r')
                elif key.char.lower() == 'x':
                    if self.currentAccent!='TILDE':
                        if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                            self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.tempWord[self.indexVowel]=accent_mapping.ADD_TILDE[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.currentAccent='TILDE'
                    else:
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.tempWord.append('x')
                        self.typeNor('x')
                elif key.char.lower() == 'j':
                    if self.currentAccent!='DOT':
                        if self.tempWord[self.indexVowel] in accent_mapping.REMOVE_ACCENT.keys():
                            self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.tempWord[self.indexVowel]=accent_mapping.ADD_DOT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.currentAccent='DOT'
                    else:
                        self.tempWord[self.indexVowel]=accent_mapping.REMOVE_ACCENT[self.tempWord[self.indexVowel]]
                        self.typeNewWord()
                        self.tempWord.append('j')
                        self.typeNor('j')
                else:
                    self.tempWord.append(key.char)
        
            if key.char in accent_mapping.PIORITY_ACCENT.keys() and key.char != self.englishVowel:
                if self.indexVowel==-1:
                    self.indexVowel=0
                    self.englishVowel=key.char
                    self.priorityVowel=accent_mapping.PIORITY_ACCENT[key.char]
                else:
                    priority=accent_mapping.PIORITY_ACCENT[key.char]
                    if priority>self.priorityVowel:
                        self.indexVowel=len(self.tempWord)
                        self.englishVowel=key.char
                        self.priorityVowel=priority
                self.tempWord.append(key.char)
    


    def on_release(self,key):
        if key==Key.esc:
            return False


kc = Control()

with Listener(on_press=kc.on_press,on_release=kc.on_release) as listener:
    listener.join()
                

