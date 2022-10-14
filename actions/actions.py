# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from os import remove
from typing import Any, Text, Dict, List, Union
from urllib import response
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ReminderScheduled, FollowupAction, UserUttered
from rasa_sdk.forms import FormValidationAction, ValidationAction
from rasa_sdk.types import DomainDict


import random


class ActivateExhibitForm(Action):
    def name(self) -> Text:
        return "action_iterate_form_exhibit"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print("action_iterate_form_exhibit")
        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        slot_exhibit = tracker.slots.get("slot_exhibit")
        silence_count = tracker.slots.get("slot_silence_count")
        remaining_exhibits = tracker.slots.get("slot_remaining_exhibits")
        available_exhibits = tracker.slots.get("slot_available_exhibits")
        


        if len(slot_list_exhibit_utters)==0:

            flag_exhibit_utters = True
            dispatcher.utter_message(response="utter_exhibit_finish")

            index = available_exhibits.index(slot_exhibit)  
            slot_list_available_exhibit_utters = tracker.slots.get("slot_list_available_exhibit_utters")  
            slot_list_exhibit_utters = slot_list_available_exhibit_utters[index] 

            if (len(remaining_exhibits)==0):

                dispatcher.utter_message(response="utter_was_last_exhibit")
                return [SlotSet("slot_list_exhibit_utters",slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_previous_exhibit", slot_exhibit),  SlotSet("slot_interested", None), SlotSet("slot_exhibit", None), FollowupAction("form_exhibit")]
        
            dispatcher.utter_message(response="utter_suggest_move_exhibit")
            return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_previous_exhibit", slot_exhibit),  SlotSet("slot_interested", "change"), SlotSet("slot_exhibit", None), FollowupAction("form_exhibit")]
        
        elif ((len(slot_list_exhibit_utters) <= 4) and (len(slot_list_exhibit_utters)%2 ==0)): # or (silence_count>=2):        
            
            flag_exhibit_utters = False
            if (len(remaining_exhibits)==0):

                dispatcher.utter_message(response="utter_is_last_exhibit")
                return [SlotSet("slot_list_exhibit_utters",slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_previous_exhibit", slot_exhibit), SlotSet("slot_interested", None), SlotSet("slot_exhibit", None), FollowupAction("form_exhibit")] #pame sto epomeno ekthema
            
            dispatcher.utter_message(response="utter_exhibit_utters_enough")
            return [SlotSet("slot_list_exhibit_utters",slot_list_exhibit_utters), SlotSet("flag_exhibit_utters",flag_exhibit_utters), SlotSet("slot_previous_exhibit", slot_exhibit), SlotSet("slot_interested", None), SlotSet("slot_exhibit", None), FollowupAction("form_exhibit")] #pame sto epomeno ekthema

        else:
            flag_exhibit_utters = False
            return [SlotSet("flag_exhibit_utters",flag_exhibit_utters), FollowupAction("action_listen")]


class SayExposition(Action):
    def name(self) -> Text:
        return "action_say_exposition"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_exposition")

        else: 
        
            dispatcher.utter_message(response="utter_say_exposition")
            dispatcher.utter_message(response="utter_say_capabilities")
        
        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]





class SayImportance(Action):
    def name(self) -> Text:
        return "action_say_importance"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_importance")

        else: 
        
            dispatcher.utter_message(response="utter_say_importance")
            dispatcher.utter_message(response="utter_say_capabilities")


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]



class SayLanguage(Action):
    def name(self) -> Text:
        return "action_say_language"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter)  
        
            dispatcher.utter_message(response="utter_say_language")

        else: 
        
            dispatcher.utter_message(response="utter_say_language")
            dispatcher.utter_message(response="utter_say_capabilities")

        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayWriter(Action):
    def name(self) -> Text:
        return "action_say_writer"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_writer")
        else: 
        
            dispatcher.utter_message(response="utter_say_writer")
            dispatcher.utter_message(response="utter_say_capabilities")


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayCreation(Action):
    def name(self) -> Text:
        return "action_say_creation"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter) 
        
            dispatcher.utter_message(response="utter_say_creation")

        else: 
        
            dispatcher.utter_message(response="utter_say_creation")
            dispatcher.utter_message(response="utter_say_capabilities")


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayContent(Action):
    def name(self) -> Text:
        return "action_say_content"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter)
        
            dispatcher.utter_message(response="utter_say_content")

        else: 
        
            dispatcher.utter_message(response="utter_say_content")
            dispatcher.utter_message(response="utter_say_capabilities")


        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class SayFinding(Action):
    def name(self) -> Text:
        return "action_say_finding"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        slot_list_exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        exhibit_utters = [ x[6:] for x  in slot_list_exhibit_utters]
        print(exhibit_utters)
        name = self.name()
        if name[7:] in exhibit_utters:
            delete_utter = "utter_" + name[7:]
            slot_list_exhibit_utters.remove(delete_utter)


            dispatcher.utter_message(response="utter_say_finding")

        else: 
        
            dispatcher.utter_message(response="utter_say_finding")
            dispatcher.utter_message(response="utter_say_capabilities")

        return [SlotSet("slot_list_exhibit_utters", slot_list_exhibit_utters), FollowupAction("action_iterate_form_exhibit")]




class Introduce(Action):
    def name(self) -> Text:
        return "action_introduce"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        dispatcher.utter_message(response="utter_introduce")
        return []


class SayBye(Action):
    def name(self) -> Text:
        return "action_say_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        dispatcher.utter_message(response="utter_say_goodbye")
        return [AllSlotsReset(),Restarted()]

class SayThanks(Action):
    def name(self) -> Text:
        return "action_say_thanks"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        dispatcher.utter_message(response="utter_say_thanks")
        return []

class SayThanksDeny(Action):
    def name(self) -> Text:
        return "action_say_thanks_deny"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print('thanks')
        dispatcher.utter_message(response="utter_say_thanks_deny")
        # return [FollowupAction("action_reset_slots")]
        return []



class ValidateForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_user"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:

        updated_slots = domain_slots.copy()
        if tracker.slots.get("slot_adult") == True:
            updated_slots.remove("slot_favorite_subject")
        print(updated_slots)
        filled_slots = [x for x in updated_slots if tracker.slots.get(x)!=None] 
        print(filled_slots)
        if len(filled_slots)==len(updated_slots): 
            updated_slots=[] 

        return updated_slots


    def validate_slot_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print("validate_slot_name")
        # If the name is super short, it might be wrong.
        # print(f"Name given = {slot_value} length = {len(slot_value)}")

        remind_slot = tracker.slots.get("remind_slot")    
        if remind_slot == "slot_name":
            remind_slot = None 

        if slot_value == "noentity":

            return {"slot_name": None, "previous_requested_slot": "slot_name", "remind_slot": remind_slot}

        else:
            return {"slot_name": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot}


    def validate_slot_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        print("validate_slot_age")
        
        remind_slot = tracker.slots.get("remind_slot")    
        if remind_slot == "slot_age":
            remind_slot = None

        if slot_value=="noentity":
            return {"slot_age": None, "previous_requested_slot": "slot_age", "remind_slot": remind_slot}

        # if slot_value=="-":
        #     return {"slot_age": slot_value, "previous_requested_slot": None, "remind_slot": None}

        try: 
            slot_value = float(slot_value)
        except:
            print("No number provided")
            return {"slot_age": None, "remind_slot": remind_slot}

        if (int(slot_value) <= 2) or (int(slot_value) >= 100):
            #dispatcher.utter_message(text=f"Number should be 10 digits long.")
            dispatcher.utter_message(text=f"Η ηλικία σου δεν είναι έγκυρη")
            return {"slot_age": None, "remind_slot": remind_slot}
        else:

            dispatcher.utter_message(response="utter_say_my_age")
            if (slot_value<=18):               
                
                return {"slot_age": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot, "slot_adult":False}
            else:               
                
                return {"slot_age": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot, "slot_adult": True}


    def validate_slot_occupation(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
            print("validate_slot_occupation")
            remind_slot = tracker.slots.get("remind_slot")    
            if remind_slot == "slot_occupation":
                remind_slot = None

            if slot_value==None:
                return {"slot_occupation": None, "remind_slot": remind_slot}

            else:
                return {"slot_occupation": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot}




    def validate_slot_favorite_subject(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
            print("validate_slot_favorite_subject")
            remind_slot = tracker.slots.get("remind_slot")    
            if remind_slot == "slot_favorite_subject":
                remind_slot = None

            if slot_value=="noentity":
                return {"slot_favorite_subject": None, "previous_requested_slot": "slot_favorite_subject", "remind_slot": remind_slot}

            else:
                return {"slot_favorite_subject": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot}








class ActionSetSlotName(Action):
    def name(self):
        return "action_set_slot_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_name")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        entities = latest_message["entities"]

        if intent == "intent_name":

            
            if len(entities)>=1:  #an einai kai ta dio i mono to ena tha ksekinisiw stin tixi apo kapoio
                if (entities[0].get("entity")=="PERSON") or (entities[0].get("entity")=="entity_name"):
                    name_value = entities[0].get("value")
                    # print("intent name entity person")
                    return [SlotSet("slot_name", name_value)]
                else:
                    text = latest_message["text"]
                    return [SlotSet("slot_name", text)]
            else:
                text = latest_message["text"]
                return [SlotSet("slot_name", text)]   

            # elif len(entities)==0:  #edw na balw na ksanarwtisi mono to onoma
            #     print("no entities") 
                
            #     # dispatcher.utter_message(response="utter_say_only_name") #δεν κανει το πριντ
            #     return [SlotSet("slot_name", "noentity")]



        elif tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot=="slot_name":
                

                if intent == "nlu_fallback":
            
                    if len(entities)>=1:  
                        if (entities[0].get("entity")=="PERSON"):
                            name_value = entities[0].get("value")
                            return [SlotSet("slot_name", name_value)]

                        else:
                            text = latest_message["text"]
                            return [SlotSet("slot_name", text)]
                    
                    else:
                        text = latest_message["text"]
                        return [SlotSet("slot_name", text)]


                else: #if (intent!="intent_silence"): 

                    #elpizw se rule
                    return [SlotSet("remind_slot", "slot_name"), SlotSet("previous_requested_slot", None)]



class ActionSetSlotAge(Action):

    def name(self):
        return "action_set_slot_age"

    def run(self, dispatcher, tracker, domain):
        print("action_set_slot_age")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        
        if intent == "intent_age":

            entities = latest_message["entities"]
            if len(entities)>=1:  #an einai kai ta dio i mono to ena tha ksekinisiw stin tixi apo kapoio
                if (entities[0].get("entity")=="entity_age"):
                    age_value = entities[0].get("value")
                    return [SlotSet("slot_age", age_value)]
                else:
                    return [SlotSet("slot_age", "noentity")]
            else:
                return [SlotSet("slot_age", "noentity")]


        elif tracker.active_loop.get("name")=="form_user":
           
            requested_slot = tracker.slots.get("requested_slot")

            if requested_slot=="slot_age":

                # previous_requested_slot = tracker.slots.get("previous_requested_slot")

                if (intent == "nlu_fallback"): 

                    text = latest_message["text"]
                    return [SlotSet("slot_age", text)]

                else: 
                    return [SlotSet("remind_slot", "slot_age"), SlotSet("previous_requested_slot", None)]


class ActionSetSlotOccupation(Action):
    def name(self):
        return "action_set_slot_occupation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_occupation")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        entities = latest_message["entities"]

        if intent == "intent_occupation":
            
            if len(entities)>=1:  #an einai kai ta dio i mono to ena tha ksekinisiw stin tixi apo kapoio
                # if (entities[0].get("entity")=="entity_occupation"):
                occupation_value = entities[0].get("value") #eimai dikigoros to ebgaze person
                return [SlotSet("slot_occupation", occupation_value)]
            
            else:
                text = latest_message["text"]
                return [SlotSet("slot_occupation", text)]

        elif tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot=="slot_occupation":
        
                if (intent == "nlu_fallback") or (intent=="intent_deny"):
                    
                    if len(entities)>=1:  
                        if (entities[0].get("entity")=="entity_occupation"):
                            occupation_value = entities[0].get("value")
                            return [SlotSet("slot_occupation", occupation_value)]
                        
                        else:
                            text = latest_message["text"]
                            return [SlotSet("slot_occupation", text)]
                    else:

                        text = latest_message["text"]
                        return [SlotSet("slot_occupation", text)]

                else:  
                    
                    return [SlotSet("remind_slot", "slot_occupation"), SlotSet("previous_requested_slot", None)]



class ActionSetSlotFavoriteSubject(Action):
    def name(self):
        return "action_set_slot_favorite_subject"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_favorite_subject")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        entities = latest_message["entities"]

        if intent == "intent_subject":
            
            if len(entities)>=1:  #an einai kai ta dio i mono to ena tha ksekinisiw stin tixi apo kapoio
                subject_entities = [x.get("value") for x in entities if x.get("entity")== "entity_subject" ]
                return [SlotSet("slot_favorite_subject", subject_entities)]            
                
            else:

                text = latest_message["text"]
                return [SlotSet("slot_favorite_subject", text)]
                

        elif tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot=="slot_favorite_subject":
                
                if intent == "intent_deny":
                    return [SlotSet("slot_favorite_subject", "Κανένα")]
                elif intent == "intent_all":
                    return [SlotSet("slot_favorite_subject", "Όλα")]

                elif intent == "nlu_fallback":
                    
                    if len(entities)>=1:  
                        if (entities[0].get("entity")=="entity_subject"):
                            subject_value = entities[0].get("value")
                            return [SlotSet("slot_favorite_subject", subject_value)]

                        else:
                            text = latest_message["text"]
                            return [SlotSet("slot_favorite_subject", text)]

                    else:
                        text = latest_message["text"]
                        return [SlotSet("slot_favorite_subject", text)]

                else:  
                    
                    return [SlotSet("remind_slot", "slot_favorite_subject"), SlotSet("previous_requested_slot", None)]

















class ValidateFormExhibit(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_exhibit"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:

        updated_slots = domain_slots.copy()
        if tracker.slots.get("slot_interested") == "stop":
            updated_slots.remove("slot_exhibit")
            
            # dispatcher.utter_message(response="utter_say_thanks_deny")

            
        return updated_slots



    def validate_slot_interested(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        print("validate_interested")
        proper_values = ["change", "no_change", "stop"]
        
        remind_slot = tracker.slots.get("remind_slot")    
        if remind_slot == "slot_interested":
            remind_slot = None

        if slot_value in proper_values:
            
            return {"slot_interested": slot_value, "previous_requested_slot": None, "remind_slot": remind_slot}
       
        else:
            # dispatcher.utter_message(text=f"Επαναλαμβάνω")
            return {"slot_interested": None, "remind_slot": remind_slot}


  
       

    def validate_slot_exhibit(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        exhibits = tracker.slots.get("slot_available_exhibits")
        remaining_exhibits = tracker.slots.get("slot_remaining_exhibits")

        remind_slot = tracker.slots.get("remind_slot")    
        if remind_slot == "slot_exhibit":
            remind_slot = None

        print("validate_exhibit")
        if slot_value=="noentity":
            
            return {"slot_exhibit": None, "previous_requested_slot": "slot_exhibit", "remind_slot": remind_slot}

        # elif slot_value=="-":
        #     # dispatcher.utter_message(response="utter_say_thanks_deny")
        #     return {"requested_slot": None}

        elif (slot_value=="random") or (slot_value=="all"):
            
            # slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
            
            # if (slot_previous_exhibit!=None) and (slot_previous_exhibit in remaining_exhibits):
            #     remaining_exhibits.remove(slot_previous_exhibit)
            if len(remaining_exhibits)==0:
                rand_index = random.randint(0, len(exhibits)-1)
                random_choice = exhibits[rand_index]
            else:
                rand_index = random.randint(0, len(remaining_exhibits)-1)
                random_choice = remaining_exhibits[rand_index]
            
            slot_list_available_exhibit_utters = tracker.slots.get("slot_list_available_exhibit_utters")  
            slot_list_exhibit_utters = slot_list_available_exhibit_utters[rand_index]

            
            if random_choice in remaining_exhibits:
                remaining_exhibits.remove(random_choice)
            
            dispatcher.utter_message(response="utter_say_current_exhibit")
            return {"slot_exhibit": random_choice, "slot_previous_exhibit":random_choice, "slot_remaining_exhibits":remaining_exhibits, "slot_list_exhibit_utters":slot_list_exhibit_utters, "previous_requested_slot": None, "remind_slot": remind_slot}

        # elif slot_value == "-":
        #     return {"slot_exhibit": None} 

        
        
        if (slot_value!=None) and (slot_value.lower() in exhibits):
            
            slot_interested = tracker.slots.get("slot_interested")
            if slot_interested == "change":
                
                index = exhibits.index(slot_value.lower())  
                slot_list_available_exhibit_utters = tracker.slots.get("slot_list_available_exhibit_utters")  
                slot_list_exhibit_utters = slot_list_available_exhibit_utters[index]             
            
                # slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")            
                # if (slot_previous_exhibit!=None) and (slot_previous_exhibit in remaining_exhibits):
                #     remaining_exhibits.remove(slot_previous_exhibit)


                if slot_value in remaining_exhibits:
                    remaining_exhibits.remove(slot_value)
            
            
                return {"slot_exhibit": slot_value, "slot_previous_exhibit": slot_value, "slot_remaining_exhibits":remaining_exhibits, "slot_list_exhibit_utters":slot_list_exhibit_utters, "previous_requested_slot": None, "remind_slot": remind_slot}
            
            return {"slot_exhibit": slot_value, "slot_previous_exhibit": slot_value,  "previous_requested_slot": None, "remind_slot": remind_slot}

        elif (slot_value==None) or (slot_value=="-"):
            print("slot_exhibit - none")
            return {"slot_exhibit": None, "remind_slot": remind_slot}
        else:
            # validation failed, set this slot to None so that the user will be asked for the slot again
            #dispatcher.utter_message(text="There is not such exhibit in our database")
            dispatcher.utter_message(response="utter_try_again_exhibit")
            return {"slot_exhibit": None, "remind_slot": remind_slot}  





class ActionSetSlotInterested(Action):
    def name(self):
        return "action_set_slot_interested"

    def run(self, dispatcher, tracker, domain):
        print("set_interested")
        requested_slot = tracker.slots.get("requested_slot")
        tracker_name = tracker.active_loop.get("name")
        
        flag_form = ( (tracker_name=="form_exhibit") and (requested_slot=="slot_interested"))
        

        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")

        list_intents = tracker.slots.get("slot_list_intents")
        change_intents = ["intent_exhibit", "intent_change_exhibit" ]
        no_change_intents = ["intent_no_change_exhibit"]
        stop_intents = ["intent_stop_tour"]

        if (intent in change_intents) or ((flag_form) and intent=="intent_affirm") or ((flag_form) and intent=="intent_whatever"):
            
            return [SlotSet("slot_interested", "change")]

        elif (intent in no_change_intents) and flag_form: 
            slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
            return [SlotSet("slot_interested", "no_change"), SlotSet("slot_exhibit", slot_previous_exhibit)]

        elif (intent in stop_intents) or ((flag_form) and intent=="intent_deny"):
            
            return [SlotSet("slot_interested", "stop")]

        elif ((flag_form) and intent in list_intents):
            slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
            return [SlotSet("slot_interested", "no_change"), SlotSet("slot_exhibit", slot_previous_exhibit)]

        elif flag_form: #simainei anagnwrise kapoio allo intnent opote elpizw na iparxei se rule meta tha epistrepsei se erwtisi gia to interested
            return [SlotSet("slot_interested", None), SlotSet("remind_slot", "slot_interested"), SlotSet("previous_requested_slot", None)]




class ActionSetSlotExhibit(Action):
    def name(self):
        return "action_set_slot_exhibit"

    def run(self, dispatcher, tracker, domain):
        print("set_exhibit")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")

        requested_slot = tracker.slots.get("requested_slot")
        tracker_name = tracker.active_loop.get("name")
        flag_form = ( (tracker_name=="form_exhibit") and (requested_slot=="slot_exhibit"))
        
        if intent == "intent_exhibit":

            entities = latest_message["entities"]
            
            if len(entities)==1:  #an einai kai ta dio i mono to ena tha ksekinisiw stin tixi apo kapoio
                if (entities[0].get("entity")=="entity_exhibit"):
                    exhibit_value = entities[0].get("value")                   
                    
                    
                    return [SlotSet("slot_interested", "change"), SlotSet("slot_exhibit", exhibit_value)]
                
            elif len(entities)==0:
                
                return [SlotSet("slot_interested", "change"), SlotSet("slot_exhibit", "noentity")]
            else:
                exhibit_values = [x.get("value") for x in entities if x.get("entity")=="entity_exhibit"]               
                if ("πάπυρος" in exhibit_values) and ("χρυσός" in exhibit_values):
                    return [SlotSet("slot_interested", "change"),SlotSet("slot_exhibit", 'all')]
            
        elif (intent=="intent_no_change_exhibit") and (flag_form):

            slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
            return [SlotSet("slot_interested", "no_change"), SlotSet("slot_exhibit", slot_previous_exhibit)]

        elif flag_form:

            if (intent == "intent_whatever") or (intent == "intent_all"):
                
                return [SlotSet("slot_interested", "change"),SlotSet("slot_exhibit", 'random')]

            elif (intent == "intent_deny"):

                return [SlotSet("slot_interested", "change"),SlotSet("slot_exhibit", 'nada')]

            elif (intent!="nlu_fallback") and (intent != "intent_say_available_exhibits"):
                #simainei anagnwrise kapoio allo intnent opote elpizw na iparxei se rule meta tha epistrepsei se erwtisi gia to interested
                return [SlotSet("slot_interested", "change"),SlotSet("remind_slot", "slot_exhibit"), SlotSet("previous_requested_slot", None)]        
        
        





class ResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        dispatcher.utter_message(response="utter_reset_slots")
        
        return [AllSlotsReset(),Restarted()]


class AbortResetSlots(Action):
    def name(self) -> Text:
        return "action_abort_reset"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:
        print("abort")
        dispatcher.utter_message(response="utter_abort_reset")
       
        return [FollowupAction("form_user")]


class AskConfirmationToResetSlots(Action):
    def name(self) -> Text:
        return "action_ask_confirmation_to_reset"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        
        dispatcher.utter_message(response="utter_ask_confirmation_to_reset")

        return []



class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

 
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        print("action_fallback")
        if tracker.active_loop.get("name")=="form_user":                
            requested_slot = tracker.slots.get("requested_slot")
            if (requested_slot=="slot_name") or (requested_slot=="slot_age"):
                return [SlotSet("slot_fallback_count", 0)] #me auton ton tropo mporei na parei to text 
                #apo ta slots xwris na emfanizei to fallback kai to count +1
        print("action_fallback")
        fallback_count = tracker.slots.get("slot_fallback_count")
        fallback_count = fallback_count + 1
        
        print("nlu_fallback")
        print(fallback_count)

        events = tracker.events
        bot_events = [x for x in events if x["event"]=="bot"]
            
        

        if fallback_count==1: #simainei oti prwti fora den katalave
            
            dispatcher.utter_message(response="utter_fallback_1st_time") #+ na ξανακανει την ερωτηση
            
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot!=None:
                bot_events = [x for x in events if x["event"]=="bot"]
                bot_event = bot_events[-1]
                bot_response = bot_event["text"]
                dispatcher.utter_message(text=bot_response)
            else:
                dispatcher.utter_message(response = "utter_say_capabilities")

            return [UserUtteranceReverted(), SlotSet("slot_fallback_count", fallback_count), SlotSet("previous_requested_slot", None),SlotSet("slot_silence_count",0)]

        elif fallback_count==2: #simainei oti deuteri fora den katalave
            
            dispatcher.utter_message(response="utter_fallback_2nd_time") #+ na ξανακανει την ερωτηση
           
            requested_slot = tracker.slots.get("requested_slot")
            if requested_slot!=None:
                bot_events = [x for x in events if x["event"]=="bot"]
                bot_event = bot_events[-1]
                bot_response = bot_event["text"]
                dispatcher.utter_message(text=bot_response)
            else:

                exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")           

                if (len(exhibit_utters)!=0):

                    i = random.randint(0, len(exhibit_utters)-1 )	
                    selected_utter=exhibit_utters[i]
                    exhibit_utters.pop(i)

                    dispatcher.utter_message(response = "utter_say_following")
                    dispatcher.utter_message(response=selected_utter)
                
                    return [UserUtteranceReverted(),  SlotSet("slot_fallback_count", fallback_count), SlotSet("slot_silence_count",0), SlotSet("previous_requested_slot", None), FollowupAction("action_iterate_form_exhibit")]
                
            return [UserUtteranceReverted(), SlotSet("slot_fallback_count", fallback_count), SlotSet("previous_requested_slot", None),SlotSet("slot_silence_count",0)]

        elif fallback_count==3:

            dispatcher.utter_message(response="utter_fallback_3rd_time")
            return [AllSlotsReset(),Restarted()]





class ActionSetSlotFallback(Action):
    def name(self):
        return "action_set_slot_fallback_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        

        if intent != "nlu_fallback":

            fallback_count  = 0
            # print("not_nlu_fallback")
            # print(fallback_count)

        
            return [SlotSet("slot_fallback_count", fallback_count)]
        
        return []



class ActionSetPreviousRequested(Action):
    def name(self):
        return "action_set_previous_requested_slot"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
                
        return []


class ActionSetPreviousExhibit(Action):
    def name(self):
        return "action_set_slot_previous_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
                
        return []

class ActionSetRemindSlot(Action):
    def name(self):
        return "action_set_remind_slot"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
                
        return []




class ActionReactToSilence(Action):
    

    def name(self) -> Text:
        return "action_react_to_silence"


    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:

        print("react_to_silence")
        silence_count = tracker.slots.get("slot_silence_count")
        silence_count = silence_count + 1

        requested_slot = tracker.slots.get("requested_slot")
        slot_exhibit = tracker.slots.get("slot_exhibit")

        if (requested_slot!=None) and (requested_slot!="slot_exhibit"):

            if (silence_count<3):
                dispatcher.utter_message(response="utter_react_to_silence_1st")

                events = tracker.events
                bot_events = [x for x in events if x["event"]=="bot"]
                bot_event = bot_events[-1]
                bot_response = bot_event["text"]
                dispatcher.utter_message(text=bot_response)

                return [UserUtteranceReverted(),  SlotSet("previous_requested_slot", None), SlotSet("slot_silence_count",silence_count)]#, SlotSet("remind_slot", None)]    
            
            elif silence_count>=3:
                dispatcher.utter_message(response="utter_react_to_silence_2nd")
                return [AllSlotsReset(),Restarted()]

        elif (requested_slot=="slot_exhibit"):
            

            if (silence_count>=2):  

                remaining_exhibits = tracker.slots.get("slot_remaining_exhibits")
          
                if len(remaining_exhibits)==0:
                    dispatcher.utter_message(response="utter_say_goodbye")
                    return [AllSlotsReset(),Restarted()]
                else:
                    rand_index = random.randint(0, len(remaining_exhibits)-1)
                    random_choice = remaining_exhibits[rand_index]
                
                slot_list_available_exhibit_utters = tracker.slots.get("slot_list_available_exhibit_utters")  
                slot_list_exhibit_utters = slot_list_available_exhibit_utters[rand_index]

            
                if random_choice in remaining_exhibits:
                    remaining_exhibits.remove(random_choice)
            
                # dispatcher.utter_message(response="utter_say_current_exhibit")

                return [UserUtteranceReverted(),  SlotSet("previous_requested_slot", None), SlotSet("slot_silence_count",0), SlotSet("slot_interested", "change"), SlotSet("slot_exhibit", random_choice), SlotSet("slot_previous_exhibit",random_choice), SlotSet("slot_remaining_exhibits",remaining_exhibits), SlotSet("slot_list_exhibit_utters",slot_list_exhibit_utters), SlotSet("remind_slot", None), FollowupAction("form_exhibit") ]
           
            else: 

                dispatcher.utter_message(response="utter_react_to_silence_1st")

                events = tracker.events
                bot_events = [x for x in events if x["event"]=="bot"]
                bot_event = bot_events[-1]
                bot_response = bot_event["text"]
                dispatcher.utter_message(text=bot_response)

                return [UserUtteranceReverted(),  SlotSet("previous_requested_slot", None), SlotSet("slot_silence_count",silence_count), SlotSet("slot_interested", "change")]
    
        elif slot_exhibit != None:

            exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")           

            if (len(exhibit_utters)!=0) and (silence_count<=1):
                
                dispatcher.utter_message(response="utter_say_capabilities")                
            
            elif (len(exhibit_utters)!=0) and (silence_count==2):

                dispatcher.utter_message(response="utter_silent_user")
                
                i = random.randint(0, len(exhibit_utters)-1 )	
                selected_utter=exhibit_utters[i]
                exhibit_utters.pop(i)
                
                dispatcher.utter_message(response=selected_utter)

            return [UserUtteranceReverted(),  SlotSet("slot_silence_count",silence_count), SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_iterate_form_exhibit")]







class ActionSetSlotSilence(Action):
    def name(self):
        return "action_set_slot_silence_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_set_slot_silence_count")
        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name")
        silence_count = tracker.slots.get("slot_silence_count")

        if intent != "intent_silence":
            silence_count  = 0

            return [SlotSet("slot_silence_count", silence_count)]


        

        
        




class ActionSayCurrentExhibit(Action):
    def name(self):
        return "action_say_current_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        dispatcher.utter_message(response="utter_say_current_exhibit")        
        return []



class ActionSayCapabilites(Action):
    def name(self):
        return "action_say_capabilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        dispatcher.utter_message(response="utter_say_capabilities")        
        return []


class ActionExhibitSelected(Action):
    def name(self):
        return "action_introduce_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_introduce_exhibit")
        dispatcher.utter_message(response="utter_introduce_exhibit") 

        return []


class ActionSubmitFormUser(Action):
    def name(self):
        return "action_submit_form_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_submit_form_user")
        dispatcher.utter_message(response="utter_introduction_to_tour")
        return []


class ActionSubmitFormExhibit(Action):
    def name(self):
        return "action_submit_form_exhibit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_submit_form_exhibit")
        slot_interested = tracker.slots.get("slot_interested")
        slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
        slot_exhibit = tracker.slots.get("slot_exhibit")

        if (slot_interested == "stop"):

            dispatcher.utter_message(response="utter_say_goodbye")
            return [AllSlotsReset(), Restarted()]

        elif (slot_interested == "no_change"):

            dispatcher.utter_message(response="utter_exhibit_not_changed")
            latest_message = tracker.latest_message
            intent = latest_message["intent"].get("name") 
            list_intents = tracker.slots.get("slot_list_intents")
            if intent in list_intents:
          
                action = "action_say_" + intent[7:]     
                return [FollowupAction(action)]
            
            else:
                exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")           

                if (len(exhibit_utters)!=0):

                    i = random.randint(0, len(exhibit_utters)-1 )	
                    selected_utter=exhibit_utters[i]
                    exhibit_utters.pop(i)
                    
                    dispatcher.utter_message(response=selected_utter)
                    return [SlotSet("slot_list_exhibit_utters",exhibit_utters)]

                else:

                    dispatcher.utter_message(response="utter_say_capabilities")

        elif (slot_interested == "change"):

            
            dispatcher.utter_message(response="utter_exhibit_changed")
            dispatcher.utter_message(response="utter_introduce_exhibit")
            dispatcher.utter_message(response="utter_say_capabilities")


        return []

        
class ActionValidateAction(Action):
    def name(self):
        return "action_validate_intents"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("validate_intents")
        list_intents = tracker.slots.get("slot_list_intents")

        latest_message = tracker.latest_message
        intent = latest_message["intent"].get("name") 

        if intent in list_intents:

            slot_exhibit = tracker.slots.get("slot_exhibit")
            slot_previous_exhibit = tracker.slots.get("slot_previous_exhibit")
            if ((intent!="intent_exhibit") and (slot_exhibit==None)): 
                
                if slot_previous_exhibit=="-":
                    return [SlotSet("slot_interested", "change"), FollowupAction("form_exhibit")]
                else:
                    return [SlotSet("slot_interested", "no_change"), SlotSet("slot_exhibit", slot_previous_exhibit)]
                
            elif (intent=="intent_exhibit"):
                

                return [SlotSet("slot_interested", "change"), FollowupAction("form_exhibit")]





class ActionSetSlotIntents(Action):
    def name(self):
        return "action_set_slot_list_intents"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

               
        return []


class ActionRepeat(Action):
    

    def name(self) -> Text:
        return "action_repeat"


    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict) -> List[EventType]:


        events = tracker.events
        bot_events = [x for x in events if x["event"]=="bot"]
        bot_event = bot_events[-1]
        bot_response = bot_event["text"]
        dispatcher.utter_message(text=bot_response)

        return [UserUtteranceReverted()]




class ActionSetListUtters(Action):
    def name(self):
        return "action_set_slot_list_exhibit_utters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        return []   



class ActionSetAvailbleExhibits(Action):
    def name(self):
        return "action_set_slot_available_exhibits"   #den allazei pote to slot

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        return []  

class ActionSetRemainingExhibits(Action):
    def name(self):
        return "action_set_slot_remaining_exhibits"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        return []  


class ActionSetListAvailableUtters(Action):
    def name(self):
        return "action_set_slot_list_available_exhibit_utters"  #den allazei pote to slot
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        return []  



class ActionSayAvailableExhibits(Action):
    def name(self):
        return "action_say_available_exhibits"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        dispatcher.utter_message(response = "utter_say_available_exhibits")
        return []  

class ActionStopTour(Action):
    def name(self):
        return "action_stop_tour"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        dispatcher.utter_message(response = "utter_say_goodbye")
        return [AllSlotsReset(),Restarted()] 


class ActionSetFlagExhibitUtters(Action):
    def name(self):
        return "action_set_flag_exhibit_utters"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return [] 
        

class ActionSetSlotAdult(Action):
    def name(self):
        return "action_set_slot_adult"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        
        return [] 



class ActionNoChangeExhibit(Action):
    def name(self):
        return "action_no_change_exhibit"  
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        print("action_no_change_exhibit")

        # dispatcher.utter_message(response="utter_exhibit_not_changed")

        exhibit_utters = tracker.slots.get("slot_list_exhibit_utters")
        slot_previous_exhibit=tracker.slots.get("slot_previous_exhibit")
        if exhibit_utters!=None:
            if (len(exhibit_utters)==0):

                slot_exhibit = tracker.slots.get("slot_exhibit")
                available_exhibits = tracker.slots.get("slot_available_exhibits")

                index = available_exhibits.index(slot_exhibit)  
                slot_list_available_exhibit_utters = tracker.slots.get("slot_list_available_exhibit_utters")  
                exhibit_utters = slot_list_available_exhibit_utters[index]

            i = random.randint(0, len(exhibit_utters)-1 )	
            selected_utter=exhibit_utters[i]
            exhibit_utters.pop(i)
            
            dispatcher.utter_message(response=selected_utter)
            return [SlotSet("slot_interested", "no_change"), SlotSet("slot_exhibit", slot_previous_exhibit),SlotSet("slot_list_exhibit_utters",exhibit_utters), FollowupAction("action_iterate_form_exhibit")]

            