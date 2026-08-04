[app]

# (str) Title of your application
title = VoiceAssistant 811

# (str) Package name
package.name = voiceassistant811

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,json

# (list) Application requirements
# يمكنك إضافة أي مكتبات بايثون إضافية تحتاجها التطبيق هنا تفصل بينها بفواصل
requirements = python3,kivy,pyobjus,android

# (str) Custom source folders for requirements
# Change it if you want to send custom commands to pygame
#requirements.source.kivy =

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# الأذونات الأساسية للتعامل مع الصوت والبلوتوث
android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT

# (int) Target Android API, should be one of the available API levels
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use (تحديد إصدار مستقر لمنع استدعاء 37.0.0)
android.build_tools_version = 33.0.2

# (bool) If True, then accept all SDK licences automatically
android.accept_sdk_license = True

# (list) List of service to declare
# services = MyService:service.py

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support. Required for NDK >= 21
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
