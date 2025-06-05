#display_image.py

from kivy.app import App
from kivy.uix.image import Image
from kivy.metrics import dp

class MainApp(App):
    def build(self):
        img = Image(source='./images/vende_facil.png',
                    #size_hint=(None, None),        # desactiva el auto‐redimensionado
                    #size=(dp(40), dp(40)) 
                    ) 
        
        return img
    
if __name__ == '__main__':
    app = MainApp()
    app.run()    