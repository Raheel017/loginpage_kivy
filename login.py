from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import mysql.connector

class LoginUI(BoxLayout):
    pass


class LoginApp(App):

    database = mysql.connector.Connect(host='localhost', user='root', password ='Rahil@321', database='loginpage')
    cursor = database.cursor()
    

    def build(self):
        return LoginUI()
    
    def send(self, email, password):
        self.cursor.execute(f"insert into logindata values('{email.text}','{password.text}')")
        self.database.commit()
        #for i in self.cursor.fetchall():
            #print(i[0], i[1])


if __name__ == '__main__':
    login = LoginApp()
    Window.size=(397,697)
    login.run()