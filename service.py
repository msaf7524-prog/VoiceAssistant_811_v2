import time
from kivy.utils import platform

# استيراد محركات الصوت التي قمنا بتجهيزها مسبقاً
from speech_engine import SpeechEngine
from tts_engine import TTSEngine

def handle_command(text):
    """
    هذه الدالة يتم استدعاؤها تلقائياً بمجرد أن يلتقط المساعد أي صوت منك.
    """
    print(f"تم سماع: {text}")
    
    # يمكنك تخصيص الأوامر والردود هنا
    if "مرحباً" in text or "أهلاً" in text:
        tts_engine.speak("أهلاً بك يا عماد، أنا جاهز لتنفيذ أوامرك في الخلفية.")
    elif "الtime" in text or "الوقت" in text:
        current_time = time.strftime("%H:%M")
        tts_engine.speak(f"الوقت الحالي هو {current_time}")
    else:
        # رد افتراضي يكرر ما قلته للتأكد من دقة الاستماع
        tts_engine.speak(f"لقد قلت: {text}")

if __name__ == "__main__":
    print("=== تم بدء تشغيل خدمة الخلفية للمساعد 811 ==-")
    
    # التأكد من أننا نعمل على نظام أندرويد
    if platform == "android":
        from jnius import autoclass
        # إبقاء الخدمة نشطة في الخلفية كخدمة أمامية خفيفة إذا لزم الأمر
        PythonService = autoclass('org.kivy.android.PythonService')
        service = PythonService.mService
        
    # تهيئة محرك النطق (TTS)
    tts_engine = TTSEngine(language="ar")
    
    # إعطاء مهلة صغيرة لضمان جاهزية المحرك
    time.sleep(3)
    
    # تهيئة وبدء محرك الاستماع الصوتي مع ربطه بدالة المعالجة
    speech_engine = SpeechEngine(callback=handle_command, language="ar-SA")
    speech_engine.start()
    
    # حلقة تكرارية لا نهائية لإبقاء الخدمة حية في الخلفية وعدم إغلاقها
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        speech_engine.stop()
        tts_engine.shutdown()
