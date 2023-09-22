#You can just copy and pasta this to quickly make an animated button upon click.
#Firstly button does in_out_bounce animation within kivy and then it's size grows to give it a good look and then,
#It goes to original size.
#Before copying this python stuff, remember to actually creat AnimatedRaisedButton named button in kv file.

#Made by Berk Öcal, Linkedin: www.linkedin.com/in/berkocall/
#Gmail: berkocal99@gmail.com you can communucate with me via mail or via my linkedin account.

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.animation import Animation
from kivymd.uix.button import MDRaisedButton

class AnimatedRaisedButton(MDRaisedButton, Animation):  # MDRaisedButton is animated here. You can change the inheration to what button you want to make.
    def on_release(self):
        original_size = self.size  # Store the original size
        animation = Animation(size=(90, 55), transition="in_out_bounce", d=0.3) + Animation(size=(80, 45), transition="in_out_bounce", d=0.3)
        animation.bind(on_complete=self.reset_button)
        animation.start(self)  ##You must change the size according to your button's size first and then at the second size alteration make it close to the original one but lesser.(That's important)

    def reset_button(self, *args):
        self.size = (80, 45)  # Reset the button size to its original value. Remember to write here your original button size or animation wont work. You can learn it via print(self.size)

class MahApp(MDApp, database):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.secondary_palette = "Amber"
        self.theme_cls.material_style = "M2"
        return Builder.load_file('my.kv')

MahApp().run()