import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig



# タイトルを追加
st.title('音声出力-Azure Text-to-Speechサンプルコード利用')
# 説明を追加
st.write('下のチェックボックスにチェックを付けると、音声ファイルが生成されます')

if st.checkbox('音声出力'):
    # 音声構成を作成する
    # speech_config = speechsdk.SpeechConfig(subscription="<paste-your-speech-key-here>", region="<paste-your-speech-location/region-here>")
    speech_config = speechsdk.SpeechConfig(subscription="c3a2ff821eb348ce984330cf92b65561", region="japanwest")
    # 合成言語と音声を選択する
    speech_config.speech_synthesis_language = "ja-JP"
    speech_config.speech_synthesis_voice_name ="ja-JP-NanamiNeural"

    # スピーカー出力に合成する
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    result = synthesizer.speak_text_async("テキストデータから音声ファイルを出力できました").get()
    stream = AudioDataStream(result)

    # オーディオ形式をカスタマイズする
    speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    result = synthesizer.speak_text_async("テキストデータから音声ファイルを出力できました").get()
    # stream.save_to_wav_file("file.wav")
    stream.save_to_wav_file("output-file.wav")

    st.write('テキストから音声データを出力しました')
 
