## happy path 1 (C:\Users\sherm\AppData\Local\Temp\tmpod8hdmu4\8ecdb7b2adc144b183f8e805002c4e9d_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->


## Atlanta (C:\Users\sherm\AppData\Local\Temp\tmpod8hdmu4\8ecdb7b2adc144b183f8e805002c4e9d_conversation_tests.md)
* greet: Hello
    - utter_greet
* inform: What is the weather in Atlanta?   <!-- predicted: inform: What is the weather in [Atlanta](location)? -->
    - slot{"location": "Atlanta"}
    - action_weather   <!-- predicted: action_listen -->
* thank: Thanks
    - utter_noworries   <!-- predicted: action_listen -->
* bye: goodbye
    - utter_bye


## Athens (C:\Users\sherm\AppData\Local\Temp\tmpod8hdmu4\8ecdb7b2adc144b183f8e805002c4e9d_conversation_tests.md)
* greet: Hello
    - utter_greet
* inform: How is the weather in Athens?   <!-- predicted: inform: How is the weather in [Athens](location)? -->
    - slot{"location": "Athens"}
    - action_weather   <!-- predicted: action_listen -->
* thank: Thanks
    - utter_noworries   <!-- predicted: action_listen -->
* bye: goodbye
    - utter_bye


