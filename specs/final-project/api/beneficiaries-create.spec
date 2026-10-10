# Saxlanmış alıcılar — alıcı əlavə etmək (GRAD-101)

POST /beneficiaries. Test case-lər: Final_Project_API_Test_Cases.xlsx (TC-BEN-xxx). Hər ssenari yeni login ilə
təmiz sandbox-da işləyir, ona görə ssenarilər bir-birinin datasından asılı deyil.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-BEN-001 Etibarlı məlumatlarla alıcının uğurla yaradılması

tags: grad-101, regression, positive, tc-ben-001

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB40060019440123456789" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Header "Location" deyerini "location" olaraq yadda saxla
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Json cavabında "id" deyeri "ben_.{8}" regex-ine uyğun olmalıdır
* "location" deyişeni "/beneficiaries/${benId}" olmalıdır
* Json cavabını cedvel ile yoxla

   |path      |value                               |
   |fullName  |Nigar Əliyeva                       |
   |iban      |AZ77AIIB40060019440123456789        |
   |ibanMasked|AZ77 **** **** **** **** 6789       |
   |currency  |AZN                                 |
   |nickname  |Anam                                |
   |createdAt |@regex:[0-9]{4}-[0-9]{2}-[0-9]{2}T.*|

## TC-BEN-002 Boşluqlu və kiçik hərfli IBAN normallaşdırılaraq saxlanır

tags: grad-101, regression, positive, tc-ben-002

* Alıcı yarat ad "Nigar Əliyeva" iban "az77 aiib 4006 0019 4401 2345 6789" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri "AZ77AIIB40060019440123456789" beraberdir
* Json cavabında "ibanMasked" deyeri "AZ77 **** **** **** **** 6789" beraberdir

## TC-BEN-003 nickname göndərilmədikdə cavabda null qaytarılır

tags: grad-101, regression, positive, tc-ben-003

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB40060019440123456789" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır

## TC-BEN-004 Yaradılmış alıcı siyahıda görünür (POST → GET)

tags: grad-101, regression, positive, tc-ben-004

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB40060019440123456789" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path               |value                        |
   |total              |1                            |
   |items[0].id        |${benId}                     |
   |items[0].fullName  |Nigar Əliyeva                |
   |items[0].iban      |AZ77AIIB40060019440123456789 |
   |items[0].ibanMasked|AZ77 **** **** **** **** 6789|
   |items[0].currency  |AZN                          |
   |items[0].nickname  |Anam                         |

## TC-BEN-005 Bir neçə sahə eyni anda səhv olduqda hər səhv sahə details-də göstərilir

tags: grad-101, regression, negative, tc-ben-005

* Alıcı yarat ad "A1" iban "INVALID" valyuta "GBP"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details[0].message" deyeri boş olmamalıdır
* Json cavabında "details[1].message" deyeri boş olmamalıdır
* Json cavabında "details[2].message" deyeri boş olmamalıdır
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-006 Boş obyekt göndərildikdə məcburi sahələr üçün xəta qaytarılır

tags: grad-101, regression, negative, tc-ben-006

* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Add body as text "{}"
* Post request and display respons
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır

## TC-BEN-007 fullName alt sərhədi: trim-dən sonra 1 simvol rədd, 2 simvol qəbul

tags: grad-101, regression, boundary, tc-ben-007

(a) 1 simvol
* Alıcı yarat ad "A" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"
(b) boşluqlarla, trim-dən sonra 1 simvol
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Add body as file resource "ben-name-spaces.json"
* Post request and display respons
* Validasiya xətası olmalıdır sahə "fullName"
(c) 2 simvol
* Alıcı yarat ad "Li" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Li" beraberdir

## TC-BEN-008 fullName üst sərhədi: 50 simvol qəbul, 51 simvol rədd

tags: grad-101, regression, boundary, tc-ben-008

* Alıcı yarat ad "NigarNigarNigarNigarNigarNigarNigarNigarNigarNigar" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "NigarNigarNigarNigarNigarNigarNigarNigarNigarNigar" beraberdir
* Alıcı yarat ad "NigarNigarNigarNigarNigarNigarNigarNigarNigarNigara" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"

## TC-BEN-009 fullName etibarsız formatda olduqda rədd edilir

tags: grad-101, regression, negative, tc-ben-009

* Alıcı yarat ad "---" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"
* Alıcı yarat ad "Ali2" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"
* Alıcı yarat ad "Ali@" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"
* Alıcı yarat ad "-Ali" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "fullName"
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-010 fullName-də Azərbaycan hərfləri, defis və apostrof qəbul olunur

tags: grad-101, regression, positive, tc-ben-010

* Alıcı yarat ad "Əli-Vəli Məmmədov" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "Əli-Vəli Məmmədov" beraberdir
* Alıcı yarat ad "O'Neil Ümid" iban "AZ56AIIB40060019440000000002" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "fullName" deyeri "O'Neil Ümid" beraberdir

## TC-BEN-011 IBAN formatı səhv olduqda rədd edilir

tags: grad-101, regression, negative, tc-ben-011

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB4006001944012345678" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB400600194401234567890" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "TR77AIIB40060019440123456789" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "AZXXAIIB40060019440123456789" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77A1IB40060019440123456789" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ77AIIB4006001944012345678@" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcı yarat ad "Nigar Əliyeva" iban "" valyuta "AZN"
* Validasiya xətası olmalıdır sahə "iban"
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-012 currency üçün icazəli dəyərlər (AZN, USD, EUR) qəbul olunur

tags: grad-101, regression, positive, tc-ben-012

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "AZN" beraberdir
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ56AIIB40060019440000000002" valyuta "USD"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ29AIIB40060019440000000003" valyuta "EUR"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "EUR" beraberdir

## TC-BEN-013 currency icazəli dəyər olmadıqda rədd edilir

tags: grad-101, regression, negative, tc-ben-013

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "GBP"
* Validasiya xətası olmalıdır sahə "currency"
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta ""
* Validasiya xətası olmalıdır sahə "currency"
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-014 nickname sərhədləri: 1 və 20 simvol qəbul, 21 simvol rədd

tags: grad-101, regression, boundary, tc-ben-014

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "A"
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" deyeri "A" beraberdir
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ56AIIB40060019440000000002" valyuta "AZN" ləqəb "BBBBBBBBBBBBBBBBBBBB"
* Status kodunun "201" olmalıdır
* Json cavabında "nickname" deyeri "BBBBBBBBBBBBBBBBBBBB" beraberdir
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ29AIIB40060019440000000003" valyuta "AZN" ləqəb "CCCCCCCCCCCCCCCCCCCCC"
* Validasiya xətası olmalıdır sahə "nickname"
* Alıcılar siyahısında total "2" olmalıdır

## TC-BEN-016 Eyni IBAN ikinci dəfə əlavə edildikdə rədd edilir

tags: grad-101, regression, negative, tc-ben-016

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Anam"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "Ana"
* Xəta cavabı olmalıdır status "409" code "BENEFICIARY_EXISTS"
* Alıcılar siyahısında total "1" olmalıdır

## TC-BEN-018 Eyni ləqəb böyük-kiçik hərf fərqi olmadan təkrar edildikdə rədd edilir

tags: grad-101, regression, negative, tc-ben-018

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "anam"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Aygün Həsənova" iban "AZ56AIIB40060019440000000002" valyuta "AZN" ləqəb "ANAM"
* Xəta cavabı olmalıdır status "409" code "NICKNAME_TAKEN"
* Alıcılar siyahısında total "1" olmalıdır

## TC-BEN-019 İstifadəçi öz hesabının IBAN-ını alıcı kimi əlavə edə bilmir

tags: grad-101, regression, negative, tc-ben-019

* Alıcı yarat ad "Test Sahib" iban "AZ29NABZ00000000137010002855" valyuta "AZN"
* Xəta cavabı olmalıdır status "422" code "OWN_ACCOUNT"
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-020 Alıcı limiti: 10-cu alıcı qəbul olunur, 11-ci rədd edilir

tags: grad-101, regression, boundary, tc-ben-020

* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ56AIIB40060019440000000002" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ29AIIB40060019440000000003" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ02AIIB40060019440000000004" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ72AIIB40060019440000000005" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ45AIIB40060019440000000006" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ18AIIB40060019440000000007" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ88AIIB40060019440000000008" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ61AIIB40060019440000000009" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ34AIIB40060019440000000010" valyuta "AZN"
* Status kodunun "201" olmalıdır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ07AIIB40060019440000000011" valyuta "AZN"
* Xəta cavabı olmalıdır status "422" code "LIMIT_REACHED"
* Json cavabında "limit" deyeri "10" beraberdir
* Alıcılar siyahısında total "10" olmalıdır

## TC-BEN-021 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-101, regression, negative, tc-ben-021

(a) Authorization header göndərilmir
* "fullName" deyişenine "Nigar Əliyeva" deyerini ver
* "iban" deyişenine "AZ83AIIB40060019440000000001" deyerini ver
* "currency" deyişenine "AZN" deyerini ver
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add body as file resource "ben-create-no-nick.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
(b) saxta token
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Add body as file resource "ben-create-no-nick.json"
* Post request and display respons
* Status kodunun "401" olmalıdır
* Alıcılar siyahısında total "0" olmalıdır

## TC-BEN-022 Body etibarlı JSON obyekti olmadıqda INVALID_JSON qaytarılır

tags: grad-101, regression, negative, tc-ben-022

(a) bağlanmamış JSON
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Add body as file resource "ben-invalid-json-unclosed.json"
* Post request and display respons
* Xəta cavabı olmalıdır status "400" code "INVALID_JSON"
(b) obyekt deyil
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Authorization header-ine tokeni elave et
* Add body as file resource "ben-invalid-json-array.json"
* Post request and display respons
* Xəta cavabı olmalıdır status "400" code "INVALID_JSON"

## TC-BEN-023 Yoxlama ardıcıllığı: validasiya OWN_ACCOUNT-dan, BENEFICIARY_EXISTS NICKNAME_TAKEN-dan əvvəl işləyir

tags: grad-101, regression, negative, tc-ben-023

(a) öz IBAN-ı + səhv currency
* Alıcı yarat ad "Test Sahib" iban "AZ29NABZ00000000137010002855" valyuta "GBP"
* Validasiya xətası olmalıdır sahə "currency"
(b0) alıcı yaradılır
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "anam"
* Status kodunun "201" olmalıdır
(b) IBAN və ləqəb ikisi də dublikat
* Alıcı yarat ad "Nigar Əliyeva" iban "AZ83AIIB40060019440000000001" valyuta "AZN" ləqəb "ANAM"
* Xəta cavabı olmalıdır status "409" code "BENEFICIARY_EXISTS"