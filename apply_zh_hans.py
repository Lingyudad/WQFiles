#!/usr/bin/env python3
# Apply the verified WQFiles string translations to source files.
# Run from the extracted WQFiles source root: python3 apply_zh_hans.py
import json, pathlib, re, sys
root=pathlib.Path(__file__).resolve().parent
catalog=json.loads((root/'zh-Hans.json').read_text(encoding='utf-8'))
targets=[root/'main.m', root/'WQAccess.m']
changed=0
for path in targets:
    if not path.exists():
        continue
    text=path.read_text(encoding='utf-8')
    original=text
    for en, zh in catalog.items():
        # Match Objective-C string literal contents, preserving surrounding quotes.
        # Escape only the source literal's backslash and quote characters.
        old=en.replace('\\','\\\\').replace('"','\\"')
        new=zh.replace('\\','\\\\').replace('"','\\"')
        text=text.replace('"'+old+'"','"'+new+'"')
    if text != original:
        path.write_text(text,encoding='utf-8')
        changed += 1
        print('Updated:',path.name)
if changed == 0:
    print('No source literals matched. Confirm this is the v0.3 source tree.')
    sys.exit(2)
# Update the display name in Info.plist when present.
plist=root/'Info.plist'
if plist.exists():
    import plistlib
    data=plistlib.loads(plist.read_bytes())
    data['CFBundleDisplayName']='WQ 文件'
    data['CFBundleName']='WQFiles'
    plist.write_bytes(plistlib.dumps(data,fmt=plistlib.FMT_XML))
    print('Updated: Info.plist')
print('Done. This changes source text only; it does not compile or sign an IPA.')
