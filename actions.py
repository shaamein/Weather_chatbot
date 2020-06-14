# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet 

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
    	tracker: Tracker,

        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    	dispatcher.utter_message(text="Hello World!")

    	return []

class ActionWeather(Action):

    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
    	import requests

    	city = tracker.get_slot('location')
    	url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=<INSERT APIID HERE>'
    	res = requests.get(url)
    	data = res.json()
    	description = data['weather'][0]['description']
    	name = data['name']
    	temperature = data['main']['temp']
    	humidity = data['main']['humidity']
    	windspeed = data['wind']['speed']

    	response = (f'{name} have currently {description}. The temperature is {temperature} ' + 
			f'degrees, the humidity is {humidity}% and the wind speed is {windspeed} mph.')

    	dispatcher.utter_message(response)
    	return [SlotSet('location',city)]