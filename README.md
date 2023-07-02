# picoW_webserver
 
![on-SIGLA](https://github.com/acican/picoW_webserver/assets/10486613/50b697d5-1f21-453e-9764-8bf520b5dae7)

Un exemplu de cod in micropython pentru implementarea unui webserver, folosind controlerul Raspberry pico W.
- Raspberry pico W
- interpretor: rp2-pico-w-20230426-v1.20.0.uf2
  
Functioneaza prin conectarea la reteaua locala wifi, ip serverului de pe picoW depinde de domeniul alocat de ruter.
Conectarea la acesta necesita introducerea ssid-ul si password-ul retelei.
Exemplele de cod generate de chatGPG sunt in fisierele din cartela "chat", respectiv:
- cod de pagina html cu form input tip checkbox si ceva modificare de stil in fisierele chat_input_checkbox" si "chat_css". Procesarea cererii se face printr-un scurt javascript
- cod micropython de procesare a cererilor catre webserver "chat_webserver"
Codul face sa se comute nivelul unei iesiri digitale a microcontrolerului (aici pin 20) pico in starile logice 1 si 0, de la comanda on/off. este util in comandarea aprnderii unui LED, comutarii unui releu, etc.  
  
