# UI: Naviqasiya (UI-NAV)

## UI-NAV-001 Əsas menyu elementləri və keçid ünvanları
tags: ui, navigation, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Menyu Biznes" elementinin "href" atributunda "/az/biznes" olmalıdır
* "Menyu Bank haqqında" elementinin "href" atributunda "/az/bank-haqqinda" olmalıdır
* "Menyu Kartlar" elementinin "href" atributunda "/az/kartlar" olmalıdır
* "Menyu Kreditlər" elementinin "href" atributunda "/az/kreditler" olmalıdır
* "Menyu Əmanətlər" elementinin "href" atributunda "/az/emanetler" olmalıdır
* "Menyu Pul köçürmələri" elementinin "href" atributunda "/az/pul-kocurmeleri" olmalıdır
* "Menyu Onlayn xidmətlər" elementinin "href" atributunda "/az/onlayn-xidmetler" olmalıdır
* "Menyu Digər xidmətlər" elementinin "href" atributunda "/az/diger-xidmetler" olmalıdır
* Brauzeri bağla

## UI-NAV-002 Kartlar bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kartlar" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/kartlar" içermelidir
* Brauzeri bağla

## UI-NAV-003 Kreditlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kreditlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Kreditlər" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/kreditler" içermelidir
* Brauzeri bağla

## UI-NAV-004 Əmanətlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Əmanətlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Əmanətlər" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/emanetler" içermelidir
* Brauzeri bağla

## UI-NAV-005 Pul köçürmələri bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Pul köçürmələri" görsensin deye maksimum "15" saniye gözle
* "Menyu Pul köçürmələri" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/pul-kocurmeleri" içermelidir
* Brauzeri bağla

## UI-NAV-006 Digər xidmətlər bölməsinə keçid
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Digər xidmətlər" görsensin deye maksimum "15" saniye gözle
* "Menyu Digər xidmətlər" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/diger-xidmetler" içermelidir
* Brauzeri bağla

## UI-NAV-007 Logo ilə ana səhifəyə qayıtmaq
tags: ui, navigation

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kartlar/debet"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Logo" elementine JavaScript ile klik et
* "2" saniye gözle
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

## UI-NAV-009 Kartlar menyusundan sonra Geri düyməsi ana səhifəyə qaytarmalıdır (BUG-012)
tags: ui, navigation, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Menyu Kartlar" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" elementine JavaScript ile klik et
* "2" saniye gözle
* URL "/az/kartlar" içermelidir
* Evvelki sehifeye qayıt
* "2" saniye gözle
* URL "https://www.bankofbaku.com/az" olmalıdır
* "Menyu Kartlar" görsensin deye maksimum "15" saniye gözle
* Brauzeri bağla

## UI-NAV-010 Olmayan ünvan 404 səhifəsi göstərməlidir, bağlantı vaxtı bitməməlidir (BUG-011)
tags: ui, navigation, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/yoxdur-test-sehife"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "Menyu Kartlar" görünür olmalıdır
* Brauzeri bağla


## UI-NAV-011 Ana səhifədəki daxili linklər dil prefiksi (/az) daşımalıdır (BUG-013)
tags: ui, navigation, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Logo" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* JavaScript icra et "var bad=[].slice.call(document.querySelectorAll('a[href]')).filter(function(a){var u=new URL(a.href,location.href);return u.hostname==='www.bankofbaku.com'&&!/^\/(az|en|ru)(\/|$)/.test(u.pathname)}).map(function(a){return a.getAttribute('href')});if(bad.length>0) throw new Error('BUG-013: dil prefiksi olmayan link sayı '+bad.length+', məsələn '+bad[0])"
* Brauzeri bağla
