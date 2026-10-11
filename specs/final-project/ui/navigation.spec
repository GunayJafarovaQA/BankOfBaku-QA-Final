# UI: Naviqasiya (UI-NAV)

## UI-NAV-001 Əsas menyu elementləri və keçid ünvanları
tags: ui, navigation, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Menyu Biznes" elementinin "href" atributu "/az/biznes" olmalıdır
* "Menyu Bank haqqında" elementinin "href" atributu "/az/bank-haqqinda" olmalıdır
* "Menyu Kartlar" elementinin "href" atributu "/az/kartlar" olmalıdır
* "Menyu Kreditlər" elementinin "href" atributu "/az/kreditler" olmalıdır
* "Menyu Əmanətlər" elementinin "href" atributu "/az/emanetler" olmalıdır
* "Menyu Pul köçürmələri" elementinin "href" atributu "/az/pul-kocurmeleri" olmalıdır
* "Menyu Onlayn xidmətlər" elementinin "href" atributu "/az/onlayn-xidmetler" olmalıdır
* "Menyu Digər xidmətlər" elementinin "href" atributu "/az/diger-xidmetler" olmalıdır
* Brauzeri bağla

## UI-NAV-002 Kartlar bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kartlar" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/kartlar" içermelidir
* Brauzeri bağla

## UI-NAV-003 Kreditlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kreditlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Kreditlər" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/kreditler" içermelidir
* Brauzeri bağla

## UI-NAV-004 Əmanətlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Əmanətlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Əmanətlər" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/emanetler" içermelidir
* Brauzeri bağla

## UI-NAV-005 Pul köçürmələri bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Pul köçürmələri" görsensin deye maksimum "15" saniye gözle
* "Menyu Pul köçürmələri" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/pul-kocurmeleri" içermelidir
* Brauzeri bağla

## UI-NAV-006 Digər xidmətlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Digər xidmətlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Digər xidmətlər" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/diger-xidmetler" içermelidir
* Brauzeri bağla

## UI-NAV-007 Logo ilə ana səhifəyə qayıtmaq
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kartlar/debet"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Logo" elementine JavaScript ile klik et
* 2 saniye gözle
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* URL "/az" içermelidir
* Brauzeri bağla

## UI-NAV-008 Daxili səhifədə F5 yeniləmə (SPA deep link)
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-krediti"
* "Logo" görsensin deye maksimum "15" saniye gözle
* Sehifeni yenile
* "Logo" görsensin deye maksimum "15" saniye gözle
* URL "/az/kreditler/nagd-pul-krediti" içermelidir
* Brauzeri bağla

## UI-NAV-009 Geri düyməsi SPA-da düzgün işləyir
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kartlar" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" elementine JavaScript ile klik et
* 2 saniye gözle
* URL "/az/kartlar" içermelidir
* Evvelki sehifeye qayıt
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* Brauzeri bağla

## UI-NAV-010 Olmayan səhifə (404) menyunu saxlayır
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/yoxdur-test-sehife"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" görünür olmalıdır
* Brauzeri bağla
