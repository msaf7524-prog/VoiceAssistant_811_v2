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
# عدنا لإصدار Kivy الحديث لأن المشكلة تم حلها من جذورها
requirements = python3,kivy==2.3.0,pyobjus,android

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# جميع الصلاحيات اللازمة للمساعد الصوتي 811
android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
# هذا هو التعديل الذهبي لحل مشكلة المجلدات المفقودة
android.ndk = 23b

# (bool) If True, then accept all SDK licences automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) python-for-android branch to use
# عدنا للفرع المستقر
p4a.branch = master

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
