from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy import *
from kivymd.label import MDLabel

#Android Fixing
import os

if not os.path.isdir('./unittest'):
    import zipfile

    zip_ref = zipfile.ZipFile("unittest.zip", 'r')
    zip_ref.extractall("./")
    zip_ref.close()

from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, \
    function_exponentiation
from sympy import N, sympify, diff, integrate, symbols

from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.textfields import MDTextField

x = symbols('x')
kvv = """

#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem


BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation:'vertical'
        size_hint_y:0.5
        MDTextField:
            id:out
            text:'0'
            font_style:'Title'
            font_size:80
            halign:'right'
            padding:(20,0)
        MDLabel:
            id:realtimeupdate
            text:'0'
            size_hint_y:0.6
            font_style:'Headline'
            font_size:60
            halign:'right'
            padding:(20,0)
            

    ScreenManager:
        id:screenmgr
        Screen:
            name: 'buttons'
            GridLayout:
                cols:3
                GridLayout:
                    id:nums
                    cols:3
                    MDFlatButton:
                        size_hint:(1,1)
                        on_press:out.text+='1'
                        MDLabel:
                            text:'1'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='2'
                        size_hint:(1,1)
                        MDLabel:
                            text:'2'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='3'
                        size_hint:(1,1)
                        MDLabel:
                            text:'3'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='4'
                        size_hint:(1,1)
                        MDLabel:
                            text:'4'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='5'
                        size_hint:(1,1)
                        MDLabel:
                            text:'5'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='6'
                        size_hint:(1,1)
                        MDLabel:
                            text:'6'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='7'
                        size_hint:(1,1)
                        MDLabel:
                            text:'7'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='8'
                        size_hint:(1,1)
                        MDLabel:
                            text:'8'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='9'
                        size_hint:(1,1)
                        MDLabel:
                            text:'9'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='.'
                        size_hint:(1,1)
                        MDLabel:
                            text:'.'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='0'
                        size_hint:(1,1)
                        MDLabel:
                            text:'0'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        id:equal_but
                        size_hint:(1,1)
                        MDLabel:
                            text:'='
                            font_size:20
                            halign:'center'

                GridLayout:
                    id:basicbuts
                    cols:1
                    size_hint_x:0.2
                    MDFlatButton:
                        size_hint:(1,1)
                        id:cancel_but
                        text:'DEL'

                    MDFlatButton:
                        size_hint:(1,1)
                        id:plus
                        text:'+'
                        on_press:out.text+='+'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:minus
                        text:'-'
                        on_press:out.text+='-'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:multiply
                        text:'*'
                        on_press:out.text+='*'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:divide
                        text:'/'
                        on_press:out.text+='/'
                MDIconButton:
                    size_hint:(0.2,1)
                    icon:'arrow-right'
                    on_press:
                        screenmgr.transition.direction='left'
                        screenmgr.current='trigo'
        Screen:
            name:'trigo'
            
            GridLayout:
                cols:3
                MDIconButton:
                    size_hint:(0.2,1)
                    icon:'arrow-left'
                    on_press:
                        screenmgr.transition.direction='right'
                        screenmgr.current='buttons'
                GridLayout:
                    id:usebut
                    cols:1
                    size_hint_x:0.2
                    MDFlatButton:
                        on_press:out.text+='('
                        size_hint:(1,1)
                        MDLabel:
                            text:'('
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+=')'
                        size_hint:(1,1)
                        MDLabel:
                            text:')'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='x'
                        size_hint:(1,1)
                        MDLabel:
                            text:'x'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='pi'
                        size_hint:(1,1)
                        MDLabel:
                            text:'pi'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_press:out.text+='e'
                        size_hint:(1,1)
                        MDLabel:
                            text:'e'
                            font_size:20
                            halign:'center'
                ScrollView:
                    do_scroll_x:False
                    GridLayout:
                        id:functionsbut
                        size_hint_y:None
                        height:Window.height
                        cols:3
                        MDFlatButton:
                            on_press:out.text+='sin('
                            size_hint:(1,1)
                            MDLabel:
                                text:'sin'
                                font_size:20
                                halign:'center'
                        MDFlatButton:
                            on_press:out.text+='cos('
                            size_hint:(1,1)
                            MDLabel:
                                text:'cos'
                                font_size:20
                                halign:'center'
                        MDFlatButton:
                            on_press:out.text+='tan('
                            size_hint:(1,1)
                            MDLabel:
                                text:'tan'
                                font_size:20
                                halign:'center'
                        MDFlatButton:
                            on_press:out.text+='^'
                            size_hint:(1,1)
                            MDLabel:
                                text:'^'
                                font_size:20
                                halign:'center'            
                        MDFlatButton:
                            on_press:out.text+='e^('
                            size_hint:(1,1)
                            MDLabel:
                                text:'e^'
                                font_size:20
                                halign:'center'            
                        MDFlatButton:
                            on_press:out.text+='!'
                            size_hint:(1,1)
                            MDLabel:
                                text:'!'
                                font_size:20
                                halign:'center'            
                        MDFlatButton:
                            on_press:out.text+='asin('
                            size_hint:(1,1)
                            MDLabel:
                                text:'arc sin'
                                font_size:20
                                halign:'center'                                    
                        MDFlatButton:
                            on_press:out.text+='acos('
                            size_hint:(1,1)
                            MDLabel:
                                text:'arc cos'
                                font_size:20
                                halign:'center'                                    
                        MDFlatButton:
                            on_press:out.text+='atan('
                            size_hint:(1,1)
                            MDLabel:
                                text:'arc tan'
                                font_size:20
                                halign:'center'                                    
                        MDFlatButton:
                            on_press:out.text+='log('
                            size_hint:(1,1)
                            MDLabel:
                                text:'log'
                                font_size:20
                                halign:'center'                
                        MDFlatButton:
                            on_press:out.text+='ln('
                            size_hint:(1,1)
                            MDLabel:
                                text:'ln'
                                font_size:20
                                halign:'center'
                        MDFlatButton:
                            id:differentiate
                            size_hint:(1,1)
                            MDLabel:
                                text:'differentiate'
                                font_size:20
                                halign:'center'                
                        MDFlatButton:
                            id:integrate
                            size_hint:(1,1)
                            MDLabel:
                                text:'integrate'
                                font_size:20
                                halign:'center'
"""
tex = '0'


class mainapp(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.orientation = 'vertical'

        self.numpad = Builder.load_string(kvv)
        self.add_widget(self.numpad)

        # Buttons
        self.out = self.numpad.ids['out']
        self.rout = self.numpad.ids['realtimeupdate']
        self.delbutton = self.numpad.ids['cancel_but']
        self.equalbutton = self.numpad.ids['equal_but']
        self.diffrenbutton = self.numpad.ids['differentiate']
        self.integrabutton = self.numpad.ids['integrate']
        # Binds
        self.delbutton.bind(on_release=self.delholdclr, on_press=self.delbut)
        self.equalbutton.bind(on_release=self.equalcall)
        self.diffrenbutton.bind(on_release=self.differentiate)
        self.integrabutton.bind(on_release=self.integrate)
        # Clock
        Clock.schedule_interval(self.outputloop, 0)

        # Coloring
        for x in self.numpad.ids['nums'].children:
            x.md_bg_color = (0.5, 0.5, 0.5, 1)
            x.children[0].font_size = 40
        for x in self.numpad.ids['basicbuts'].children:
            x.md_bg_color = (0.4, 0.4, 0.4, 1)
            x.children[0].font_size = 40
        for x in self.numpad.ids['usebut'].children:
            x.md_bg_color = (0.2, 0.1, 0.4, 0.5)
            x.children[0].font_size = 40
        for x in self.numpad.ids['functionsbut'].children:
            x.md_bg_color = (0, 0.1, 0.4, 0.4)
            x.children[0].font_size = 40

        # extras
        self.pretex = '..'

    def outputloop(self, dt):
        tex = self.out.text
        if tex == '':
            tex = '0'
        elif len(tex) > 1 and tex[:1] == '0':
            tex = tex[1:]
        self.out.text = tex
        if self.out.text != self.rout.text and self.out.text != self.pretex:
            self.equalcall(None, out=self.rout)
            self.pretex = self.out.text
        if self.rout.text == self.out.text:
            self.rout.text = self.out.text

    def delbut(self, ins):
        tex = self.out.text
        tex = tex[:-1]
        self.out.text = tex
        Clock.schedule_once(self.clearall, 1)

    def clearall(self, ins):
        self.out.text = '0'

    def delholdclr(self, ins):
        Clock.unschedule(self.clearall)

    def equalcall(self, ins, out=None):
        if out == None:
            self.ou = self.out
        else:
            self.ou = out
        transformations = (standard_transformations + (implicit_multiplication_application,))
        finalexprstr = self.out.text.replace('^', '**')
        # finalexprstr=finalexprstr.replace('e','E')
        # finalexprstr=finalexprstr.replace('log','log10')
        try:
            # expr=N(sympify(finalexprstr))
            expr = N(parse_expr(finalexprstr, transformations=transformations))
        except:
            expr = finalexprstr
        try:
            tex = str(eval(str(expr)))
        except:
            tex = expr
        self.ou.text = str(tex)

    def differentiate(self, ins):
        finalexprstr = self.rout.text.replace('^', '**')
        # finalexprstr = finalexprstr.replace('e', 'E')
        # finalexprstr = finalexprstr.replace('log', 'log10')
        try:
            expr = N(sympify(finalexprstr))
            # expr=N(parse_expr(finalexprstr,transformations=transformations))
            difexpr = diff(expr, x)
            self.out.text = str(difexpr)
            self.equalcall(None)
        except Exception as e:
            errormessage = str(e.message)
            errordialog = MDDialog(body=errormessage)
            # TODO

    def integrate(self, ins):
        finalexprstr = self.rout.text.replace('^', '**')
        # finalexprstr = finalexprstr.replace('e', 'E')
        # finalexprstr = finalexprstr.replace('log', 'log10')
        try:
            expr = N(sympify(finalexprstr))
            # expr=N(parse_expr(finalexprstr,transformations=transformations))
            difexpr = integrate(expr, x)
            self.out.text = str(difexpr).replace('Exp', 'e')
            self.equalcall(None)
        except Exception as e:
            print e


class myapp(App):
    theme_cls = ThemeManager()

    def build(self):
        return mainapp()


A = myapp()
A.run()
