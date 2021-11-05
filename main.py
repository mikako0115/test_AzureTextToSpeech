import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
# タイトルを追加
st.title('音声出力-Azure Text-to-Speechサンプルコード利用')
# 説明を追加
st.write('下のチェックボックスにチェックを付けると、指定フォルダに音声ファイルが生成されます')

if st.checkbox('音声出力'):
    # 音声構成を作成する
    # speech_config = speechsdk.SpeechConfig(subscription="<paste-your-speech-key-here>", region="<paste-your-speech-location/region-here>")
    speech_config = speechsdk.SpeechConfig(subscription="c3a2ff821eb348ce984330cf92b65561", region="japanwest")
    # ソース言語を変更する
    speech_config.speech_recognition_language="jp-JP"

    # 音声をファイルに合成する
    audio_config = AudioOutputConfig(filename="path/to/write/file.wav")

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async("テキストから音声データを出力できるか確認するサンプルテキストです。")

    # ステータス文を追加
    st.write('音声ファイルはpath/to/writeフォルダに出力されました')


# ファイルから認識する
# def from_file():
#     speech_config = speechsdk.SpeechConfig(subscription="<paste-your-speech-key-here>", region="<paste-your-speech-location/region-here>")
#     audio_input = speechsdk.AudioConfig(filename="your_file_name.wav")
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
#     result = speech_recognizer.recognize_once_async().get()
#     print(result.text)

# from_file()

# if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#     print("Recognized: {}".format(result.text))
# elif result.reason == speechsdk.ResultReason.NoMatch:
#     print("No speech could be recognized: {}".format(result.no_match_details))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         print("Error details: {}".format(cancellation_details.error_details))


