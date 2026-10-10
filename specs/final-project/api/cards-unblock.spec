# Virtual kartlar — dondurulmuş kartı açmaq (GRAD-204)

POST /cards/{id}/unblock. Hər ssenari yeni login ilə təmiz sandbox-da başlayır.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-CUB-001 FROZEN kart ACTIVE-ə qaytarılır, blockReason və blockedAt təmizlənir

tags: grad-204, regression, positive, tc-cub-001

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokdan çıxar
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "${cardId}" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Kartın statusu "ACTIVE" olmalıdır

## TC-CUB-002 ACTIVE kart üçün unblock 409 NOT_FROZEN qaytarır

tags: grad-204, regression, negative, tc-cub-002

* Test kartı yarat
* Kartı blokdan çıxar
* Xəta cavabı olmalıdır status "409" code "NOT_FROZEN"
* Kartın statusu "ACTIVE" olmalıdır

## TC-CUB-003 LOST / STOLEN ilə bloklanmış kart açılmır (409 PERMANENTLY_BLOCKED)

tags: grad-204, regression, negative, tc-cub-003

* Test kartı yarat
* Kartı blokla səbəb "LOST"
* Status kodunun "200" olmalıdır
* Kartı blokdan çıxar
* Xəta cavabı olmalıdır status "409" code "PERMANENTLY_BLOCKED"
* Kartın statusu "BLOCKED" olmalıdır
* Test kartı yarat
* Kartı blokla səbəb "STOLEN"
* Status kodunun "200" olmalıdır
* Kartı blokdan çıxar
* Xəta cavabı olmalıdır status "409" code "PERMANENTLY_BLOCKED"

## TC-CUB-004 Dondur, aç, yenidən dondur dövrü işləyir

tags: grad-204, regression, positive, tc-cub-004

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Kartı blokdan çıxar
* Status kodunun "200" olmalıdır
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Kartın statusu "FROZEN" olmalıdır

## TC-CUB-005 Mövcud olmayan və ya başqasının kartı üçün 404 NOT_FOUND

tags: grad-204, regression, negative, tc-cub-005

* "cardId" deyişenine "vcd_nonexist" deyerini ver
* Kartı blokdan çıxar
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"
* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
* Kartı blokdan çıxar
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-CUB-006 Token yoxdur və ya saxtadır — 401

tags: grad-204, regression, negative, tc-cub-006

* Test kartı yarat
* Kartı blokla səbəb "TEMPORARY"
* Status kodunun "200" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${cardId}/unblock"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/cards/${cardId}/unblock"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Kartın statusu "FROZEN" olmalıdır