from dotenv import load_dotenv

load_dotenv()

import os
import boto3

#Explicit Client Configuration
polly = boto3.client('polly')

result = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the Audio from the response
audio = result['AudioStream'].read()
with open("helloworld.mp3","wb") as file:
    file.write(audio)