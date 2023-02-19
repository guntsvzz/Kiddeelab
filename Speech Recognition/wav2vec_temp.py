from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import speech_recognition as sr
import io
import pydub
# load model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

r = sr.Recognizer()

with sr.Microphone(sample_rate = 16000) as source:
    print('Start Speaking now...')
    while True:
        audio = r.listen(source) #pyaudio object
        data = io.BytesIO(audio.get_wav_data()) #list of bytes
        clip = pydub.AudioSegment.from_file(data) #numpy array
        print(clip)
        # x = torch.FloatTensor(clip.get_array_of_samples()) #Tensor
        
        # inputs = processor(x , samping_rate = 16000 ,return_tensors="pt", padding = 'longest').input_values
        # logits = model(inputs).logits
        # tokens = torch.argmax(logits, axis = -1) #get the 
        # text   = processor.batch_decode(tokens) #tokens into a string

        # print('You said',str(text).lower())