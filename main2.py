import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

# タイトルを追加
st.title('簡易音声出力アプリ-Azure Text-to-Speech')

st.markdown('### 音声出力用のテキストデータ(日本語)を準備')
st.write('\n')  # 改行
# 入力データの選択
input_data_option = st.selectbox(
    '入力データの選択',
    ('直接入力','テキストファイル')
)
st.write('\n')  # 改行

input_data = None

if input_data_option == '直接入力':
    input_data = st.text_area('こちらにテキストを入力してください。','Azure Text-To-Speechを使って音声出力するサンプル文になります。')
else:
    uploaded_file = st.file_uploader('こちらにテキストファイルをアップロードしてください。', ['txt'])
    if uploaded_file is not None:
        # テキストとして読み込む
        content = uploaded_file.read()
        input_data = content.decode()

if input_data is not None:
    st.write('音声出力するデータ')
    st.write(input_data)
else:
    input_data = 'サンプルテキストを選択してください。'
st.write('\n')  # 改行

# 説明を追加
st.write('下のチェックボックスにチェックを付けると、音声ファイルが生成されます')

if st.checkbox('音声出力') and input_data is not None:
    # 音声構成を作成する
    # speech_config = speechsdk.SpeechConfig(subscription="<paste-your-speech-key-here>", region="<paste-your-speech-location/region-here>")
    speech_config = speechsdk.SpeechConfig(subscription="c3a2ff821eb348ce984330cf92b65561", region="japanwest")
    # 合成言語と音声を選択する
    speech_config.speech_synthesis_language = "ja-JP"
    speech_config.speech_synthesis_voice_name ="ja-JP-NanamiNeural"

    # スピーカー出力に合成する
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    result = synthesizer.speak_text_async(input_data).get()
    stream = AudioDataStream(result)

    # オーディオ形式をカスタマイズする
    speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    result = synthesizer.speak_text_async(input_data).get()
    # stream.save_to_wav_file("file.wav")
    stream.save_to_wav_file("output-file.wav")

    st.write('テキストから音声データを出力しました')
    st.audio("output-file.wav")



