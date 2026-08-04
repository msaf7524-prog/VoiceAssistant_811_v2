[app]

# (str) Title of your application
title = VoiceAssistant 811

# (str) Package name
package.name = voiceassistant811

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Application version
version = 0.1

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the source directory)
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# (list) Application requirements
requirements = python3,kivy==2.3.0,kivymd,pyjnius

# (str) Custom source folders for requirements
# requirements.source.kivy = ../kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
permissions = RECORD_AUDIO, INTERNET, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK build tools version to use
android.sdk_build_tools_version = 33.0.2

# (bool) If True, then automatically accept SDK licenses
android.accept_sdk_licenses = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Gradle dependencies
# android.gradle_dependencies = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn, 2 = error)
warn_on_root = 1
