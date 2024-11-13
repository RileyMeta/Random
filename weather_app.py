from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from dotenv import load_dotenv
from PyQt5.QtCore import Qt
import requests
import sys
import os



class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter a City Name: ", self)
        self.city_entry = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Riley's Weather App")
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_entry)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_entry.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_entry.setObjectName("city_entry")
        self.weather_button.setObjectName("weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_entry{
                font-size: 40px;
            }
            QPushButton#weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        city = self.city_entry.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request: Please double-check your input")
                case 401:
                    self.display_error("Unauthorized: Invalid API Key")
                case 403:
                    self.display_error("Forbidden: Access is Denied")
                case 404:
                    self.display_error("Not Found: City was not found")
                case 500:
                    self.display_error("Internal Server Error: Please try again later")
                case 502:
                    self.display_error("Bad Gateway: Invalid Response from Server")
                case 503:
                    self.display_error("Service Unvailable: Server is down")
                case 504:
                    self.display_error("Gateway Timeout: No response from the Server")
                case _:
                    self.display_error(f"HTTP Error Occured: {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: Check your Internet Connection")

        except requests.exceptions.Timeout:
            self.display_error("Time Out Error: The request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects: Please check the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)

        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        c_temperature = round(data["main"]["temp"] - 273.15, 2)
        f_temperature = round((9/5) * c_temperature + 32, 2)

        weather_id = data['weather'][0]["id"]
        weather_description = data["weather"][0]["description"]

        
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.temperature_label.setText(f"{f_temperature}°F")
        self.emoji_label.setText(self.display_emoji(weather_id))
        self.description_label.setText(weather_description)


    @staticmethod
    def display_emoji(weather_id):
        if 200 <= weather_id <= 232: 
            return "🌩️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌊"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
