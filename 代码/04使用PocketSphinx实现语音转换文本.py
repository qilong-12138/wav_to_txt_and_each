import speech_recognition as sr
audio_file='demo_audio.wav'
r=sr.Recognizer()
#打开语音文件
with sr.AudioFile(audio_file) as source:
    audio=r.record(source)

#将语音转换为文本
# print('文本内容：',r.recognize_sphinx(audio))
print('文本内容：',r.recognize_sphinx(audio,language='zh-CN'))