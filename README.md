# yuki-emby-crack

## Об этом проекте
Этот репозиторий является ответвлением проекта MitsuhaYuki [yuki-emby-crack](https://github.com/MitsuhaYuki/yuki-emby-crack), служит целям перевода документации программы на русский язык, популяризации Emby Media Server в русскоязычной среде, актуализации "сертификатов для ленивых", и :warning: **НЕ СОДЕРЖИТ ИЗМЕНЕНИЙ В КОДЕ ПРОГРАММЫ!**

## Принцип работы
Каждая программа-клиент Emby активируется отдельно на сервере активации Emby, расположенном в сети Интернет по адресу `mb3admin.com`. Этот проект подменяет сервер активации приложений Emby фейковым сервером активации приложений, расположенным на вашем `localhost`, и удостоверенным фейковым корневым центром сертификации.

## Ограничения
Этот метод ограничен системами и устройствами, на которых можно организовать перенаправление активации на фейковый сервер активации и возможна установка сертификата фейкового корневого центра сертификации.

## Результат

> Активированный браузер на Windows

![i-demo-1](images/i-demo-1.png)

> Просмотр эфира (Premiere-функция) на Emby Theater в Windows

![i-demo-4](images/i-demo-4.jpg)

## Установка

### 1. Разархивируйте файлы

Скачайте `dist.zip` со страницы [`release`](https://github.com/nbb1967/yuki-emby-crack/releases) и разархивируйте его в любую папку. Запустите `main.exe`. 

![i-dist.png](images/i-unzip.png)

### 2. Настройте автоматический запуск

Щелкните правой кнопкой по `main.exe`，и выберите `Создать ярлык`，переместите `main.exe - ярлык` в папку `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`. Вы можете перименовать ярлык.

![i-autostart.png](images/i-autostart-1.png)

![i-autostart.png](images/i-autostart-2.png)

### 3. Внесите изменения в файл hosts

Откройте файл `hosts` расположенный в `C:\Windows\System32\drivers\etc`и внесите в конец файла следующую строку：

```
 127.0.0.1 mb3admin.com
```

> Программа, в которой вы редактируете файл `hosts` (например, `Блокнот`) должна быть запущена от имени администратора

> После строки `127.0.0.1 mb3admin.com` не забудьте вставить пустую строку，иначе изменения могут быть проигнорированы

### 4. Установите сертификат

Дважды щелкните по файлу `frca.cer` в папке `root`，и нажмите кнопку `Установить сертификат...`. В открывшемся окне выберите `Текущий пользователь` - `Далее` - `Поместить все сертификаты в следующее хранилище`，нажмите кнопку `Обзор` и выберите `Доверенные корневые центры сертификации`，затем нажмите `ОК` - `Далее` - `Готово`, чтобы завершить `Мастер импорта сертификатов`. Подтвердите установку сертификата: `Да` - `OK`

![i-installcert](images/i-installcert.png)

### 5. Перезапустите Emby Server

Щелкните правой кнопкой мыши по значку Emby Server в панели уведомлений и выберите `Перезапуск Emby Server`. Дождитесь пока сервер перезапуститься. Откройте панель управления сервера, вы должны увидеть золотой значок `Emby Premiere`. Но это не всё!

### 6. Введите ключ

Перейдите на вкладку `Emby Premiere` и введите любые символы в поле `Ключ Emby Premiere`, нажмите кнопку `Сохранить`.

## FAQ

### Активация не удалась

#### ШАГ 1：Проверьте запущена ли программа

Откройте `Диспетчер задач` и прокрутите вниз，если программа запущена，вы должны увидеть два процесса `main.exe`

![i-step1](images/i-step1.png)

если вы не видите их там, вернитесь к настройке автозапуска，или запустите `main.exe` вручную

#### ШАГ 2：Проверьте перенаправление в файле hosts

Запустите `Командную строку` и введите в неё `ping mb3admin.com`，вы должны увидеть что-то похожее:

![i-step2](images/i-step2.png)

Если вы не видите адреса 127.0.0.1, значит возникла проблема с файлом hosts и вам нужно вернуться к его редактированию 

#### ШАГ 3：Проверьте наличие проблем с прокси-сервером или сертификатом

Если всё вышеперечисленное в порядке, откройте в браузере адрес [`https://mb3admin.com`](https://mb3admin.com), в идеале вы должны увидеть следующее: 

![i-step3-1](images/i-step3-1.png)

Если вы получаете сообщение об ошибке сертификата, то вернитесь к шагу установки сертификата.
Если вы не видите такой же картины в своем браузере, и на первых двух шагах все в порядке, проверьте не используете ли вы какие-либо прокси-плагины, отключите их, перезапустите браузер и повторите попытку. Если все еще не работает, перейдите в `Параметры Windows` - `Сеть и Интернет` - `Прокси-сервер` и убедитесь, что переключатель `Использовать прокси-сервер` выключен.

![i-step3-2](images/i-step3-2.png)

> Это не значит, что нельзя использовать эту программу совместно с прокси-сервером, нужно добавить адрес `mb3admin.com` в исключения прокси-сервера, чтобы этот адрес открывался напрямую, в обход прокси-сервера. 

#### ШАГ 4：Все еще не работает？

Тогда, увы, вам придется решать это самостоятельно.

Вы можете запустить программу в командной строке командой `main.exe > log.txt 2> errorlog.txt`. Это создаст файлы журналов в папке программы.

## Дополнительно

### О составе релиза

В релизе новый корневой сертификат (мой), новый сертификат (и ключ) сервера активации и оригинальный файл из [release v0.0.3](https://github.com/MitsuhaYuki/yuki-emby-crack/releases/tag/v0.0.3), подписанный с целью снижения количества ложных срабатываний антивирусов.

### Самостоятельная компиляция

По самостоятельной компиляции читайте [оригинальную инструкцию](https://github.com/MitsuhaYuki/yuki-emby-crack#%E8%87%AA%E8%A1%8C%E7%BC%96%E8%AF%91) MitsuhaYuki 

### Активация других устройств в локальной сети

Фейковый сервер активации запущен на localhost, и доступен лишь приложениям на этом компьютере. Чтобы сделать его доступным в локальной сети, нужно организовать переадресацию порта (potr-forwarding) с IP-адреса компьютера в локальной сети <LAN_IP> (компьютера, на котором запущен фейковый сервер активации) на его localhost (127.0.0.1):
```
netsh interface portproxy add v4tov4 listenport=443 listenaddress=<LAN_IP> connectport=443 connectaddress=127.0.0.1
```
и создать входящее правило в брандмауэре Защитника Windows для 443 порта (не привязывая его к main.exe):
```
netsh advfirewall firewall add rule name=”443 TCP for yuki-emby-crack” protocol=TCP dir=in localip=<LAN_IP> localport=443 action=allow profile=private
```
На компьютере в локальной сети с приложением, которое требуется активировать, нужно установить сертификат фейкового корневого центра сертификации, а в его файле hosts организовать перенаправление на IP-адрес компьютера, на котором запущен фейковый сервер активации.
```
 <LAN_IP> mb3admin.com
```
> Аналогично, если это нужно, можно организовать проброс порта и в сеть Интернет...

### О сертификатах

:warning: **Предупреждение**: использование чужого сертификата в качестве доверенного корневого удостоверяющего центра небезопасно. Рекомендуется выпустить свой собственный сертификат!

Но можно и не выпускать...

### Выпуск собственных сертификатов в Windows

Загружаем и устанавливаем последний [Win64 OpenSSL Light](https://slproweb.com/products/Win32OpenSSL.html)  
Запускаем `cmd` от админа

переходим в каталог с `openssl.exe:`

```
cd C:\Program Files\OpenSSL-Win64\bin
```

создаем папки для сертификатов:

```
md root cert code
```

создаем корневой ключ (задаем и повторяем пароль корневого ключа (он не отображается - это нормально)):

```
openssl genrsa -aes256 -out root/frca.key 4096
```

создаем сертификат корневого центра сертификации (подтверждаем паролем корневого ключа):

```
openssl req -key root/frca.key -new -x509 -days 7306 -sha256 -subj "/CN=Fake Root CA for Emby" -addext "basicConstraints = CA:TRUE, pathlen:0" -addext "keyUsage = keyCertSign" -out root/frca.crt
```

создаем ключ сервера (без пароля):

```
openssl genrsa -out cert/server.key 4096
```

создаем сертификат сервера: 

```
openssl req -key cert/server.key -new -x509 -days 3653 -sha256 -CA root/frca.crt -CAkey root/frca.key -subj "/CN=mb3admin.com" -addext "basicConstraints = CA:FALSE" -addext "keyUsage = digitalSignature,keyEncipherment,dataEncipherment" -addext "extendedKeyUsage = serverAuth, clientAuth" -addext "subjectAltName=DNS:*.mb3admin.com,DNS:mb3admin.com" -out cert/server.crt
```

создаем ключ для подписания кода (задаем и повторяем пароль корневого ключа):

```
openssl genrsa -aes256 -out code/codesign.key 4096
```

создаем сертификат подписания кода (подтверждаем паролем ключа подписания кода и паролем корневого ключа):

```
openssl req -key code/codesign.key -new -x509 -days 3653 -sha256 -CA root/frca.crt -CAkey root/frca.key -subj "/CN=Fake Code Signing for Emby" -addext "basicConstraints = CA:FALSE" -addext "keyUsage = digitalSignature" -addext "extendedKeyUsage = codeSigning" -out code/codesign.crt
```

извлекаем `PFX` для подписания приложения (подтверждаем паролем ключа подписания кода, задаем и повторяем пароль для экспорта в `PFX`):

```
openssl pkcs12 -export -out code/codesign.pfx -inkey code/codesign.key -in code/codesign.crt
```

Забираем из папки `root` `frca.crt` - сертификат вашего нового фейкового корневого центра сертификации и устанавливаем его для текущего пользователя в доверенные корневые центры сертификации  
Забираем целиком папку `cert` с файлами `server.crt` и `server.key` - это ваш новый сертификат и ключ фейкового сервера активации - помещаем папку `cert` рядом с `main.exe`  

### Цифровая подпись main.exe

Устанавливаем [Windows 10 SDK](https://developer.microsoft.com/ru-ru/windows/downloads/windows-sdk/): только `App Certification Kit`  
Временно (до окончания сеанса `cmd`) добавляем `signtool` в `PATH`: 

```
set PATH=%PATH%;C:\Program Files (x86)\Windows Kits\10\App Certification Kit
```

Копируем `main.exe` в папку `code`

Подписываем `main.exe` (предварительно заменив <PASSWORD_PFX> на пароль `PFX`):

```
signtool sign /f code/codesign.pfx /p <PASSWORD_PFX> /t http://timestamp.digicert.com /fd SHA256 code/main.exe
```

Из папки `code` забираем подписанный `main.exe`

## На всякий случай...

##### Как удалить сертификат?    

Чтобы удалить сертификат фейкового корневого центра сертификации из доверенных корневых центров сертификации текущего пользователя, нажмите `Win+R`, введите `certmgr.msc`, нажмите `OK`. В открывшемся окне программы `Сертификаты` выберите  `Сертификаты — текущий пользователь` - `Доверенные корневые центры сертификации` - `Сертификаты`. Найдите в списке и выделите `Fake Root CA for Emby`, в контекстное меню по правой кнопке выберите `Удалить` и подтвердите удаление: `Да` - `Да`

##### Как удалить-просмотреть переадресацию порта?

Показать все правила переадресации:

```
netsh interface portproxy show all
```

Удалить правило:

```
netsh interface portproxy delete v4tov4 listenport=443 listenaddress=<LAN_IP>
```

Полный сброс:

```
netsh interface portproxy reset
```

##### Как удалить правило брандмауэра Защитника Windows?

```
netsh advfirewall firewall delete rule name="443 TCP for yuki-emby-crack"
```

