# GRAD-303 Ödəniş tarixçəsi — filtr və səhifələmə

## TC-HST-001 Parametrsiz sorğu: page 1, limit 10, ən yeni ödəniş birinci

tags: grad-303, regression, positive, tc-hst-001

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu ""
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "3" beraberdir
* Json cavabında "items[0].amount" deyeri "20" beraberdir
* Json cavabında "items[2].amount" deyeri "10" beraberdir

## TC-HST-002 7 ödəniş, limit=3: səhifələr 3/3/1, totalPages 3

tags: grad-303, regression, boundary, tc-hst-002

* Tarixçə üçün 7 ödəniş göndər
* Tarixçəni al sorğu "?limit=3&page=1"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "3" olmalıdır
* Json cavabında "total" deyeri "7" beraberdir
* Json cavabında "totalPages" deyeri "3" beraberdir
* Json cavabında "items[0].amount" deyeri "7" beraberdir
* Tarixçəni al sorğu "?limit=3&page=3"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items[0].amount" deyeri "1" beraberdir

## TC-HST-003 Mövcud olmayan səhifə xəta yox, boş siyahı qaytarır

tags: grad-303, regression, boundary, tc-hst-003

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu "?limit=3&page=4"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
* Json cavabında "total" deyeri "3" beraberdir

## TC-HST-004 limit sərhədləri: 1 və 50 qəbul olunur

tags: grad-303, regression, boundary, tc-hst-004

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu "?limit=1"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "totalPages" deyeri "3" beraberdir
* Tarixçəni al sorğu "?limit=50"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "3" olmalıdır
* Json cavabında "limit" deyeri "50" beraberdir

## TC-HST-005 billerId=citynet yalnız CityNet ödənişlərini qaytarır, total uyğundur

tags: grad-303, regression, positive, tc-hst-005

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu "?billerId=citynet"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC-HST-006 from = to = bu gün: bugünkü bütün ödənişlər

tags: grad-303, regression, positive, tc-hst-006

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu "?from=${today}&to=${today}"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "3" beraberdir

## TC-HST-007 Gələcək tarix aralığı boş nəticə qaytarır

tags: grad-303, regression, positive, tc-hst-007

* Tarixçə üçün 3 ödəniş göndər
* Tarixçəni al sorğu "?from=2099-01-01&to=2099-12-31"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
## TC-HST-008 Yanlış limit/page dəyərləri rədd edilir

tags: grad-303, regression, negative, tc-hst-008

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Tarixçəni al sorğu "?limit=0"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"
* Tarixçəni al sorğu "?limit=51"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"
* Tarixçəni al sorğu "?page=0"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"
* Tarixçəni al sorğu "?page=-1"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"
* Tarixçəni al sorğu "?page=abc"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"

## TC-HST-009 Səhv tarix: mövcud olmayan tarix və from > to rədd edilir

tags: grad-303, regression, negative, tc-hst-009

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Tarixçəni al sorğu "?from=2026-13-01"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"
* Tarixçəni al sorğu "?from=2026-10-10&to=2026-10-01"
* Xəta cavabı olmalıdır status "400" code "VALIDATION_ERROR"

## TC-HST-010 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-303, regression, negative, tc-hst-010

* Initalize request specification
* Add Endpoint "/bill-payments"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/bill-payments"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Get request and display respons
* Status kodunun "401" olmalıdır