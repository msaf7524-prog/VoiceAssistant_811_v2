[app]

# (str) Title of your application
title = VoiceAssistant 811

# (str) Package name
package.name = voiceassistant811

# (str) Package domain (needed for android/ios packaging)
package.domain = org.msaf

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# (str) Application versioning
version = 1.0

# (list) Application requirements
# تمت إزالة pyobjus وإضافة pyjnius و plyer لدعم ميزات الأندرويد والخدمات الخلفية
requirements = python3,kivy==2.3.0,android,pyjnius,plyer

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# تمت إضافة صلاحيات الـ Wake Lock والـ Foreground Service الإلزامية في API 34
android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS,WAKE_LOCK,FOREGROUND_SERVICE,FOREGROUND_SERVICE_MICROPHONE,FOREGROUND_SERVICE_CONNECTED_DEVICE

# (list) Services
# هذا السطر ضروري جداً لكي يعمل التطبيق ويرد على الأوامر بدون فتح الشاشة
services = VoiceService:service.py

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
# تم التعديل إلى 25b ليتوافق مع شروط Buildozer الأخيرة
android.ndk = 25b

# (bool) If True, then accept all SDK licences automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) python-for-android branch to use
# تغيير الفرع إلى develop يحل مشكلة IndexError مع NDK 25b
p4a.branch = develop

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
