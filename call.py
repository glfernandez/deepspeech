import os
import time

def activate_call():
  """Activates the call.py file and saves the transcription to a text file.

  Args:
    None.

  Returns:
    None.
  """

  # Get the current date and time.
  now = time.strftime("%Y-%m-%d_%H-%M-%S")

  # Create a directory to store the transcriptions.
  if not os.path.exists("/Users/gl_fernandez/Documents/Basecamp/DeepSpeech/Save file"):
    os.mkdir("/Users/gl_fernandez/Documents/Basecamp/DeepSpeech/Save file")

  # Run the call.py file.
  os.system(
      "python /Users/gl_fernandez/deepspeech/DeepSpeech-examples/mic_vad_streaming/mic_vad_streaming.py -m /Users/gl_fernandez/deepspeech/deepspeech-0.9.3-models.pbmm -s /Users/gl_fernandez/deepspeech/deepspeech-0.9.3-models.scorer")

  # Get the transcription from the call.py file.
  transcription = ""
  if os.path.exists("/tmp/deepspeech.transcript"):
    transcription = os.system("cat /tmp/deepspeech.transcript").decode("utf-8")

  # Save the transcription to a text file.
  with open("/Users/gl_fernandez/Documents/Basecamp/DeepSpeech/Save file/" + now + ".txt", "w") as f:
    f.write(transcription)

  # Save the audio file.
  try:
    audio_file = os.system("arecord -r 16000 -d 10 /tmp/deepspeech.wav")
    f.write(audio_file)
  except:
    audio_file = ""


if __name__ == "__main__":
  activate_call()
