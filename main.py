import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class PhoneNumberInfoApp(App):
    def build(self):
        self.title = "Phone Number Info"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.background = Widget()
        with self.background.canvas:
            Color(0, 0, 1, 1)  # Blue color
            self.rect = Rectangle(size=(self.layout.width, self.layout.height), pos=self.layout.pos)

        self.phone_input = TextInput(hint_text="Enter your Phone number with +__", size_hint=(None, None), size=(300, 50))
        self.info_button = Button(text="Get Info", size_hint=(None, None), size=(150, 50))
        self.result_label = Label(text="Result will be displayed here.", halign='center')

        self.layout.add_widget(self.background)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(self.info_button)
        self.layout.add_widget(self.result_label)

        self.info_button.bind(on_release=self.get_phone_info)

        return self.layout

    def get_phone_info(self, instance):
        phone_number = self.phone_input.text
        try:
            parsed_phone = phonenumbers.parse(phone_number)
            time_zones = timezone.time_zones_for_number(parsed_phone)
            carrier_name = carrier.name_for_number(parsed_phone, "en")
            region = geocoder.description_for_number(parsed_phone, "en")

            result = f"Phone Number: {phone_number}\n"
            result += f"Time Zone: {', '.join(time_zones)}\n"
            result += f"Carrier: {carrier_name}\n"
            result += f"Region: {region}"

            self.result_label.text = result
        except phonenumbers.phonenumberutil.NumberFormatException:
            self.result_label.text = "Invalid Phone Number"

if __name__ == '__main__':
    PhoneNumberInfoApp().run()
