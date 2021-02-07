import kivy 
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App 
from kivy.uix.button import Button 

kivy.require("1.9.1")  
# class in which we are creating the button 
class CatApp(App): 
      
    def build(self):
        layout=BoxLayout(orientation='vertical') 

        self.btn = Button(text ="Cat Facts!",bold=True,font_size='30sp',
        background_normal='images/cat.jpg',
        background_down='CatFacts\images\cat_pressed.jpg')
        
        cat_facts = ['cats like to eat',
        'cats like to knock things down',
        'cats like to play',
        'Cats can jump up to six times their length.',
        '''Cats are believed to be the only 
           mammals who don’t taste sweetness.''',
        'Cats dream, just like people do.',
        '''Cats are crepuscular, which means that they’re 
           most active at dawn and dusk.'''
        ]
      
        catLabel = Label(text=str(random.choice(cat_facts)), 
        font_size='30sp',bold=True,color=[.5,.7,.7,.7])
        layout.add_widget(self.btn)
        layout.add_widget(catLabel)

        def callback(self):
            catLabel.text = random.choice(cat_facts)

        self.btn.bind(on_press=callback)
        return layout

if __name__ == '__main__':
    app = CatApp()
    app.run()