
import requests
import json

# from speech_to_text_algorithm import *
# from pytimedinput import timedInput



######################################################## GET TRACKER

def get_tracker(headers):

    response = requests.get('http://localhost:5005/conversations/tester/tracker', headers=headers)

    if (response.status_code==200) and (response.headers["content-type"].strip().startswith("application/json")):
        print(response)
        print("tracker oook")
        my_json = response.content.decode('utf8').replace("'", '"')#.replace("\\", "\\\\")

        print("response ok")
        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        sender_id = data["sender_id"]
        slots = data["slots"]
        latest_message=data["latest_message"]
        events = data["events"]
        latest_action = data["latest_action"]
        followup_action = data["followup_action"]
        
        return sender_id, slots, latest_message, events, latest_action, followup_action

    else: 

        return [],[],[],[],[],[]


##################################### USER INPUT

def user_input(headers,message):

    #message=m.encode('utf-8')
    dct = {"sender": "tester", "message": message}
    data = json.dumps(dct, indent=True)
    response = requests.post('http://localhost:5005/webhooks/callback/webhook', headers=headers, data=data)	
	
    if response.status_code==200:
        print("response ok")
        # print(response.headers["content-type"].strip().startswith("application/json")) # einai false se autin tin periptwsi
        #get_tacker
        sender_id, slots, latest_message, events, latest_action, followup_action = get_tracker(headers)
	
        return sender_id, slots, latest_message, events, latest_action, followup_action 

    else:

        return [],[],[],[],[],[]


def trigger_intent(headers,data):

    response = requests.post('http://localhost:5005/conversations/tester/trigger_intent', headers=headers, data=data)

    if response.status_code==200:
        print(response)
        my_json = response.content.decode('utf8').replace("'", '"')
        
        #print(my_json)


        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        
        tracker = data["tracker"]
        messages= data["messages"]

        
        sender_id = tracker["sender_id"]
        slots = tracker["slots"]
        latest_message=tracker["latest_message"]
        events = tracker["events"]
        followup_action = tracker["followup_action"]
        latest_action = tracker["latest_action"]

        return sender_id, slots, latest_message, events, messages, latest_action, followup_action   

    else:

        return [],[],[],[],[],[],[]


def set_slot(headers,data):

    params = (('include_events', 'NONE'),)    
    #localhost rasa
    response = requests.post('http://localhost:5005/conversations/tester/tracker/events', params=params, headers=headers, data=data)    
    
    my_json = response.content.decode('utf8').replace("'", '"')

    if response.status_code==200:
        print("response ok")
        #get_tacker
        sender_id, slots, latest_message, events, latest_action, followup_action = get_tracker(headers)
    
        return sender_id, slots, latest_message, events, latest_action, followup_action

    else:

        return [],[],[],[],[],[]



def execute_action(headers,data):

    response = requests.post('http://localhost:5005/conversations/tester/execute', headers=headers, data=data)   

    if response.status_code==200: 
        print(response)
        my_json = response.content.decode('utf8').replace("'", '"')


        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        # tracker = data["tracker"]
        # messages= data["messages"]

        sender_id, slots, latest_message, events, latest_action, followup_action = get_tracker(headers)
        
        return sender_id, slots, latest_message, events, latest_action, followup_action

    else:

        return [],[],[],[],[],[]



def bot_response(events,len_bot_events_old):

    bot_events = [x for x in events if x["event"]=="bot"]
        
    diff = len(bot_events)-len_bot_events_old
    print(len(bot_events))
    print(len_bot_events_old)
    print(diff)
    len_bot_events_old = len(bot_events)

    bot_events = bot_events[-1:-1-diff:-1]
    
    bot_responses = [x["text"] for x in bot_events]
    # print(bot_responses)
    bot_responses = bot_responses[::-1]
    # print(bot_responses)

    return bot_responses, len_bot_events_old

def restart(headers):

    data = '{"name":"action_reset_slots"}'
    sender_id, slots, latest_message, events, latest_action, followup_action = execute_action(headers,data)
    
    len_bot_events_old = 0

    return len_bot_events_old



def talk_to_bot():
    

    headers = {'Content-type': 'application/json',}    
    len_bot_events_old = restart(headers)



    # data = '{"name":"action_set_slot_exhibit"}'
    # sender_id, slots, latest_message, events, latest_action, followup_action = execute_action(headers,data)


    # # ################## TRIGGER TO START #########################

    # data = '{"name": "intent_start_conversation"}'
    # sender_id, slots, latest_message, events, messages, latest_action, followup_action = trigger_intent(headers,data)

    # print('--'*10,'sender id','--'*10)
    # print(sender_id)
    # print('--'*10,'slots','--'*10)
    # print(slots)
    # print('--'*10,'latest message','--'*10)
    # print(latest_message)
    # print('--'*10,'latest action','--'*10)
    # print(latest_action)
    # print('--'*10,'messages','--'*10)
    # print(messages)
    # print('--'*10,'followup_action','--'*10)
    # print(followup_action)
    # print('--'*10,'events','--'*10)
    # for event in events:
    #     print('--'*10,'single event','--'*10)
    #     print(event)

    # print('--'*50)
    # bot_responses, len_bot_events_old = bot_response(events,len_bot_events_old) 
    # print('--'*10,'bot responses','--'*10)
    # for response in bot_responses:
    #     print(response)

    duration = 20 #seconds
    while True:

        ##################################### USER INPUT ################################
            # message, timedOut = timedInput("περιμένω user input: ",duration)
            message = input("user input: ")
            #beep
            # message = speech_to_text(duration)  #duration is how much time wait//2*duration total length of speech
            #beep

            if message=="exit":
                break
            
            if not message:
                message="Σιωπή"

            sender_id, slots, latest_message, events, latest_action, followup_action = user_input(headers,message)

            print('--'*10,'sender id','--'*10)
            print(sender_id)
            print('--'*10,'slots','--'*10)
            print(slots)
            print('--'*10,'latest message','--'*10)
            print(latest_message)
            print('--'*10,'latest action','--'*10)
            print(latest_action)
            print('--'*10,'followup_action','--'*10)
            print(followup_action)
            print('--'*10,'events','--'*10)
            for event in events:
                print('--'*10,'single event','--'*10)
                print(event)

            
            print('--'*50)   
            bot_responses, len_bot_events_old = bot_response(events,len_bot_events_old) 
            print('--'*10,'bot responses','--'*10)
            for response in bot_responses:
                print(response)

            print('--'*10,'slots','--'*10)
            print(slots)


def talk_to_bot_via_rest():
    

    headers = {'Content-type': 'application/json',}    
    


    while True:

        ##################################### USER INPUT ################################

        message = input("user input: ")
        

        if message=="exit":
            break

            #message=m.encode('utf-8')
        dct = {"sender": "tester", "message": message}
        data = json.dumps(dct, indent=True)
        response = requests.post('http://localhost:5005/webhooks/rest/webhook', headers=headers, data=data)	
        print(response)
        # 
        print(response.headers)
        if (response.status_code==200) and (response.headers["content-type"].strip().startswith("application/json")):
            print("response ok")
            my_json = response.content.decode('utf8').replace("'", '"')
        
            # Load the JSON to a Python list & dump it back out as formatted JSON
            data = json.loads(my_json)
            for bot_message in data:
                recipient_id = bot_message["recipient_id"]
                text = bot_message["text"]
                print("'" + recipient_id +"': " + text)
            



if __name__ == "__main__":
    talk_to_bot()
    # talk_to_bot_via_rest()

    







