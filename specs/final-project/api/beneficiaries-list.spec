# Saxlanmış alıcılar — siyahı, axtarış, filtr, sıralama (GRAD-102)

GET /beneficiaries. Test case-lər: Final_Project_API_Test_Cases.xlsx (TC-LST-xxx). Hər ssenari yeni login ilə təmiz sandbox-da
başlayır və 5 test alıcısı yaradır. Yaranma sırası: Nigar, Aygün, Çinar, Əli, Zaur.

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-LST-001 Parametrsiz sorğuda total = items sayı, ən yeni alıcı birinci gəlir

tags: grad-102, regression, positive, tc-lst-001

* Axtarış üçün 5 test alıcısı yarat
* Alıcılar siyahısı sorğusunu hazırla
* Get request and display respons
* Status kodunun "200" olmalıdır
* Cavab "beneficiary-list.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "total" deyeri "5" beraberdir
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Zaur Zeynalov |
   |items[1].fullName|Əli Məmmədov  |
   |items[2].fullName|Çinar Quliyev |
   |items[3].fullName|Aygün Həsənova|
   |items[4].fullName|Nigar Əliyeva |

## TC-LST-002 sort=fullName&order=asc — adlar Azərbaycan əlifbası ilə düzülür

tags: grad-102, regression, positive, tc-lst-002

* Axtarış üçün 5 test alıcısı yarat
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "5" beraberdir
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Aygün Həsənova|
   |items[1].fullName|Çinar Quliyev |
   |items[2].fullName|Əli Məmmədov |
   |items[3].fullName|Nigar Əliyeva |
   |items[4].fullName|Zaur Zeynalov |

## TC-LST-003 Digər sort/order kombinasiyaları: fullName desc və createdAt asc

tags: grad-102, regression, positive, tc-lst-003

(a) fullName desc
* Axtarış üçün 5 test alıcısı yarat
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "desc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Zaur Zeynalov |
   |items[1].fullName|Nigar Əliyeva |
   |items[2].fullName|Əli Məmmədov |
   |items[3].fullName|Çinar Quliyev |
   |items[4].fullName|Aygün Həsənova|
(b) createdAt asc
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "sort" = "createdAt"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Nigar Əliyeva |
   |items[1].fullName|Aygün Həsənova|
   |items[2].fullName|Çinar Quliyev |
   |items[3].fullName|Əli Məmmədov |
   |items[4].fullName|Zaur Zeynalov |

## TC-LST-004 currency=USD filtri yalnız USD alıcıları qaytarır

tags: grad-102, regression, positive, tc-lst-004

* Axtarış üçün 5 test alıcısı yarat
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "currency" = "USD"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Zaur Zeynalov |
   |items[1].fullName|Aygün Həsənova|

## TC-LST-005 Axtarış böyük-kiçik hərfə və I / İ / ı fərqinə həssas deyil

tags: grad-102, regression, positive, tc-lst-005

* Axtarış üçün 5 test alıcısı yarat
(a) q=NİGAR
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "NİGAR"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir
(b) q=NIGAR (nöqtəsiz I)
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "NIGAR"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir
(c) q=nigar
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "nigar"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-LST-006 Axtarış həm fullName-in, həm də nickname-in hissəsi üzrə işləyir

tags: grad-102, regression, positive, tc-lst-006

* Axtarış üçün 5 test alıcısı yarat
(a) nickname-in hissəsi
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "dost"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Aygün Həsənova" beraberdir
* Json cavabında "items[0].nickname" deyeri "Dostum" beraberdir
(b) fullName-in hissəsi, bir neçə nəticə
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "liyev"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabını cedvel ile yoxla

   |path             |value         |
   |items[0].fullName|Çinar Quliyev |
   |items[1].fullName|Nigar Əliyeva |

## TC-LST-007 Parametrlər AND məntiqi ilə birləşir

tags: grad-102, regression, positive, tc-lst-007

* Axtarış üçün 5 test alıcısı yarat
(a) q + currency + sort + order (spesifikasiyadakı nümunə)
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "nig"
* Query parametri elave et "currency" = "AZN"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir
* Json cavabında "items[0].currency" deyeri "AZN" beraberdir
(b) q uyğun gəlir, currency uyğun gəlmir
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "nigar"
* Query parametri elave et "currency" = "USD"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-LST-008 Heç nə tapılmadıqda 200 və boş siyahı qaytarılır

tags: grad-102, regression, positive, tc-lst-008

* Axtarış üçün 5 test alıcısı yarat
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "zzzz"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC-LST-009 q sərhədi: 1 simvol rədd edilir, 2 simvol qəbul olunur

tags: grad-102, regression, boundary, tc-lst-009

* Axtarış üçün 5 test alıcısı yarat
(a) 1 simvol
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "a"
* Get request and display respons
* Validasiya xətası olmalıdır sahə "q"
(b) 2 simvol
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "q" = "ni"
* Get request and display respons
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items[0].fullName" deyeri "Nigar Əliyeva" beraberdir

## TC-LST-010 currency, sort və order üçün icazəsiz dəyərlər rədd edilir

tags: grad-102, regression, negative, tc-lst-010

(a) currency
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "currency" = "GBP"
* Get request and display respons
* Validasiya xətası olmalıdır sahə "currency"
(b) sort
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "sort" = "nickname"
* Get request and display respons
* Validasiya xətası olmalıdır sahə "sort"
(c) order
* Alıcılar siyahısı sorğusunu hazırla
* Query parametri elave et "order" = "up"
* Get request and display respons
* Validasiya xətası olmalıdır sahə "order"

## TC-LST-011 Token yoxdur və ya saxtadır — 401 qaytarılır

tags: grad-102, regression, negative, tc-lst-011

(a) Authorization header göndərilmir
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Get request and display respons
* Status kodunun "401" olmalıdır
(b) saxta token
* Initalize request specification
* Add Endpoint "/beneficiaries"
* Add as a header "Authorization" = "Bearer invalid.token.value"
* Get request and display respons
* Status kodunun "401" olmalıdır