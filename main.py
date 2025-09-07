from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import math

Window.size = (280,480)




class Calculator(Screen):

    def calculate(self,*args):
        calc_entry = self.ids.txtinput.text
        if calc_entry !='':
            try:
                if calc_entry[0] in '1234567890()':
                    self.ids.txtinput.text = str(eval(calc_entry))
            except:
                self.ids.txtinput.text = 'Error'

    def ac_clear(self):
        self.ids.txtinput.text = ''

    def delete(self):
        self.ids.txtinput.text = self.ids.txtinput.text[:-1]

    def percentage(self):
        try:
            per = self.ids.txtinput.text+'*100'
            self.ids.txtinput.text = str(eval(per))
        except:
            self.ids.txtinput.text = 'Error'
    def add_sub(self):
        value = self.ids.txtinput.text
        try:
            if value == '':
                pass
            elif value[0] == '-':
                if value[-1] == '-':
                    self.ids.txtinput.text = str(eval(value+'0'))+'+' # -2-
                    
                elif value[-1] == '+':
                    self.ids.txtinput.text = str(eval(value+'0'))+'-' # -2+
                elif int(value[-1]) >= 0:
                    self.ids.txtinput.text = str(eval(value +'*(-1)')) # -2

            elif value[0] == '+':
                if value[-1] == '-':
                    self.ids.txtinput.text = str(eval(value+'0'))+'+' # +2-
                elif value[-1] == '+':
                    self.ids.txtinput.text = str(eval(value+'0'))+'-' # +2+
                elif int(value[-1]) >= 0:
                    self.ids.txtinput.text = str(eval(value +'*(-1)')) # +2
             
            elif int(value[0]) >= 0:
                if value[-1] == '-':
                    self.ids.txtinput.text = str(eval(value+'0'))+'+' # 2-
                elif value[-1] == '+':
                    self.ids.txtinput.text = str(eval(value+'0'))+'-' # 2+
                elif int(value[0]) > 0:
                    self.ids.txtinput.text = str(eval(value +'*(-1)')) # 2
        except:
            self.ids.txtinput.text = 'Error'
            
    def rad(self):
       try:
           value = self.ids.txtinput.text
           new_value = math.radians(int(value))
           self.ids.txtinput.text = str(new_value)
       except:
          self.ids.txtinput.text = 'Error' 

    def deg(self):
        try:
           value = self.ids.txtinput.text
           new_value = math.degrees(int(value))
           self.ids.txtinput.text = str(new_value)
        except:
          self.ids.txtinput.text = 'Error' 
       
    def dot(self):

        value = self.ids.txtinput.text
        try:
            if value == '':
                self.ids.txtinput.text = '0.'
            elif value[-1] == '.':
                pass
            else:
                self.ids.txtinput.text = value + "."
        except:
          self.ids.txtinput.text = 'Error'

    def pi(self):
        self.ids.txtinput.text = self.ids.txtinput.text + str((math.pi))

class MainApp(App):

    
    def build(self):
        return Calculator()

MainApp().run()
