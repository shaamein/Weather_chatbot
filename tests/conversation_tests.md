#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## Atlanta
* greet: Hello
  - utter_greet
* inform: What is the weather in Atlanta?
  - action_weather
* thank: Thanks
  - utter_noworries
* bye: goodbye
  - utter_bye

## Athens
* greet: Hi
  - utter_greet
* inform: How is the weather in Athens?
  - action_weather
* thank: Thanks for that
  - utter_noworries
* bye: bye
  - utter_bye
