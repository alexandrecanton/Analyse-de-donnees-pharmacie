# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Users\\Alexandre\\Desktop\\pharmacie_project\\Analyse de donnees pharmacie'],
             binaries=[],
             datas=[(r'C:\Users\alexa\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\folium\templates','folium_templates'),
             (r'C:\Users\alexa\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\branca','branca'),
             ('background.jpg','.'),
             ('logo-pharmacie-médical.ico','.')],
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
          [],
          exclude_binaries=True,
          name='Medical_Data_Analyer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
