# Virtual kartlar — kartı bloklamaq / dondurmaq (GRAD-203)

POST /cards/{id}/block. Vəziyyət keçid cədvəlinin hər xanası ayrı ssenaridir.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-CBL-001 ACTIVE kart TEMPORARY səbəbi ilə dondurulur (FROZEN)

tags: grad-203, regression, positive, tc-cbl-001

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır
* Kartın statusu "FROZEN" olmalıdır

## TC-CBL-002 ACTIVE kart LOST və STOLEN səbəbləri ilə bloklanır (BLOCKED)

tags: grad-203, regression, positive, tc-cbl-002

* Test kartı yarat
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri boş olmamalıdır
* Kartın statusu "BLOCKED" olmalıdır
* Test kartı yarat
* Kartı blokla səbəb "STOLEN"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir

## TC-CBL-003 FROZEN kart LOST / STOLEN ilə bloklanır (eskalasiya)

tags: grad-203, regression, positive, tc-cbl-003

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "STOLEN"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Kartın statusu "BLOCKED" olmalıdır
* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir

## TC-CBL-004 FROZEN kart yenidən TEMPORARY ilə dondurulduqda 409 ALREADY_FROZEN

tags: grad-203, regression, negative, tc-cbl-004

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "TEMPORARY"
* Xəta cavabı olmalıdır status "409" code "ALREADY_FROZEN"
* Kartın statusu "FROZEN" olmalıdır

## TC-CBL-005 BLOCKED kart üçün istənilən səbəb 409 CARD_BLOCKED qaytarır

tags: grad-203, regression, negative, tc-cbl-005

* Test kartı yarat
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "TEMPORARY"
* Xəta cavabı olmalıdır status "409" code "CARD_BLOCKED"
* Kartı blokla səbəb "LOST"
* Xəta cavabı olmalıdır status "409" code "CARD_BLOCKED"
* Kartı blokla səbəb "STOLEN"
* Xəta cavabı olmalıdır status "409" code "CARD_BLOCKED"
* Kartın statusu "BLOCKED" olmalıdır

## TC-CBL-006 Səhv, boş və ya olmayan reason 400 VALIDATION_ERROR qaytarır

tags: grad-203, regression, negative, tc-cbl-006

* Test kartı yarat
* Kartı blokla səbəb "BROKEN"
* Validasiya xətası olmalıdır sahə "reason"
* Kartı blokla səbəb ""
* Validasiya xətası olmalıdır sahə "reason"
* Initalize request specification
* Add Endpoint "/cards/${cardId}/block"
* Authorization header-ine tokeni elave et
* Add body as text "{}"
* Post request and display respons
* Validasiya xətası olmalıdır sahə "reason"
* Kartın statusu "ACTIVE" olmalıdır

## TC-CBL-007 Body yoxdur və ya JSON deyilsə 400 INVALID_JSON qaytarılır

tags: grad-203, regression, negative, tc-cbl-007

* Test kartı yarat
* Initalize request specification
* Add Endpoint "/cards/${cardId}/block"
* Authorization header-ine tokeni elave et
* Post request and display respons
* Xəta cavabı olmalıdır status "400" code "INVALID_JSON"
* Initalize request specification
* Add Endpoint "/cards/${cardId}/block"
* Authorization header-ine tokeni elave et
* Add body as file resource "ben-invalid-json-unclosed.json"
* Post request and display respons
* Xəta cavabı olmalıdır status "400" code "INVALID_JSON"
* Kartın statusu "ACTIVE" olmalıdır

## TC-CBL-008 Yoxlama ardıcıllığı: reason validasiyası NOT_FOUND və status keçidindən əvvəl işləyir

tags: grad-203, regression, negative, tc-cbl-008

* "cardId" deyişenine "vcd_nonexist" deyerini ver
* Kartı blokla səbəb "BROKEN"
* Validasiya xətası olmalıdır sahə "reason"
* Test kartı yarat
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "BROKEN"
* Validasiya xətası olmalıdır sahə "reason"

## TC-CBL-009 Mövcud olmayan və ya başqasının kartı üçün 404 NOT_FOUND

tags: grad-203, regression, negative, tc-cbl-009

* "cardId" deyişenine "vcd_nonexist" deyerini ver
* Kartı blokla səbəb "TEMPORARY"
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"
* Test kartı yarat
* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
* Kartı blokla səbəb "TEMPORARY"
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-CBL-010 Token yoxdur və ya saxtadır — 401

tags: grad-203, regression, negative, tc-cbl-010

* Test kartı yarat
* "reason" deyişenine "TEMPORARY" deyerini ver
* Initalize request specification
* Add Endpoint "/cards/${cardId}/block"
* Add body as file resource "block-reason.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${cardId}/block"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Add body as file resource "block-reason.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Kartın statusu "ACTIVE" olmalıdır