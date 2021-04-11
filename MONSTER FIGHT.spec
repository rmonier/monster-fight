# -*- mode: python ; coding: utf-8 -*-

import sys

block_cipher = None


a = Analysis(['MONSTER FIGHT.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('DEPENDANCES/audio', 'DEPENDANCES/audio'),
                 ('DEPENDANCES/images', 'DEPENDANCES/images'),            
                 ('DEPENDANCES/polices', 'DEPENDANCES/polices')             
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MONSTER FIGHT',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          windowed=True,
          icon='DEPENDANCES/images/icone.ICO')

if sys.platform == 'darwin':
    app = BUNDLE(exe,
                 name='MONSTER FIGHT.app',
                 icon='DEPENDANCES/images/icone.ICO',
                 bundle_identifier=None)