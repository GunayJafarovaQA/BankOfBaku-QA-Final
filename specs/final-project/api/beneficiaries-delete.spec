# Saxlanmış alıcılar — alıcını silmək (GRAD-103)

DELETE /beneficiaries/{id}. Test case-lər: Final_Project_API_Test_Cases.xlsx (TC-DEL-xxx). Hər ssenari yeni login ilə
təmiz sandbox-da başlayır.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-DEL-001 Mövcud alıcı silinir, 204 qaytarılır və siyahı boş qalır

tags: grad-103, regression, positive, tc-del-001

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Status kodunun "204" olmalıdır
* Alıcılar siyahısında total "0" olmalıdır

## TC-DEL-002 Silinmiş alıcı siyahıda görünmür, digər alıcı qalır, total 1 azalır

tags: grad-103, regression, positive, tc-del-002

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Alıcı yarat ad "Aygün Həsənova" iban "AZ56AIIB40060019440000000002" valyuta "USD" ləqəb "Dostum"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId2" olaraq yadda saxla
* Alıcılar siyahısında total "2" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Status kodunun "204" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |total            |1             |
   |items[0].id      |${benId2}     |
   |items[0].fullName|Aygün Həsənova|
   |items[0].nickname|Dostum        |

## TC-DEL-003 Silinmiş alıcını yenidən silmək 404 NOT_FOUND qaytarır

tags: grad-103, regression, negative, tc-del-003

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Status kodunun "204" olmalıdır
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-DEL-004 Mövcud olmayan id silinərkən 404 NOT_FOUND qaytarılır

tags: grad-103, regression, negative, tc-del-004

* Initalize request specification
* Add Endpoint "/beneficiaries/ben_nonexist"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-DEL-005 Başqa istifadəçinin alıcısı silinməyə çalışılanda 404 qaytarılır (403 yox)

tags: grad-103, regression, negative, tc-del-005

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* "/auth/login" ünvanına "login-user2.json" ile yeni sessiya açaraq login ol ve "token" tokenini yadda saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Xəta cavabı olmalıdır status "404" code "NOT_FOUND"

## TC-DEL-006 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-103, regression, negative, tc-del-006

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
(a) Authorization header göndərilmir
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Delete request and display response
* Status kodunun "401" olmalıdır
(b) saxta token
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Delete request and display response
* Status kodunun "401" olmalıdır
* Alıcılar siyahısında total "1" olmalıdır

## TC-DEL-007 Silinmiş alıcının IBAN və ləqəbi yenidən istifadə oluna bilər

tags: grad-103, regression, positive, tc-del-007

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Initalize request specification
* Add Endpoint "/beneficiaries/${benId}"
* Authorization header-ine tokeni elave et
* Delete request and display response
* Status kodunun "204" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ83AIIB40060019440000000001" beraberdir
* Json cavabında "nickname" deyeri "Anam" beraberdir
* Alıcılar siyahısında total "1" olmalıdır