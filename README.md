# BusinessReports
## Synopsis

BusinessReports application is Django web application based on this application
https://github.com/gregpinero/django-mr_reports

## Installation in polish

1. Zainstaluj Python 2.7.13, dodaj do zmiennych środowiskowych zmienną PYTHON_HOME o wartości C:\Python27, 
   potem dodaj na końcu zmiennej PATH %PYTHON_HOME%\;%PYTHON_HOME%\Scripts
   Polecenie python powinno działać.

2. Ściągnij get-pip.py, następnie uruchom python get-pip.py

3. Zainstalowanie wkhtmltopdf: wkhtmltox-0.12.4_mingw-w64-cross-win32.exe bądź 64
   Należy zainstalować w C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe

4. Zainstaluj Microsoft Visual C++ for Pyhon 2.7

5. pip install -r requirements.txt
   Gdy pojawią się problemy z M2CryptoWin trzeba zainstalować M2Crypto-0.21.1.win-amd64-py2.7.exe
   Problemy z django-auth-ldap można zignorować

6. Wygenerowanie tabel bazy danych + stworzenie admina: python manage.py syncdb

7. python manage.py runserver

8. Idź do http://127.0.0.1:8000/admin/

// python setup.py install tworzy zbudowaną wersję

