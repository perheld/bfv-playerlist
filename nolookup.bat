powershell -Command "Start-Process 'python' -Verb runAs -ArgumentList 'nolook.py'"
@if NOT ["%errorlevel%"]==["0"] pause
