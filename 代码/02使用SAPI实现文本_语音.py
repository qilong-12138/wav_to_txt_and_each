from win32com.client import Dispatch
speaker=Dispatch('SAPI.SpVoice')
speaker.Speak('大家好')
del speaker