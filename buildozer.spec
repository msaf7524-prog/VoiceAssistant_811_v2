[app]

# (str) Title of your application
title = Voice Assistant 811

# (str) Package name
package.name = voiceassistant811

# (str) Package domain (needed for android packaging)
package.domain = org.msaf

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude none)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude none)
source.exclude_dirs = bin, .git, .github, __pycache__

# (list) List of exclusions using pattern matching
source.exclude_patterns = license, images/*.jpg

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تأكد من تضمين جميع المكتبات الحيوية التي يستخدمها مشروعك
requirements = python3,kivy,plyer,android,pyjnius

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
# ربط خدمة الخلفية التي أنشأناها في ملف service.py
services = voiceservice:service.py

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (hex color code)
#android.presplash_color = #FFFFFF

# (list) Permissions
# الصلاحيات الكاملة للمايكروفون، الإنترنت، والبلوتوث للعمل عبر السماعة
android.permissions = INTERNET, RECORD_AUDIO, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, FOREGROUND_SERVICE

# (list) Features
#android.features = android.hardware.bluetooth, android.hardware.bluetooth_le

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API to use for NDK.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir storage (False)
android.private_storage = True

# (list) Android architectural to build for, 
# حصر البناء على معمارية هاتفك لتسريع العملية وتجنب أخطاء الخادم
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.androidx = True

# (str) python-for-android branch to use
p4a.branch = master

# (str) OUYA Console support
#ouya.console = false

# (list) 
#android.ouya.category = GAME

# (str) XML buid files to add
#android.manifest.xml =

# (list) Extra XML files to include for the manifest
#android.manifest.manifest_extra =

# (list) Extra XML files to include for activities
#android.manifest.activity_extra =

# (list) Included directories for meta-data
#android.manifest.meta_data =

# (list) Library projects to add
#android.manifest.library_projects =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) add java files
#android.add_java_src =

# (list) fixup the output of python-for-android
#android.add_source_libs =

# (str) The format used to package the app for release ('aab' or 'apk')
android.format = apk


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = .buildozer

# (str) Path to build output (APK)
bin_dir = ./bin
