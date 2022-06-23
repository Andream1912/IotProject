# IotProject
Progetto di Internet of Things 2021/2022. Il progetto simula un progetto IOT per l'ingresso smart di un azienda.

Il progetto si basa su due schede Zerynth.

Il primo codice si trova all'interno della cartella "IOT"
Il secondo codice si trova all'interno della cartella "IOT USCITA"

Il primo codice configura i seguenti sensori:
- Led (Rosso e Verde)
- Bottone
- LCD 16x02
- RFID
- Buzzer
- Servo Motore

Il secondo codice configura i seguenti sensori:
-Servo Motore
-RFID

Viene utilizzato per l'lcd un protocollo i2C e per l'rfid un protocollo SPI. All'inizializzazione del progetto viene configurata la rete wireless, utile per mandare i data allo zdm cloud. L'lcd è stato utilizzato per rappresentare qualsiasi eventualità all'interno del progetto come, connessione riuscita, ingressi,uscita,accessi non consentiti e infine sono stati implementati, attraverso lo zdm, dei controlli remoti per aggiungere un nuovo user,rimuoverlo e bloccare il sistema.
Il progetto simula l'ingresso di un azienda con un contatore dinamica, rappresentato sull'lcd, ad ogni ingresso e ad ogni uscita. Con la gestione, al passaggio dell'rfid, di una sbarra (servo motore) che si alza e si abbassa consentendo l'accesso ai dipendenti. In caso di nfc non riconosciuto ci sarà un buzzer e un led rosso che si accenderanno con una rappresentazione grafica su lcd "ACCESSO NON CONSENTITO". La seconda scheda invece è stata implementata per l'uscita ed invierà costantemente i dati alla scheda principale attraverso un protoccolo MQTT per permettere l'uscita, andando a decrementare il conteggio delle persone all'interno. 
