from jnius import autoclass, PythonJavaClass, java_method
from threading import Timer

SpeechRecognizer = autoclass("android.speech.SpeechRecognizer")
RecognizerIntent = autoclass("android.speech.RecognizerIntent")
Intent = autoclass("android.content.Intent")
PythonActivity = autoclass("org.kivy.android.PythonActivity")


class _RecognitionListener(PythonJavaClass):
    __javainterfaces__ = ["android/speech/RecognitionListener"]

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

    @java_method("(I)V")
    def onError(self, error):
        if self.engine and self.engine.running:
            self.engine.restart_later()

    @java_method("(Landroid/os/Bundle;)V")
    def onResults(self, results):
        if not self.engine:
            return

        try:
            matches = results.getStringArrayList(
                SpeechRecognizer.RESULTS_RECOGNITION
            )
            if matches and matches.size() > 0:
                text = matches.get(0)
                if self.engine.callback:
                    self.engine.callback(text)
        except Exception:
            pass

        if self.engine.running:
            self.engine.restart_later()

    @java_method("(Landroid/os/Bundle;)V")
    def onPartialResults(self, bundle):
        pass

    @java_method("(ILandroid/os/Bundle;)V")
    def onEvent(self, eventType, params):
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

        try:
            context = PythonActivity.mActivity
            self.recognizer = SpeechRecognizer.createSpeechRecognizer(context)
            self.listener = _RecognitionListener(self)
            self.recognizer.setRecognitionListener(self.listener)
            self.start_listening()
        except Exception as e:
            self.running = False
            if self.callback:
                self.callback(f"[Speech start error] {e}")

    def stop(self):
        self.running = False

        if self.recognizer:
            try:
                self.recognizer.stopListening()
            except Exception:
                pass

            try:
                self.recognizer.cancel()
            except Exception:
                pass

            try:
                self.recognizer.destroy()
            except Exception:
                pass

        self.recognizer = None
        self.listener = None

    def build_intent(self):
        intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
        intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE_MODEL,
            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
        )
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, self.language)
        intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
        return intent

    def start_listening(self):
        if not self.recognizer or not self.running:
            return

        try:
            self.recognizer.startListening(self.build_intent())
        except Exception as e:
            if self.callback:
                self.callback(f"[Speech listening error] {e}")
            self.restart_later()

    def restart_later(self):
        if not self.running:
            return
        Timer(0.6, self.restart).start()

    def restart(self):
        if not self.running or not self.recognizer:
            return

        try:
            self.recognizer.cancel()
        except Exception:
            pass

        try:
            self.recognizer.startListening(self.build_intent())
        except Exception as e:
            self.running = False
            if self.callback:
                self.callback(f"[Speech restart error] {e}")
