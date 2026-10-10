# Təcrübə (sonra silinəcək)

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## EXP-1 query endpoint daxilində, 400
tags: exp

* Initalize request specification
* Add Endpoint "/beneficiaries?q=a"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## EXP-2 query parametr addımı ilə, 400
tags: exp2

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "a"
* Get request and display respons
* Status kodunun "400" olmalıdır

## EXP-3 GET, body və Content-Type ilə, 400
tags: exp3

* Initalize request specification
* Add Endpoint "/beneficiaries?q=a"
* Authorization header-ine tokeni elave et
* Add as a header "Content-Type" = "application/json"
* Add body as text "{}"
* Get request and display respons
* Status kodunun "400" olmalıdır