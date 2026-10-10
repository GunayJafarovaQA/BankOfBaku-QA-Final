# GRAD-302 Kommunal ödəniş

POST /bill-payments. Hər ssenari "Ödəniş kartı yarat" ilə təmiz sandbox-da yeni kart açır.

## TC-PAY-001 CityNet 50 AZN uğurlu ödəniş: fee, total, balanceAfter

tags: grad-302, regression, positive, tc-pay-001

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "pay-001-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "50.5" beraberdir
* Json cavabında "balanceAfter" deyeri "49.5" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "biller.id" deyeri "citynet" beraberdir

## TC-PAY-002 Ödənişdən sonra kartın balansı və spentToday yenilənir

tags: grad-302, regression, positive, tc-pay-002

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "pay-002-${timestamp}"
* Status kodunun "201" olmalıdır
* Kartın qalıq balansı "49.5" xərclənən "50.5" olmalıdır

## TC-PAY-003 Eyni açar və eyni body: 200, eyni id, balans ikinci dəfə azalmır

tags: grad-302, regression, positive, tc-pay-003

* Ödəniş kartı yarat məbləğ "100"
* "key" deyişenine "pay-003-${timestamp}" deyerini ver
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "${key}"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "firstId" olaraq yadda saxla
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "${key}"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${firstId}" beraberdir
* Kartın qalıq balansı "49.5" xərclənən "50.5" olmalıdır

## TC-PAY-004 Eyni açar, fərqli məbləğ: 409 IDEMPOTENCY_CONFLICT

tags: grad-302, regression, negative, tc-pay-004

* Ödəniş kartı yarat məbləğ "100"
* "key" deyişenine "pay-004-${timestamp}" deyerini ver
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "${key}"
* Status kodunun "201" olmalıdır
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "51" açar "${key}"
* Xəta cavabı olmalıdır status "409" code "IDEMPOTENCY_CONFLICT"

## TC-PAY-005 Idempotency-Key qısa (7 simvol): 400

tags: grad-302, regression, boundary, tc-pay-005

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "abcdefg"
* Xəta cavabı olmalıdır status "400" code "IDEMPOTENCY_KEY_INVALID"

## TC-PAY-006 Idempotency-Key sərhəd (8 simvol) qəbul olunur

tags: grad-302, regression, boundary, tc-pay-006

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "50" açar "abcdefgh"
* Status kodunun "201" olmalıdır

## TC-PAY-007 Azercell-ə Bakcell nömrəsi: 422 INVALID_SUBSCRIBER

tags: grad-302, regression, negative, tc-pay-007

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "azercell" abunəçi "551234567" məbləğ "10" açar "pay-007-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "INVALID_SUBSCRIBER"

## TC-PAY-008 Azercell məbləğ 0.49: 422 AMOUNT_OUT_OF_RANGE

tags: grad-302, regression, boundary, tc-pay-008

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "azercell" abunəçi "501234567" məbləğ "0.49" açar "pay-008-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "AMOUNT_OUT_OF_RANGE"

## TC-PAY-009 Azercell məbləğ 0.50 (aşağı sərhəd) qəbul olunur

tags: grad-302, regression, boundary, tc-pay-009

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "azercell" abunəçi "501234567" məbləğ "0.50" açar "pay-009-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0" beraberdir

## TC-PAY-010 Azercell məbləğ 200.01: 422 AMOUNT_OUT_OF_RANGE

tags: grad-302, regression, boundary, tc-pay-010

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "azercell" abunəçi "501234567" məbləğ "200.01" açar "pay-010-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "AMOUNT_OUT_OF_RANGE"

## TC-PAY-011 CityNet komissiya: 5 AZN → 0.20 (minimum)

tags: grad-302, regression, boundary, tc-pay-011

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "5" açar "pay-011-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.2" beraberdir

## TC-PAY-012 CityNet komissiya: 21 AZN → 0.21

tags: grad-302, regression, boundary, tc-pay-012

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "21" açar "pay-012-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.21" beraberdir

## TC-PAY-013 CityNet komissiya: 150 AZN → 1.50 (maksimum məbləğ)

tags: grad-302, regression, boundary, tc-pay-013

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "150" açar "pay-013-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "1.5" beraberdir

## TC-PAY-014 Aztelekom sabit komissiya 0.50

tags: grad-302, regression, positive, tc-pay-014

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "aztelekom" abunəçi "1234567" məbləğ "100" açar "pay-014-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "100.5" beraberdir

## TC-PAY-015 total 300.01: 422 PER_TRANSACTION_LIMIT

tags: grad-302, regression, boundary, tc-pay-015

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "300.01" açar "pay-015-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "PER_TRANSACTION_LIMIT"

## TC-PAY-016 total 300.00 keçir

tags: grad-302, regression, boundary, tc-pay-016

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "300" açar "pay-016-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "700" beraberdir

## TC-PAY-017 Balans 49.50, ödəniş 49.51: 422 INSUFFICIENT_FUNDS

tags: grad-302, regression, boundary, tc-pay-017

* Ödəniş kartı yarat məbləğ "49.5"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "49.51" açar "pay-017-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "INSUFFICIENT_FUNDS"

## TC-PAY-018 Balans 49.50, ödəniş 49.50: 201, balanceAfter 0

tags: grad-302, regression, boundary, tc-pay-018

* Ödəniş kartı yarat məbləğ "49.5"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "49.5" açar "pay-018-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "0" beraberdir

## TC-PAY-019 Komissiya total-a daxildir: balans 100, CityNet 100 → total 101 > balans

tags: grad-302, regression, negative, tc-pay-019

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "citynet" abunəçi "CN123456" məbləğ "100" açar "pay-019-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "INSUFFICIENT_FUNDS"
## TC-PAY-020 Gündəlik limit: 500 xərclənibsə 1 AZN də 422 DAILY_LIMIT_EXCEEDED, remaining 0

tags: grad-302, regression, boundary, tc-pay-020

* Ödəniş kartı yarat məbləğ "1000"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "300" açar "pay-020-a-${timestamp}"
* Status kodunun "201" olmalıdır
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "200" açar "pay-020-b-${timestamp}"
* Status kodunun "201" olmalıdır
* Kartın qalıq balansı "500" xərclənən "500" olmalıdır
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "1" açar "pay-020-c-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "DAILY_LIMIT_EXCEEDED"
* Json cavabında "remaining" deyeri "0" beraberdir

## TC-PAY-021 Dondurulmuş kart: 422 CARD_NOT_ACTIVE

tags: grad-302, regression, negative, tc-pay-021

* Ödəniş kartı yarat məbləğ "100"
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-021-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "CARD_NOT_ACTIVE"
* Kartın qalıq balansı "100" xərclənən "0" olmalıdır

## TC-PAY-022 Bloklanmış kart (LOST): 422 CARD_NOT_ACTIVE

tags: grad-302, regression, negative, tc-pay-022

* Ödəniş kartı yarat məbləğ "100"
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-022-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "CARD_NOT_ACTIVE"

## TC-PAY-023 Açılmış kartla ödəniş keçir (GRAD-204 AC-4)

tags: grad-302, regression, positive, tc-pay-023

* Ödəniş kartı yarat məbləğ "100"
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokdan çıxar
* Status kodunun "200" olmalıdır
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-023-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "90" beraberdir

## TC-PAY-024 USD kart: 422 CURRENCY_NOT_SUPPORTED

tags: grad-302, regression, negative, tc-pay-024

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
* Kart buraxılışı hesab "acc_003" məbləğ "100" ləqəb "UsdCard"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-024-${timestamp}"
* Xəta cavabı olmalıdır status "422" code "CURRENCY_NOT_SUPPORTED"

## TC-PAY-025 receiptNo ardıcıllığı: ilk ödəniş 000001, ikinci 000002

tags: grad-302, regression, positive, tc-pay-025

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-025-a-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla

   |path     |value                    |
   |receiptNo|@regex:RCP-[0-9]{8}-000001|

* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-025-b-${timestamp}"
* Status kodunun "201" olmalıdır
* Json cavabını cedvel ile yoxla

   |path     |value                    |
   |receiptNo|@regex:RCP-[0-9]{8}-000002|

## TC-PAY-026 Idempotency-Key header yoxdur: 400 IDEMPOTENCY_KEY_REQUIRED

tags: grad-302, regression, negative, tc-pay-026

* Ödəniş kartı yarat məbləğ "100"
* "billerId" deyişenine "citynet" deyerini ver
* "subscriberNo" deyişenine "CN123456" deyerini ver
* "amount" deyişenine "10" deyerini ver
* Initalize request specification
* Add Endpoint "/bill-payments"
* Authorization header-ine tokeni elave et
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "pay-create.json"
* Post request and display respons
* Xəta cavabı olmalıdır status "400" code "IDEMPOTENCY_KEY_REQUIRED"

## TC-PAY-027 amount mətn kimi göndərilir: 400 VALIDATION_ERROR

tags: grad-302, regression, negative, tc-pay-027

* Ödəniş kartı yarat məbləğ "100"
* Initalize request specification
* Add Endpoint "/bill-payments"
* Authorization header-ine tokeni elave et
* Add as a header "Idempotency-Key" = "pay-027-${timestamp}"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "pay-amount-string.json"
* Post request and display respons
* Validasiya xətası olmalıdır sahə "amount"

## TC-PAY-028 Mövcud olmayan təchizatçı: 404 BILLER_NOT_FOUND

tags: grad-302, regression, negative, tc-pay-028

* Ödəniş kartı yarat məbləğ "100"
* Ödəniş göndər təchizatçı "gazprom" abunəçi "1234567890" məbləğ "10" açar "pay-028-${timestamp}"
* Xəta cavabı olmalıdır status "404" code "BILLER_NOT_FOUND"

## TC-PAY-029 Mövcud olmayan kart: 404 CARD_NOT_FOUND

tags: grad-302, regression, negative, tc-pay-029

* Ödəniş kartı yarat məbləğ "100"
* "cardId" deyişenine "vcd_nonexist" deyerini ver
* Ödəniş göndər təchizatçı "azerisiq" abunəçi "1234567890" məbləğ "10" açar "pay-029-${timestamp}"
* Xəta cavabı olmalıdır status "404" code "CARD_NOT_FOUND"

## TC-PAY-030 Token yoxdur: 401

tags: grad-302, regression, negative, tc-pay-030

* Ödəniş kartı yarat məbləğ "100"
* "billerId" deyişenine "citynet" deyerini ver
* "subscriberNo" deyişenine "CN123456" deyerini ver
* "amount" deyişenine "10" deyerini ver
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Idempotency-Key" = "pay-030-${timestamp}"
* Add as a header "Content-Type" = "application/json"
* Add body as file resource "pay-create.json"
* Post request and display respons
* Status kodunun "401" olmalıdır