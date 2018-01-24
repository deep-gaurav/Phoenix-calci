def import_sympy(obj):
    d=obj.display
    try:
        d.text= 'try import sympy'
        import sympy.simplify
        d.text = 'symp import successfull'
    except:
        import zipfile
        d.text = "Trying to install sympy, Extracting"
        zip_ref = zipfile.ZipFile("unittest.zip", 'r')
        zip_ref.extractall("./")
        zip_ref.close()
        d.text = "installing sympy"


    print('changing app')
    from calc import mainapp
    for x in App.get_running_app().root.children:
        App.get_running_app().root.remove_widget(x)
    App.get_running_app().root.add_widget(mainapp())
    return True

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
import threading

class startup(App):
    theme_cls = ThemeManager()
    def __init__(self,**kwargs):
        App.__init__(self,**kwargs)
        self.display=Button(text="running")
        self.roott=BoxLayout()
        self.roott.add_widget(self.display)
    def build(self):
        self.th=threading.Thread(target=import_sympy,args=(self,))
        self.th.start()
        return self.roott

if __name__=="__main__":
    startup().run()
