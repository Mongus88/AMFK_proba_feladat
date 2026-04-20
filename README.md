# Aktív Magyarország Fejlesztési Központ próba feladat megoldása

## 1. feladat E2E (UI) Tesztelés
### Teszt esetek
| Teszteset száma | Teszteset címe                   | Leírás                                                                                                         | Alkalmazás tesztelt része  | Előfeltétel                                           | Tesztadatok                                                   | Teszt lépések                                                                                                                                                                                                                                                                                                                                                  | Elvárt eredmény                                                                                 | Valós eredmény                                                    |
|-----------------|----------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------|-------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| TC01            | login, érvényes adatokkal        | login oldalra érvényes adatokkal lépsz be és megnézed sikerül-e                                                | login                      | ne legyél bejelentkezve                               | Username: standard_user<br/>Password: secret_sauce            | 1. navigálj a login oldalra<br/>2.töltsd ki a mezőket a tesztadatokkal<br/>3.kattints a Login gombra                                                                                                                                                                                                                                                           | megnyílik a fő oldal ahol a termékek vanak                                                      | megnyílik a fő oldal a termékekkel                                |
| TC02            | kosár, tartalom ellenőrzése      | a kosárba helyezel egy terméket és megnézed, hogy az került-e bele                                             | kosár                      | - legyél bejelentkezve<br/>- a kosár legyen üres      | termék neve: Sauce Labs Backpack                              | 1. navigálj a fő oldalra<br/>2. a Sauce Labs Backpack terméknél kattints a Add to cart gombra<br/>3. kattints a kosár piktogrammra                                                                                                                                                                                                                             | a kosárban a Sauce Labs Backpack termék szerepel                                                | a kosárban a Sauce Labs Backpack termék szerepel                  |
| TC03            | checkout, érvényes adatokkal     | a checkout-ot érvényes adatokkal töltöd ki és ellenőrzöd az összegző oldalon az a termék van amit választottál | checkout                   | - legyél bejelentkezve<br/>- a kosárban legyen termék | Firts Name: test1<br/>Last Name: test2<br/>Zip/Postal Code: 5600 | 1. navigálj a kosár oldalra<br/>2. kattints a Checkout gombra<br/>3. töltsd ki a mezőket a tesztadatokkal<br/>4. kattints a Continue gombra                                                                                                                                                                                                                    | megnyílik az összesítő oldal és az a termék van benne ami a kosárban volt                       | az oldal betölt és az a termék van benne ami a kosárban szerepelt |
| TC04            | sikeres rendelés, visszaigazolás | egy teljes rendelési folyamaton mész végig                                                                     | login -> checkout complite | n/a                                                   | Username: standard_user<br/>Password: secret_sauce<br/>termék neve: Sauce Labs Backpack<br/>Firts Name: test1<br/>Last Name: test2<br/>Zip/Postal Code: 5600| 1. navigálj a login oldalra<br/>2.töltsd ki a mezőket a tesztadatokkal<br/>3.kattints a Login gombra<br/>4.a Sauce Labs Backpack terméknél kattints a Add to cart gombra<br/>5. kattints a kosár piktogrammra <br/>6. kattints a Checkout gombra<br/>7. töltsd ki a mezőket a tesztadatokkal<br/>8. kattints a Continue gombra<br/>9. kattints a Finish gombra | betölt a Checkout: Complete! oldal és megjelenik a következő felirat: Thank you for your order! | a sikeres order felirat megjelent                                 |
### Teszt futtatás
1. Menj az Actions fülre.
2. Bal oldalon válaszd ki a Playwright Tests (with uv) workflow-t.
3. Megjelenik egy kék sáv: "Run workflow".
4. Kattints rá, és a kis ablakba beírhatod a teszt fájl nevét (pl. login_test.py). Ha üresen hagyod, lefut minden teszt.  

A teszt lefutása után letölthető egy html formátumú összegzés, hogy sikerültek a tesztek.
### Összegzés
A tesztcsomagot úgy készítettem el, hogy bővíthető legyen további tesztekkel és új oldalakkal. Ez a POM struktúrának köszönhető.
A selectorok megtalálásához törekedtem a get_by_roll és get_by_text locatorokat használni, mivel ezek működése hasonlít legjobban
egy emberi felhasználó viselkedéséhez. Az akadálymentesített oldalak tesztelésére is alkalmazhatók. Ahol ezek nem működnek ott testID-t
vagy placeholder-t használtam.  

TC01-03 happy path tesztek a fejlesztési folyamat és hibakeresésnél lesznek hasznosak. Ezek nem a teljes folyamaton mennek végig így időben gyorsabban lefutnak.
Az egymásra épülés miatt a hibákat könnyebben meg lehet találni mert ha a TC02 elbukik akkor tudjuk hogy a kosárnál van a gond.  
Szükséges lenne még negatív teszteket is készíteni, hogy még nagyobb lefedetséget érjünk el.

A TC04 teszt a regressziós csomagba szánnám mert itt a teljes folyamatot teszteljük érvényes adatokkal, ez megfelel egy smoke tesztnek.
Ha ez elbukik akkor nincs értelme további teszteknek. Egy webshopon az ügyfél gyors, pontos és akadálymentes kiszolgálása a legfontosabb.
Ezzel a teszttel a kockázatokat nagyban tudjuk csökkenteni.  

## 2. API Tesztelés
Niquests API tesztelő keretrendszerrel szerettem volna megoldani a feladatot de 403-as státusz kódot kapok a GET kérésre. A 403 Forbidden azt jelenti, hogy nincs hozzáférési jogom
és szerver megtagadja a kérést. (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/403) claude AI szerint ennek az lehet az oka, hogy a niquests modern API tesztelő ezért az oldal robotként érzékeli.
Próbáltam a kérést úgy csomagolni (a header átírásával) mintha az egy böngészőből érkezne, de nem jártam sikerrel. Az oldalt böngészőben megnyitva látható, hogy API key kell a kapcsolathoz.  

#### update  
Az oldalra regisztrálás után tudunk API kulcsot kapni és így a szervertől nem kapunk 403-as kódot. Az AI ezt nem tudta ezért mondhatta azt, hogy robotként azonosít a szerver. A három teszt elksézült. 
### Ennél a feladatnál a következőket tesztelném
* státuszkod jó? 200 == 200
* adatstrúktúra ellenőrzés: ellenőrzöm hogy a válasz tartalmazza a kötelező mezőket:  pl.: id, email, first_name, last_name
* adattípus ellenőrzés: validálom, hogy pl.: az id integere-e vagy, hogy az email-ben van @  
## 3. Release Notes
### a.
Kedves Ügyfelünk örömmel tájékoztatjuk, hogy jogszabálykövetően kezeljük a cookikat a weboldalon. Ezzel is biztosítva a még biztonságosabb
böngészést az oldalunkon.
### b.
Kedves Ügyfelünk a szállásfoglaló rendszerünk mostmár alkalmas, hogy a foglalási adatokat összhangban lássa a szállásfoglaló oldalak (pl. Booking, Airbnb) adataival.
Így elkerülhetők a túlfoglalások.
### c.
Kedves Ügyfelünk a zavartalan működés érdekében új automata rendszert vezettünk be a szerverleállások észlelésére.
Kollégáink még gyorsabban tudják elhárítani az esetleges hibákat.