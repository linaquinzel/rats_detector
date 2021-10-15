import kivy
from kivy.app import App
from kivy.uix.button import Button
from face_detector.py import rats_detector


# класс, в котором мы создаем кнопку
class ButtonApp(App):

    def build(self):
        btn = Button(text="Push Me!")
        btn.bind(on_press = rats_detector)
        return btn

  
# создание корня объекта для класса ButtonApp ()

root = ButtonApp()

  
# run функция запускает всю программу
# т.е. метод run (), который вызывает
# целевая функция передается конструктору.
root.run()