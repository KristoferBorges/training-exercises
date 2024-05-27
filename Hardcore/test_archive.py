import speech_recognition as sr

while True:
    # Crie um objeto de reconhecimento de fala
    r = sr.Recognizer()

    # Use o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        # Reconheça o áudio usando o Google Speech Recognition
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))