import requests
import json
import time
from speech_algorithm_for_rasa import *
from play_sound import *

def talk_to_bot_via_rest():


    beep_file = "beep.wav"

    headers = {'Content-type': 'application/json',}
    while True:
        try:
            dct = {"sender": "tester", "message": "γεια"}
            data = json.dumps(dct, indent=True)
            response = requests.post('http://localhost:5005/webhooks/rest/webhook', headers=headers, data=data)	#rasa localhost


            if (response.status_code==200) and (response.headers["content-type"].strip().startswith("application/json")):

                my_json = response.content.decode('utf8').replace("'", '"')

                # Load the JSON to a Python list & dump it back out as formatted JSON
                data = json.loads(my_json)
                for bot_message in data:
                    recipient_id = bot_message["recipient_id"]
                    text = bot_message["text"]
                    print("'" + recipient_id +"': " + text)
                    text_to_speech(text)

                break

            # response = requests.get('http://localhost:5005', headers=headers) #rasa localhost
            # if (response.status_code==200):
            #     break

        except:
            print("failed")
        time.sleep(1)

    print("bgika")
    duration = 15
    while True:

        ##################################### USER INPUT ################################
        print("bika")
        #message = input("user input: ")
        #play_sound(beep_file)
        try:
            message, flag = speech_to_text()  #duration is how much time wait//2*duration total length of speech
        except:
            print("error exception caught")
            continue

        flag = True
        if flag:
            # play_sound(beep_file)

            if message=="έξοδος":
                break

                #message=m.encode('utf-8')
            dct = {"sender": "tester", "message": message}
            data = json.dumps(dct, indent=True)
            response = requests.post('http://localhost:5005/webhooks/rest/webhook', headers=headers, data=data)	#rasa localhost
            # print(response)
            # #
            # print(response.headers)
            if (response.status_code==200) and (response.headers["content-type"].strip().startswith("application/json")):
                # print("response ok")
                my_json = response.content.decode('utf8').replace("'", '"')

                # Load the JSON to a Python list & dump it back out as formatted JSON
                data = json.loads(my_json)
                for bot_message in data:
                    recipient_id = bot_message["recipient_id"]
                    text = bot_message["text"]
                    print("'" + recipient_id +"': " + text)
                    text_to_speech(text)

        else:

            text_to_speech(message)



if __name__ == "__main__":
    talk_to_bot_via_rest()
