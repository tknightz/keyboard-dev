from pynput.keyboard import Key, Controller, Listener
import maps
import re

hasDPattern = '[đ]'
hasWPattern = '[ă,ơ,ư]{1}'
hasVPattern = '[â,ô,ê]{1}'
hasUOPattern = 'ươ'
hasFPattern = '[à,ằ,ầ,è,ề,ò,ồ,ờ,ù,ừ,ì,ỳ]{1}'
hasSPattern = '[á,ắ,ấ,é,ế,ó,ố,ớ,ú,ứ,í,ý]{1}'
hasRPattern = '[ả,ẳ,ẩ,ẻ,ể,ỏ,ở,ổ,ủ,ử,ỉ,ỷ]{1}'
hasXPattern = '[ã,ẵ,ẫ,ẽ,ễ,õ,ỗ,ỡ,ũ,ữ,ĩ,ỹ]{1}'
hasJPattern = '[ạ,ặ,ậ,ẹ,ệ,ọ,ộ,ợ,ụ,ự,ị,ỵ]{1}'
hasVowelsPattern = '[a,e,o,i,u,y,e,ê,ơ,ô,ư]{1}'
VNPattern = '[]'

class Control:
    def __init__(self):
        self.keyboard = Controller()
        self.mapsWord = {}
        self.mapsTonge={
                'huyen':0,
                'sac':0,
                'nga':0,
                'hoi':0,
                'nang':0
                }
        self.word = []
        self.tempWord = []
        self.sizeWord = 0
        self.autoType = False
    
    def typeNewWord(self,word):
        self.autoType = True
        cnt = len(self.tempWord)
        while cnt>0:
            self.keyboard.press(Key.backspace)
            self.keyboard.release(Key.backspace)
            cnt-=1
        self.keyboard.type(word)
        self.autoType=False

    def on_press(self,key):
        if key==Key.space:
            self.word = ''
            self.sizeWord = 0
        elif hasattr(key,'char'):
            if key.char in self.mapsWord.keys():
                hasV = re.findall(r'{0}'.format(hasVPattern),self.word)
                hasW = re.findall(r'{0}'.format(hasWPattern),self.word)
                if len(hasW):
                    indexW = self.tempWord.index(hasW[0])
                    self.tempWord[indexW]=maps.canGetDup[key.char]
                    self.typeNewWord(''.join(self.tempWord))

                elif len(hasV):
                    indexV = self.word.index(hasV[0])
                    self.tempWord[indexV]=key.char
                    self.typeNewWord(''.join(self.tempWord))
                else:
                    index = self.tempWord.index(key.char)
                    self.tempWord[index]=maps.canGetDup(key.char)
                    self.typeNewWord(''.join(self.tempWord))

            elif key.char == 'f':
                hasF = re.findall(r'{0}'.format(hasFPattern),self.word)
                if len(hasF):
                    indexF = self.tempWord.index(hasF[0])
                    key_list = list(maps.canGetF.keys())
                    value_list = list(maps.canGetF.values())
                    self.tempWord[indexF]=key_list[value_list.index(self.tempWord[indexF])]
                    self.tempWord+='f'
                else:
                    lastVW = re.findall(r'{0}'.format(hasVowelsPattern),self.word)
                    if len(lastVW):
                        lastVowel = lastVW[len(lastVW)-1]
                        indexInWord = self.tempWord.index(lastVowel)
                        self.tempWord[indexInWord]=maps.canGetF(lastVowel)
                        self.typeNewWord(self.tempWord)

            
            elif not self.autoType:
                    self.word+=key.char
                    self.tempWord+=key.char

    def on_release(self,key):
        if key==Key.esc:
            return False

kc = Control()



# Collect events until released
with Listener(
        on_press=kc.on_press,
        on_release=kc.on_release
        ) as listener:
    listener.join()
