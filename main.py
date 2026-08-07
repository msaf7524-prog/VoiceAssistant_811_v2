from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=15, padding=15, **kwargs)

        self.title_label = Label(text="Voice Assistant 811", font_size="24sp")
        self.add_widget(self.title_label)

        self.status = Label(text="التطبيق جاهز، اضغط للتشغيل", font_size="18sp")
        self.add_widget(self.status)

        self.start_btn = Button(text="بدء المساعد (في الخلفية)", size_hint=(1, None), height=60)
        self.start_btn.bind(on_press=self.start_assistant)
        self.add_widget(self.start_btn)

    def start_assistant(self, *args):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            # نطلب جميع الصلاحيات اللازمة للعمل عبر البلوتوث والمايكروفون
            permissions = [
                Permission.RECORD_AUDIO,
                Permission.BLUETOOTH_CONNECT,
                Permission.BLUETOOTH,
                Permission.INTERNET
            ]
            self.status.text = "جاري طلب الصلاحيات..."
            # نمرر دالة callback لتُنفذ بعد رد المستخدم
            request_permissions(permissions, self.permissions_callback)
        else:
            self.status.text = "عذراً، هذا التطبيق مخصص للأندرويد فقط."

    def permissions_callback(self, permissions, grants):
        # التحقق مما إذا كان المستخدم قد وافق على جميع الصلاحيات
        if all(grants):
            self.status.text = "تمت الموافقة، جاري تشغيل الخدمة..."
            self.start_background_service()
        else:
            self.status.text = "لا يمكن تشغيل المساعد بدون الصلاحيات المطلوبة."

    def start_background_service(self):
        if platform == 'android':
            try:
                from jnius import autoclass
                # استدعاء النشاط الحالي للتطبيق
                mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
                # استدعاء الخدمة التي عرفناها في buildozer.spec
                # لاحظ أن الصيغة هي: org.domain.package.ServiceServicename
                service = autoclass('org.msaf.voiceassistant811.ServiceVoiceservice')
                
                # تشغيل الخدمة
                service.start(mActivity, "")
                self.status.text = "المساعد يعمل الآن في الخلفية!\nيمكنك إغلاق الشاشة."
            except Exception as e:
                self.status.text = f"خطأ في بدء الخدمة: {e}"

class VoiceAssistantApp(App):
    def build(self):
        self.title = "Voice Assistant 811"
        return MainLayout()

if __name__ == "__main__":
    VoiceAssistantApp().run()
