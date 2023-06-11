powershell -Command "Start-Process 'python' -Verb runAs -ArgumentList 'playerlist.py'"
@if NOT ["%errorlevel%"]==["0"] pause
