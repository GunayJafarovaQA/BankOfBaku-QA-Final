# GRAD-301 Təchizatçı kataloqu

## TC-BLR-001 Parametrsiz sorğu: 6 təchizatçı, hər birində format, aralıq və komissiya sahələri

tags: grad-301, regression, positive, tc-blr-001

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Initalize request specification
* Add Endpoint "/billers"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabını cedvel ile yoxla

   |path                      |value   |
   |items[0].subscriberPattern|@notNull|
   |items[0].minAmount        |@notNull|
   |items[0].maxAmount        |@notNull|
   |items[0].fee              |@notNull|

## TC-BLR-002 category=MOBILE yalnız Azercell və Bakcell qaytarır

tags: grad-301, regression, positive, tc-blr-002

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Initalize request specification
* Add Endpoint "/billers?category=MOBILE"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.category" siyahısındakı bütün deyerler "MOBILE" olmalıdır

## TC-BLR-003 category=INTERNET və UTILITY hər biri 2 təchizatçı qaytarır

tags: grad-301, regression, positive, tc-blr-003

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Initalize request specification
* Add Endpoint "/billers?category=INTERNET"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.category" siyahısındakı bütün deyerler "INTERNET" olmalıdır
* Initalize request specification
* Add Endpoint "/billers?category=UTILITY"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items.category" siyahısındakı bütün deyerler "UTILITY" olmalıdır
## TC-BLR-004 category=GAS (icazəsiz dəyər) 400 VALIDATION_ERROR qaytarır

tags: grad-301, regression, negative, tc-blr-004

* Yeni təmiz sandbox ilə user1 kimi daxil ol
* Initalize request specification
* Add Endpoint "/billers?category=GAS"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Validasiya xətası olmalıdır sahə "category"

## TC-BLR-005 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-301, regression, negative, tc-blr-005

* Initalize request specification
* Add Endpoint "/billers"
* Get request and display respons
* Status kodunun "401" olmalıdır
* Initalize request specification
* Add Endpoint "/billers"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Get request and display respons
* Status kodunun "401" olmalıdır