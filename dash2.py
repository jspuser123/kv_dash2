from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import numpy as np
from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from IPython import display
from kivy.clock import Clock
from kivy.properties import NumericProperty
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count



#from matplotlib import animation
#from matplotlib.animation import FuncAnimation





Config.write()

colors = {
    "Teal": {
        "200": "#34acbc",
        "500": "#34acbc",
        "700": "#34acbc",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
        "A700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#202020",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
       # "MDTextField":  "#CCCCCC",

    },
}
Builder.load_string('''
<login>:
    FloatLayout:
        size: root.width, root.height
    
    AnchorLayout:
        #md_bg_color: 0,23,2,23
        anchor_x:'center'
        anchor_y:'top'
        
        MDCard:
            spacing:10
            padding:10
            md_bg_color: "blue"
            elevation: 3
            radius:25,25,25,25
            size_hint_y:.1
            MDScreen:
                MDIconButton:
                    on_press: app.root.current = 'sucess'
                    icon: "home"
                    pos_hint: {"center_x": .5, "center_y": .5}
               
                


        
    

<login_sucess>:

   
                     
########################################side button
    MDBoxLayout:
        id:bx
        orientation:'vertical'
        #pos_hint:{'x':.1}
        size_hint_x:.05
        md_bg_color: "teal"           
    ScrollView:
       
        do_scroll_x: False
        do_scroll_y: True
        size_hint_y:.99
        size_hint_x:.05
        #pos_hint:{'x':.1,'y':.1}
        #
       

      
        MDGridLayout:
            cols:1
            size:(root.width,root.height)
            size_hint_x:.95
            size_hint_y:None
            height:self.minimum_height
            md_bg_color: "teal"
            spacing:10
            padding:10
            
    
        
            MDFloatingActionButton:
                #pos_hint: {"center_x": .5, "center_y": .5}
                icon: "apps"
                md_bg_color: "teal"
                on_press:nav_drawer.set_state('toggle')
       
   
            MDFloatingActionButton:
                #pos_hint: {"center_x": .5, "center_y": .89}
                icon: "home"
                md_bg_color:"teal"
                on_press:nav_drawer.set_state('toggle')

        
            MDFloatingActionButton:
                
                icon: "heart"
                #pos_hint: {"center_x": .5, "center_y": .79}
                md_bg_color: "teal"
                on_press:nav_drawer.set_state('toggle')
    
            MDFloatingActionButton:
                #pos_hint: {"center_x": .5, "center_y": .69}
                icon: "rss"
                md_bg_color: "teal"
                on_press:nav_drawer.set_state('toggle')
   
            MDFloatingActionButton:
                #pos_hint: {"center_x": .5, "center_y": .59}
                icon: "cog"
                md_bg_color:"teal"
                on_press:nav_drawer.set_state('toggle')
####################################header
    AnchorLayout:
        #md_bg_color: 0,23,2,23
        anchor_x:'right'
        anchor_y:'top'
        
        MDCard:
            spacing:10
            padding:10
            md_bg_color:"teal"
            elevation: 3
            radius:25,25,25,25
            size_hint_y:.25
            size_hint_x:.95
            
            MDScreen:
                MDSmartTile:
                    radius: 24
                    box_radius: [0, 0, 5, 5]
                    #box_color: 1, 1, 1,2
                    source: "login4.jpg"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    #size_hint: None, None
                    #size: "420dp", "620dp"
   #             Image:
    #                source:"login3.jpg"
                MDTextField:
                    mode: "rectangle"
                    hint_text: "Google"
                    line_color_normal: app.theme_cls.accent_color
                    pos_hint: {"center_x": .75,"center_y":.88}
                    size_hint: .2,.2    
                        
                       

                MDIconButton:
                    on_press: app.root.current = 'menu'
                    icon: "magnify"
                    theme_icon_color: "Custom"
                    icon_color: "blue"
                    elevation: 5
    
                    pos_hint: {"center_x": .86, "center_y": .88}
                MDIconButton:
                    on_press: app.root.current = 'menu'
                    icon: "earth"
                    theme_icon_color: "Custom"
                    icon_color: "blue"
    
                    pos_hint: {"center_x": .89, "center_y": .88}
                MDIconButton:
                    on_press: app.root.current = 'menu'
                    icon: "home"
                    theme_icon_color: "Custom"
                    icon_color: "blue"
    
                    pos_hint: {"center_x": .92, "center_y": .88}
                MDIconButton:
                    on_press: app.root.current = 'menu'
                    icon: "email"
                    theme_icon_color: "Custom"
                    icon_color: "blue"
    
                    pos_hint: {"center_x": .95, "center_y": .88}
                MDIconButton:
                    on_press: app.root.current = 'menu'
                    icon: "cog"
                    theme_icon_color: "Custom"
                    icon_color: "blue"
    
                    pos_hint: {"center_x": .98, "center_y": .88}
               
              
                    
                
#################################bottom
    AnchorLayout:
        #md_bg_color: 0,23,2,23
        anchor_x:'right'
        anchor_y:'bottom'
        
        MDCard:
            spacing:10
            padding:10
            md_bg_color: "teal"
            elevation: 3
            radius:5,5,5,5
            size_hint_y:.05
            size_hint_x:.95
            MDLabel:
                text: "Python Devlopment "
                halign: "left"
                theme_text_color: "Custom"
                pos_hint: {"center_y": .1}
                text_color:"skyblue"
                font_size:20

            MDLabel:
                text: "Created By Vee Yes Softwere "
                halign: "right"
                theme_text_color: "Custom"
                pos_hint: {"center_y":.1}
        
                text_color:"skyblue"
                font_size:20
  
##################################items                
    ScrollView:
       
        do_scroll_x: False  
        do_scroll_y: True
        size_hint_y:.7
        size_hint_x:.96
        pos_hint:{'x':.05,'y':.05}    
        
        MDGridLayout:
            cols:1
            size:(root.width,root.height)
            size_hint_x:.99
            size_hint_y:None
            height:self.minimum_height
            #row_default_height:500
            #row_force_default: True
            id:scr
            
           
            MDCard:
                id:home
                orientation:'vertical'
                spacing:0
                padding:5
                md_bg_color:1,0,0,0
                elevation: 0
                #radius:25,25,25,25
                  
            
                    
                MDCard:
                    #row:1
                    spacing:5
                    padding:5
                    md_bg_color:1,0,0,0
                    elevation: 0
                    radius:5,5,5,5
                    MDCard:
                        spacing:5
                        padding:5
                        md_bg_color:"teal"
                        elevation: 3
                        radius:5,5,5,5
                        
                       
                        MDScreen:
                            #Image:
                                #source: 'digtal.jpg'
                            MDSlider:
                                min: 0
                                max: 50
                                value: 20
                                hint: True
                                pos_hint: {"center_y": .3}
                                elevation: 0
                            MDRoundFlatButton:
                                text: "process"
                                font_size: 20
                                size_hint: .1,.1
                               # pos_hint: {"center_x": 5}
                                text_color:"white"
                                md_bg_color:"pink"
                                on_press: root.clk()
                                            
                           
                                                                            
                               
                            Label:
                                text:'Control Process normal'
                                color: "purple"
                                pos_hint: {"center_x": 0.6,"center_y":.9}
                                size_hint:None,None
                                width:100
                                hight:100
                            
                            
                            Label:
                                text:'cpu process'
                                color:0,0,2,1
                                pos_hint: {"center_x": 0.53,"center_y":.8}
                                size_hint:None,None
                                width:100
                                hight:100
                            
                            Label:
                                text:'ram process'
                                color:0,0,2,1
                                pos_hint: {"center_x": 0.53,"center_y":.7}
                                size_hint:None,None
                                width:100
                                hight:100
                            ###############################
                            Label:
                                id:cpu
                                text:'0%'
                                color: "purple"
                                pos_hint: {"center_x": .1,"center_y":.75}
                                size_hint:None,None
                                width:100
                                hight:100
                                val:0
                                canvas.before:
                                    Color:
                                        rgba:0, 0, 1, 1
                                    Ellipse:
                                        size:self.size
                                        pos:self.pos
                                
                                    Color:
                                        rgba: 0, 33, 3, 5
                                    Ellipse:
                                        size:self.size
                                        pos:self.pos
                                        angle_end:self.val
                                
                                    Color:
                                        rgba: 1, 1, 0, 5
                                    Ellipse:
                                        size:[self.width - 30,self.width -30]
                                        pos:[(self.center_x - (self.width - 30)/2),(self.center_y -(self.hight - 30)/2)]
                            ###############
                            Label:
                                id:ram
                                text:'0%'
                                color: "blue"
                                pos_hint: {"center_x": 0.3,"center_y":.75}
                                size_hint:None,None
                                width:100
                                hight:100
                                val1:0
                                canvas.before:
                                    Color:
                                        rgba: 0, 0, 1, 1
                                    Ellipse:
                                        size:self.size
                                        pos:self.pos
                            
                                    Color:
                                        rgba: 0, 3, 33, 45
                                    Ellipse:
                                        size:self.size
                                        pos:self.pos
                                        angle_end:self.val1
                                
                                    Color:
                                        rgba: 1,1,0,22
                                    Ellipse:
                                        size:[self.width - 30,self.width -30]
                                        pos:[(self.center_x - (self.width - 30)/2),(self.center_y -(self.hight - 30)/2)]
                                        
    ##############################################
                
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color: "teal"
                        elevation: 3
                        radius:5,5,5,5
                        MDScreen:
                            id:bar
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color: "teal"
                        elevation: 3
                        radius:5,5,5,5
                        MDScreen:
                            id:wave
                        
                
    ######################                
                
               
                MDCard:
                    id:row3
                    spacing:5
                    padding:5
                    md_bg_color:1,0,0,0
                    elevation: 0
                    radius:5,5,5,5 
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:1,0,0,0
                        elevation: 0
                        radius:5,5,5,5 
                        MDCard:
                            spacing:5
                            padding:5
                            md_bg_color:"teal"
                            elevation: 3
                            radius:5,5,5,5
                            ScrollView:
                                md_bg_color: 0,4,5,4
                
                                MDList:
                                    id: lis
                                    #md_bg_color: 2,2,2,5
                       
                                    OneLineAvatarListItem:
                                        id:lis1
                                        #md_bg_color: 0,0,23,5
                                        text: "menu"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25 
                                    OneLineAvatarListItem:
                                        id:li2
                                        text: "user"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25
                                    OneLineAvatarListItem:
                                        id:lis3
                                        text: "email"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25
                                    OneLineAvatarListItem:
                                        id:lis4
                                        text: "password"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25
                                    OneLineAvatarListItem:
                                        id:lis5
                                        text: "name"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25
                                    OneLineAvatarListItem:
                                        id:lis6
                                        text: "data_list"
                                        ImageLeftWidget:
                                            source: "im2.jpg"
                                            radius:25,25,25,25
                                             
                        MDCard:
                            spacing:5
                            padding:5
                            md_bg_color:"teal"
                            elevation: 3
                            radius:5,5,5,5
                            MDScreen:
                                id:circle
                    MDCard:
                        id:col2
                        spacing:10
                        padding:10
                        md_bg_color:1,0,0,0
                        elevation: 0
                        radius:5,5,5,5
                        MDScreen:
                            id:tap1
                            md_bg_color:"teal"
    
    MDScreen:   
       
        MDNavigationDrawer:
            md_bg_color: "grey"
            
            id: nav_drawer
            ScrollView:
                
                MDList:
                    
                    
                    id:list
                    
                    OneLineListItem:                
                        text: "               Screen 1"
        
                    OneLineListItem:
                        text: "               Screen 2"
                    OneLineListItem:
                        text: "               Screen 3"
        
        
                    OneLineListItem:
                        text: "               Screen 4"
                    OneLineListItem:
                        text: "               Screen 5"
    
        
                    OneLineListItem:
                        text: "               Screen 6"
                    OneLineListItem:
                        text: "               Screen 7"
        
        
                    OneLineListItem:
                        text: "               Screen 8"
                    
                    
 
                                 
                                              
''')


class login(Screen):
      pass
class login_sucess(Screen):
      def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.c = 0
         self.d = 0
        #####################################tables
         data_tables = MDDataTable(
            pos_hint={"center_x": .5, "center_y": .5},
            background_color_header="#65275d",
            background_color_cell="#451938",
            background_color_selected_cell="e4514f",
            #background_color="teal",

            #size_hint=(0.4, 0.35),
            use_pagination=True,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
            ],
         )
         self.ids.tap1.add_widget(data_tables)

         ########################bar
         x1 = np.array(["A", "B", "c", "D"])
         x5= np.array(["x","y","z","m"])
         y1 = np.array([3, 8, 1, 10])

         fig = plt.figure()
         fig.set_facecolor("teal")

         fig = plt.bar(x1,y1,color="hotpink")
         fig = plt.bar (x5,y1,color="purple")


         fig=plt.ylabel("This is MY Y Axis")
         fig=plt.xlabel("This is my X Axis")
         self.ids.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))
         ############################wave
         x = np.linspace(0, 20, 201)
         y = np.sin(x)
         fig1 = plt.figure(figsize = (5, 5))
         fig1.set_facecolor("teal")
         fig1=plt.plot(x, y, 'b')
         fig1=plt.ylabel("This is MY Y Axis")
         fig1=plt.xlabel("This is X Axis")
         self.ids.wave.add_widget(FigureCanvasKivyAgg(plt.gcf()))
         ############################################################################graph
        # df = pd.read_csv(r"F:\datain\Book1.csv")

         #x = []

        # y = []

        # fig1, ax = plt.subplots()
         #fig1.set_facecolor("teal")
         #plt.ylabel("This is MY Y Axis")
         #plt.xlabel("This is my X Axis")
         #ax.plot(x, y)
         #counter = count(0, 1)

         #def update(i):
         #    idx = next(counter)
         #    x.append(df.iloc[idx, 0])
         #    y.append(df.iloc[idx, 1])
         #    plt.cla()
         #    ax.plot(x, y)

         #ani = FuncAnimation(fig=fig1, func=update, interval=100)

         #self.ids.wave.add_widget(FigureCanvasKivyAgg(plt.gcf()))



         ###########################
         y3 = np.array([35, 25, 25, 15])
          
         fig2 = plt.figure(facecolor='teal')
         fig2 =  plt.pie(y3)
         fig2=plt.ylabel("This is MY Y Axis")
         fig2=plt.xlabel("X Axis")
       #  fig2.set_facecolor("teal")
         self.ids.circle.add_widget(FigureCanvasKivyAgg(plt.gcf()))
################

      def clk(self):

          self.c = 0
          self.d = 0
          Clock.schedule_interval(self.increment, .05)

          self.increment(0)


      def increment(self, interval):
          self.c += 1
          self.d += 1
          print("increment number", self.c)
          print("increment number", self.d)
          self.ids.cpu.val = self.c
          self.ids.cpu.text = f'{self.c}%'
          self.ids.ram.val1 = self.d
          self.ids.ram.text = f'{self.d}%'

          if self.c == 360:
             Clock.unschedule(self.increment)
             self.clk()




sm = ScreenManager()

class TestApp(MDApp):

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Teal"

        self.theme_cls.accent_palette = "Red"
        sm.add_widget(login(name='menu'))
        sm.add_widget(login_sucess(name='sucess'))

        return sm



TestApp().run()
