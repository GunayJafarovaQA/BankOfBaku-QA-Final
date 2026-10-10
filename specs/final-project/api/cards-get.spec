# Virtual kartlar — kart məlumatına baxmaq (GRAD-202)

GET /cards/{id}. Test case-lər: Final_Project_API_Test_Cases.xlsx (TC-CGT-xxx). Hər ssenari yeni login ilə təmiz sandbox-da
başlayır.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-CGT-001 Yeni buraxılmış kartı GET etdikdə POST cavabı ilə eyni dəyərlər qaytarılır

tags: grad-202, regression, positive, tc-cgt-001

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Json cavabında "maskedPan" deyerini "pan" olaraq yadda saxla
* Json cavabında "expiry" deyerini "exp" olaraq yadda saxla
* Json cavabında "createdAt" deyerini "created" olaraq yadda saxla
* Initalize request specification
* Add Endpoint "/cards/${cardId}"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabını cedvel ile yoxla

   |path                 |value        |
   |id                   |${cardId}    |
   |accountId            |acc_002      |
   |label                |Kommunal     |
   |maskedPan            |${pan}       |
   |expiry               |${exp}       |
   |currency             |AZN          |
   |status               |ACTIVE       |
   |availableBalance     |100          |
   |limits.dailyOnline   |500          |
   |limits.perTransaction|300          |
   |spentToday           |0            |
   |createdAt            |${created}   |

## TC-CGT-002 Mövcud olmayan kart id-si üçün 404 NOT_FOUND qaytarılır

tags: grad-202, regression, negative, tc-cgt-002

* Initalize request specification
* Add Endpoint "/cards/vcd_nonexist"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-CGT-003 Başqa istifadəçinin kartına baxmaq cəhdi 404 NOT_FOUND qaytarır

tags: grad-202, regression, negative, tc-cgt-003

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
* Initalize request specification
* Add Endpoint "/cards/${cardId}"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-CGT-004 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-202, regression, negative, tc-cgt-004

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Kommunal"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
(a) Authorization header göndərilmir
* Initalize request specification
* Add Endpoint "/cards/${cardId}"
* Get request and display respons
* Status kodunun "401" olmalıdır
(b) saxta token
* Initalize request specification
* Add Endpoint "/cards/${cardId}"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Get request and display respons
* Status kodunun "401" olmalıdır