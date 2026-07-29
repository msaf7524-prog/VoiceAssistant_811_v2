[app]

title = VoiceAssistant
package.name = voiceassistant
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

version = 0.1

requirements = python3,kivy,requests,urllib3,certifi,charset_normalizer,idna,plyer,pyjnius

android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.private_storage = True
android.skip_update = False
android.accept_sdk_license = True

android.entrypoint = org.kivy.android.PythonActivity

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
