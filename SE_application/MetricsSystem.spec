# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['SE_application.py'],
             pathex=['C:\\Users\\rosha\\PycharmProjects\\FunctionPointGUIprogram\\SE_application'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib', 'scipy', 'setuptools', 'hook', 'distutils', 'site', 'hooks', 'tornado', 'PIL', 'mysql-connector-python', 'pydoc', 'pythoncom', 'pytz', 'pywintypes', 'sqlite3', 'pyz', 'pandas', 'numpy', 'sklearn', 'scapy', 'scrapy', 'sympy', 'kivy', 'pyramid', 'opencv', 'tensorflow', 'pipenv', 'pattern', 'mechanize', 'beautifulsoup4', 'requests', 'wxPython', 'pygi', 'pillow', 'pygame', 'pyglet', 'flask', 'django', 'pylint', 'pytube', 'odfpy', 'mccabe', 'pilkit', 'six', 'wrapt', 'astroid', 'isort', 'XlsxWriter', 'zipp'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MetricsSystem',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
