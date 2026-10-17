# Virtual kartlar — kart buraxmaq (GRAD-201)

POST /cards. Test case-lər: Final_Project_API_Test_Cases.xlsx (TC-CRD-xxx). Hər ssenari yeni login ilə təmiz sandbox-da
başlayır. user1 = acc_002 (AZN, 12 500), user2 = acc_003 (USD, 890.50).

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-CRD-001 Etibarlı sorğu ilə kart ACTIVE statusunda və standart limitlərlə buraxılır

tags: grad-201, regression, positive, tc-crd-001

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Kommunal"
* Status kodunun "201" olmalıdır
* Cavab "card.schema.json" JSON schema-sına uyğun olmalıdır
* Header "Location" deyerini "location" olaraq yadda saxla
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Json cavabında "id" deyeri "vcd_.{8}" regex-ine uyğun olmalıdır
* "location" deyişeni "/cards/${cardId}" olmalıdır
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabını cedvel ile yoxla

   |path                |value                                  |
   |accountId           |acc_002                                |
   |label               |Kommunal                               |
   |maskedPan           |@regex:4169 73[*]{2} [*]{4} [0-9]{4}   |
   |expiry              |@regex:[0-1][0-9]/[0-9]{2}             |
   |currency            |AZN                                    |
   |status              |ACTIVE                                 |
   |availableBalance    |100                                    |
   |limits.dailyOnline  |500                                    |
   |limits.perTransaction|300                                   |
   |spentToday          |0                                      |
   |createdAt           |@regex:[0-9]{4}-[0-9]{2}-[0-9]{2}T.*   |

## TC-CRD-002 label göndərilmədikdə cavabda null qaytarılır

tags: grad-201, regression, positive, tc-crd-002

* Kart buraxılışı hesab "acc_002" məbləğ "100"
* Status kodunun "201" olmalıdır
* Json cavabında "label" açarı mövcud olmalıdır
* Json cavabında "label" deyeri null olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "100" beraberdir

## TC-CRD-003 initialAmount sərhədləri: 1.00 və 1000.00 qəbul, 0.99 və 1000.01 rədd

tags: grad-201, regression, boundary, tc-crd-003

* Kart buraxılışı hesab "acc_002" məbləğ "1.00" ləqəb "Min"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1" beraberdir
* Kart buraxılışı hesab "acc_002" məbləğ "1000.00" ləqəb "Max"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1000" beraberdir
* Kart buraxılışı hesab "acc_002" məbləğ "0.99" ləqəb "Alt"
* Validasiya xətası olmalıdır sahə "initialAmount"
* Kart buraxılışı hesab "acc_002" məbləğ "1000.01" ləqəb "Ust"
* Validasiya xətası olmalıdır sahə "initialAmount"

## TC-CRD-004 initialAmount mətn, 3 onluq və sıfır dəyərlərində rədd edilir

tags: grad-201, regression, negative, tc-crd-004

(a) mətn
* Initalize request specification
* Add Endpoint "/cards"
* Authorization header-ine tokeni elave et
* Add body as file resource "card-amount-string.json"
* Post request and display respons
* Validasiya xətası olmalıdır sahə "initialAmount"
(b) 3 onluq
* Kart buraxılışı hesab "acc_002" məbləğ "10.555" ləqəb "Onluq"
* Validasiya xətası olmalıdır sahə "initialAmount"
(c) sıfır
* Kart buraxılışı hesab "acc_002" məbləğ "0" ləqəb "Sifir"
* Validasiya xətası olmalıdır sahə "initialAmount"

## TC-CRD-005 İki onluqlu məbləğ qəbul olunur

tags: grad-201, regression, positive, tc-crd-005

* Kart buraxılışı hesab "acc_002" məbləğ "10.55" ləqəb "Onluq"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "10.55" beraberdir
* Json cavabında "spentToday" deyeri "0" beraberdir

## TC-CRD-006 label sərhədləri: 1 və 30 simvol qəbul, 31 simvol rədd

tags: grad-201, regression, boundary, tc-crd-006

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "A"
* Status kodunun "201" olmalıdır
* Json cavabında "label" deyeri "A" beraberdir
* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
* Status kodunun "201" olmalıdır
* Json cavabında "label" deyeri "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" beraberdir
* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
* Validasiya xətası olmalıdır sahə "label"

## TC-CRD-007 Boş obyekt göndərildikdə məcburi sahələr üçün xəta qaytarılır

tags: grad-201, regression, negative, tc-crd-007

* Initalize request specification
* Add Endpoint "/cards"
* Authorization header-ine tokeni elave et
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "accountId" olmalıdır
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC-CRD-008 user1 başqa istifadəçinin hesabı ilə kart aça bilmir

tags: grad-201, regression, negative, tc-crd-008

* Kart buraxılışı hesab "acc_003" məbləğ "100" ləqəb "Basqa"
* Xəta cavabı olmalıdır status "403" code "FORBIDDEN"

## TC-CRD-009 Mövcud olmayan hesab üçün 404 ACCOUNT_NOT_FOUND qaytarılır

tags: grad-201, regression, negative, tc-crd-009

* Kart buraxılışı hesab "acc_999" məbləğ "100" ləqəb "Yoxdur"
* Xəta cavabı olmalıdır status "404" code "ACCOUNT_NOT_FOUND"

## TC-CRD-010 Məbləğ hesab balansından böyük olduqda 422 INSUFFICIENT_FUNDS, balansa bərabər olduqda qəbul

tags: grad-201, regression, boundary, tc-crd-010

* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
(a) balansdan 0.50 çox
* Kart buraxılışı hesab "acc_003" məbləğ "891" ləqəb "Cox"
* Xəta cavabı olmalıdır status "422" code "INSUFFICIENT_FUNDS"
(b) balansdan 0.01 çox
* Kart buraxılışı hesab "acc_003" məbləğ "890.51" ləqəb "Cox"
* Xəta cavabı olmalıdır status "422" code "INSUFFICIENT_FUNDS"
(c) balansa bərabər, valyuta hesabın valyutası ilə eynidir
* Kart buraxılışı hesab "acc_003" məbləğ "890.50" ləqəb "Dolu"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "accountId" deyeri "acc_003" beraberdir
* Json cavabında "availableBalance" deyeri "890.5" beraberdir

## TC-CRD-011 Üç aktiv kartdan sonra dördüncü kart 422 CARD_LIMIT_REACHED qaytarır

tags: grad-201, regression, boundary, tc-crd-011

* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Bir"
* Status kodunun "201" olmalıdır
* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Iki"
* Status kodunun "201" olmalıdır
* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Uc"
* Status kodunun "201" olmalıdır
* Kart buraxılışı hesab "acc_002" məbləğ "100" ləqəb "Dord"
* Xəta cavabı olmalıdır status "422" code "CARD_LIMIT_REACHED"

## TC-CRD-012 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-201, regression, negative, tc-crd-012

(a) Authorization header göndərilmir
* "accountId" deyişenine "acc_002" deyerini ver
* "amount" deyişenine "100" deyerini ver
* Initalize request specification
* Add Endpoint "/cards"
* Add body as file resource "card-create-no-label.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
(b) saxta token
* Initalize request specification
* Add Endpoint "/cards"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Add body as file resource "card-create-no-label.json"
* Post request and display respons
* Status kodunun "401" olmalıdır