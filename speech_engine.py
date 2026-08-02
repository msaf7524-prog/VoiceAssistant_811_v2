from threading import Timer
from kivy.utils import platform

if platform == "android":
    try:
        from jnius import autoclass, PythonJavaClass, java_method
        from android.runnable import run_on_ui_thread

        SpeechRecognizer = autoclass("android.speech.SpeechRecognizer")
        RecognizerIntent = autoclass("android.speech.RecognizerIntent")
        Intent = autoclass("android.content.Intent")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        HAS_ANDROID = True
    except Exception as e:
        print("Android Speech Imports Error:", e)
        HAS_ANDROID = False
else:
    HAS_ANDROID = False
    # دالة وهمية للحفاظ على عمل الكود خارج الأندرويد
    def run_on_ui_thread(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


if HAS_ANDROID:
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
    def __init__(self, callback=None, language="ar-SA"):
        self.callback = callback
        self.language = language
        self.running = False
        self.recognizer = None
        self.listener = None

    def start(self):
        if self.running or not HAS_ANDROID:
            return

        self.running = True
        self._init_and_start_ui()

    @run_on_ui_thread
    def _init_and_start_ui(self):
        try:
            context = PythonActivity.mActivity
            if self.recognizer is None:
                self.recognizer = SpeechRecognizer.createSpeechRecognizer(context)
                self.listener = _RecognitionListener(self)
                self.recognizer.setRecognitionListener(self.listener)
            
            self._start_listening_ui()
        except Exception as e:
            self.running = False
            if self.callback:
                self.callback(f"[Speech start error] {e}")

    @run_on_ui_thread
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

    @run_on_ui_thread
    def _start_listening_ui(self):
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
        if not self.running or not HAS_ANDROID:
            return
        self._restart_ui()

    @run_on_ui_thread
    def _restart_ui(self):
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
