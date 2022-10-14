# coding=utf-8
from __future__ import division
from subprocess import Popen
import os
import time
import re
import sys
import wave
import io
import pyaudio
from six.moves import queue
import numpy as np
from google.oauth2 import service_account
from google.cloud import speech_v1 as speech
from google.cloud.speech import enums
from google.cloud import texttospeech_v1 as texttospeech
from play_sound import *


RESPEAKER_RATE = 32000 # default: 16000
RESPEAKER_CHANNELS = 1 # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 10  # refer to input device id
#CHUNK = 1024 # default 1024
CHUNK = 4096
RECORD_SECONDS = 10



################################################################################
class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    #---------------------------------------------------------------------------
    def __init__(self, rate, chunk, duration):
        self._rate = rate
        self._chunk = chunk
        self.duration = duration

        self.has_input = False
        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.time_over = False
        self.start_input = 999999999999999999999999


    #---------------------------------------------------------------------------
    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=self._audio_interface.get_format_from_width(RESPEAKER_WIDTH),
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=RESPEAKER_CHANNELS,
            rate=self._rate,
            input=True,
            output=False,
            frames_per_buffer=self._chunk,
            input_device_index=RESPEAKER_INDEX,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self


    #---------------------------------------------------------------------------
    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True


        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()


    #---------------------------------------------------------------------------
    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)

        data_as_np = np.frombuffer(in_data, dtype=np.int16)
        data_as_np = data_as_np.reshape(frame_count, RESPEAKER_CHANNELS)
        data_as_np = np.int16(data_as_np)
        return data_as_np, pyaudio.paContinue


    #---------------------------------------------------------------------------
    def generator(self):

        i = 0
        while not self.closed:

            self._audio_stream.start_stream()

            if (i > int(self._rate / self._chunk * self.duration)-1) and (not self.has_input):
                print("telos xronou kai adeio")
                break

            current_time = time.time()
            diff_time = current_time-self.start_input
            if diff_time > self.duration*3:
                print("10 deuterolepta")
                self.time_over = True
                break

            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
#                try:
                    #chunk = self._buff.get(block=False)
                    #if chunk is None:
                        #return
                    #data.append(chunk)
                #except queue.Empty:
                    #break

                try:
                  #d = self._audio_stream.read(CHUNK)
                  chunk = self._buff.get(block=False)
                  if chunk is None:
                      return
                  data.append(chunk)
                except queue.Empty:
                    break

            i = i + 1

            yield b"".join(data)


#-------------------------------------------------------------------------------
def listen_print_loop(responses,stream):


    num_chars_printed = 0

    #billed_time = response.total_billed_time
    # print("billed_time: "+ str(billed_time))


    for response in responses:
        print('------------')
        print(response.results)
        print('------------')
        if not response.results:
          print('not response.results')
          continue

        results = response.results

        result = results[0]

        print('if not result.alternatives:')
        if not result.alternatives:
            print ("no results")
            return [],[]

        print('if not stream.has_input')
        if not stream.has_input:
            print("exw input")
            stream.has_input = True
            stream.start_input = time.time()


        alternative = result.alternatives[0]

        transcript = alternative.transcript

        confidence = alternative.confidence

        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()
            num_chars_printed = len(transcript)
        else:
            print(transcript + overwrite_chars)
            num_chars_printed = 0
            return transcript, confidence


    print("no responses")
    return [], []


#-------------------------------------------------------------------------------
def speech_to_text():

    # Audio recording parameters
    rate = RESPEAKER_RATE
    chunk =  CHUNK #int(rate / 10)  # 100ms
    duration = 5


    language_code = "el-GR"  # a BCP-47 language tag

    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    cred = service_account.Credentials.from_service_account_file('solid-scope-361216-f63934ecc11d.json', scopes=SCOPES)

    client = speech.SpeechClient(credentials=cred)

    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=rate,
        language_code=language_code,
    )

    streaming_config = speech.types.StreamingRecognitionConfig(
        config=config, single_utterance=False, interim_results=True
    )


    while True:

        print("--"*50)
        print("--"*50)
        with MicrophoneStream(rate, chunk, duration) as stream:

            print("new stream")
            start_stream = time.time()
            audio_generator = stream.generator()

            requests = (
                speech.types.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            transcript, confidence = listen_print_loop(responses,stream)

            if stream.time_over:

                transcript = "πιο σύντομα παρακαλώ"
                flag = False
                print(transcript)
                break

            elif not transcript:   #den milise katholou
                print("no message at all")
                print("εiiii esai ekeiiii sou ekana mia erwtisi")
                transcript = "Σιωπή"
                flag = True
                break

            else:

                if confidence<0.75:
                    print("low confidence")
                    print(confidence)
                    transcript = "δεν κατάλαβα, παρακαλώ επανάλαβε πιο καθαρά αυτή τη φορά"
                    print(transcript)
                    flag = False
                    break

                else:
                    print("μην επανάλαμβανεις ola teleia")
                    #steile to transcript sto rasa
                    print(transcript)
                    print(confidence)
                    flag = True
                    break #apo tin while True


    return transcript, flag


#-------------------------------------------------------------------------------
def text_to_speech(text):

    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    cred = service_account.Credentials.from_service_account_file('solid-scope-361216-f63934ecc11d.json', scopes=SCOPES)

    client=texttospeech.TextToSpeechClient(credentials=cred)


    #output of: print(client.list_voices())
    #voices {
      #language_codes: "el-GR"
      #name: "el-GR-Wavenet-A"
      #ssml_gender: FEMALE
      #natural_sample_rate_hertz: 24000
    #}
    #voices {
      #language_codes: "el-GR"
      #name: "el-GR-Standard-A"
      #ssml_gender: FEMALE
      #natural_sample_rate_hertz: 24000
    #}

    input=texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='el-GR',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
        name='el-GR-Wavenet-A' # Better than el-GR-Standard-A
    )


    audio_config=texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16,
        #speaking_rate=0.5,
        #pitch=2,
        #effects_profile_id=[effects_profile_id]

    )

    # https://stackoverflow.com/questions/55291174/error-in-python-cryptography-module-rsaprivatekey-object-has-no-attribute-si
    print('Converting text to speech...')
    response=client.synthesize_speech(
        input_=input,
        voice=voice,
        audio_config=audio_config
    )
    print('Done')


    with wave.open(io.BytesIO(response.audio_content), 'rb') as f:
        width = f.getsampwidth()
        channels = f.getnchannels()
        rate = f.getframerate()

    pa = pyaudio.PyAudio()

    pa_stream = pa.open(
        format=pyaudio.get_format_from_width(width),
        channels=channels,
        rate=rate,
        output=True
    )

    pa_stream.write(response.audio_content)
