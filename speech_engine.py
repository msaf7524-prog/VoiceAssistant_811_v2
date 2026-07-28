from jnius import autoclass, PythonJavaClass, java_method

SpeechRecognizer = autoclass("android.speech.SpeechRecognizer")
RecognizerIntent = autoclass("android.speech.RecognizerIntent")
Intent = autoclass("android.content.Intent")
PythonActivity = autoclass("org.kivy.android.PythonActivity")

_CONTEXT = PythonActivity.mActivity


class _RecognitionListener(PythonJavaClass):
    __javainterfaces__ = [
        "android/speech/RecognitionListener"
    ]

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    @java_method("(Landroid/os/Bundle;)V")
    def onReadyForSpeech(self, params):
        pass

    @java_method("()V")
    def onBeginningOfSpeech(self):
        pass

    @java_method("(F)V")
    def onRmsChanged(self, rmsdB):
        pass

    @java_method("([B)V")
    def onBufferReceived(self, buffer):
        pass

    @java_method("()V")
    def onEndOfSpeech(self):
        pass

    @java_method("(ILandroid/os/Bundle;)V")
    def onError(self, error, params):
        if not self.engine:
            return

        if self.engine.callback:
            self.engine.callback(f"[Speech Error {error}]")

        if self.engine.running:
            self.engine.restart()

    @java_method("(Landroid/os/Bundle;)V")
    def onResults(self, results):
        if not self.engine:
            return

        matches = results.getStringArrayList(
            SpeechRecognizer.RESULTS_RECOGNITION
        )

        if matches and matches.size() > 0:
            text = matches.get(0)

            if self.engine.callback:
                self.engine.callback(text)

        if self.engine.running:
            self.engine.restart()

    @java_method("(Landroid/os/Bundle;)V")
    def onPartialResults(self, bundle):
        pass

    @java_method("(I)V")
    def onEvent(self, eventType):
        pass
      class SpeechEngine:

    def __init__(self, callback=None, language="en-US"):
        self.callback = callback
        self.language = language

        self.running = False

        self.recognizer = None
        self.listener = None

    def start(self):

        if self.running:
            return

        self.running = True

        self.recognizer = SpeechRecognizer.createSpeechRecognizer(_CONTEXT)

        self.listener = _RecognitionListener(self)

        self.recognizer.setRecognitionListener(self.listener)

        self.start_listening()

    def stop(self):

        self.running = False

        if self.recognizer:
            try:
                self.recognizer.stopListening()
            except:
                pass

            try:
                self.recognizer.cancel()
            except:
                pass

            try:
                self.recognizer.destroy()
            except:
                pass

        self.recognizer = None
        self.listener = None

    def build_intent(self):

        intent = Intent(
            RecognizerIntent.ACTION_RECOGNIZE_SPEECH
        )

        intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE_MODEL,
            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
        )

        intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE,
            self.language
        )

        intent.putExtra(
            RecognizerIntent.EXTRA_PARTIAL_RESULTS,
            False
        )

        intent.putExtra(
            RecognizerIntent.EXTRA_MAX_RESULTS,
            1
        )

        return intent
          def start_listening(self):

        if not self.recognizer:
            return

        try:
            self.recognizer.startListening(
                self.build_intent()
            )

        except Exception as e:

            if self.callback:
                self.callback(
                    f"[SpeechEngine] {e}"
                )

            self.restart()

    def restart(self):

        if not self.running:
            return

        try:
            self.recognizer.cancel()
        except:
            pass

        try:
            self.recognizer.startListening(
                self.build_intent()
            )
        except Exception as e:

            self.running = False

            if self.callback:
                self.callback(
                    f"[SpeechEngine Fatal] {e}"
                )

    def is_running(self):
        return self.running

    def set_language(self, language):
        self.language = language

    def set_callback(self, callback):
        self.callback = callback
