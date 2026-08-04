[app]
title = VoiceAssistant811
package.name = voiceassistant811
package.domain = org.assistant811

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

version = 0.1

requirements = python3,kivy==2.3.0,pyjnius,requests,arabic_reshaper,python-bidi

android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.private_storage = True
android.accept_sdk_licenses = True

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0
