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
    # 合成言語と音声を選択する
    speech_config.speech_synthesis_language = "ja-JP"
    speech_config.speech_synthesis_voice_name ="ja-JP-NanamiNeural"
    
    # 音声をファイルに合成する
    audio_config = AudioOutputConfig(filename="path/to/write/file.wav")

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async("テキストから音声データを出力できるか確認するサンプルテキストです。")

    # ステータス文を追加
    st.write('音声ファイルはpath/to/writeフォルダに出力されました')



