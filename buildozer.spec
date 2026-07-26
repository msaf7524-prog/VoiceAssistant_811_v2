[app]

# (str) Title of your application
title = VoiceAssistant

# (str) Package name
package.name = voiceassistant

# (str) Package domain
package.domain = org.test

# (str) Source code
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

# (str) Version
version = 0.1

# (list) Requirements
requirements = python3,kivy,requests,urllib3,certifi,charset_normalizer,idna,plyer,speechrecognition,gTTS,pyjnius

# (list) Android permissions
android.permissions = INTERNET,RECORD_AUDIO,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,MODIFY_AUDIO_SETTINGS,POST_NOTIFICATIONS

# (int) Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (bool) Private storage
android.private_storage = True

# (bool) Skip SDK update
android.skip_update = False

# (bool) Accept SDK licenses
android.accept_sdk_license = True

# (str) Android entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

[buildozer]

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 1
