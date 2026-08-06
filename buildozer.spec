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
# استخدمنا إصدار 2.2.1 المستقر لتخطي خطأ libthorvg
requirements = python3,kivy==2.2.1,pyobjus,android

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# صلاحيات الميكروفون والبلوتوث والإنترنت الخاصة بالمساعد الصوتي
android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS

# (int) Target Android API, should be one of the available API levels
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (bool) If True, then accept all SDK licences automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support. Required for NDK >= 21
android.enable_androidx = True

# (str) python-for-android branch to use
# استخدمنا develop لتخطي خطأ pip
p4a.branch = develop

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
