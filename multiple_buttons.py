#multipple_buttons.py

import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


red=[1,0,0,1]
green=[0,1,0,1]
blue=[0,0,1,1]
purple=[1,0,1,1]
colors=[red, green, blue, purple]

class HBoxLayoutExample(App):
    def build(self):
        layout =  BoxLayout(padding=10)
        
        for i in range(5):
            btn=Button(text=f"Button #{i+1}",
                       background_color=random.choice(colors)
            )
            
            btn.index = i+1   
            btn.bind(on_press=self.on_press_button) 
                    
            layout.add_widget(btn)
            
        return layout    
    
    def on_press_button(self, instance):
        print(f"Presiona Botón #{instance.index}")

if __name__ == '__main__':
    app = HBoxLayoutExample()
    app.run()