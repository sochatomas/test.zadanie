# Microservice v pythone
 Program zabezpečuje RESTful API na spravovanie príspevkov používateľov.

## Spustenie programu
### Inštalácia
 Nainštalovanie Pythonu vo verzií 3.9
 
 Inštalácia flask , sqlalchemy, requests, flask_restful, flask_sqlalchemy (napr. pomocou príkazu "pip install <nazov_kniznice>" v termináli)

### Prvé spustenie
Do terminalu zadať postupne príkazy:
```sh
python
from app import db
db.create_all()
exit()
flask run
```
## Požiadavky

### Funkčné požiadavky
- Pridanie príspevku - potrebné validovať userID pomocou externej API
- Zobrazenie príspevku
   - na základe id alebo userId
   - ak sa príspevok nenájde v systéme, je potrebné ho dohľadať pomocou externej API a uložiť (platné iba pre vyhľadávanie pomocou id príspevku)
- Odstránenie príspevku
- Upravenie príspevku - možnosť meniť title a body

### Všeobecné požiadavky:
- ReadMe s popisom inštalácie a prvého spustenia
- Dokumentácia API (napr. Swagger)
- Validácia vstupných dát
- Použitie ORM

Externá API na linku https://jsonplaceholder.typicode.com/ - používané endpointy users a posts.

 #### Formát príspevku
>{
>       "id": integer
>       "userId": integer
>        "title": string
>       "body": string
>}
