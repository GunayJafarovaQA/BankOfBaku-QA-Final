# UI: Filiallar və ATM (UI-BRN)

## UI-BRN-001 Filiallar səhifəsi açılır, xəritə konteyneri və 3 tab görünür
tags: ui, branches, smoke

* "chrome" brauzeri aç ve keçid et "/az/xidmet-shebekeleri/filiallar"
* "Xəritə Konteyneri" görsensin deye maksimum "20" saniye gözle
* "Xidmət Tab Aktiv" elementinin metni "Filiallar" olmalıdır
* "Xidmət Tab Bankomatlar" elementinin "href" atributunda "/az/xidmet-shebekeleri/bankomatlar" olmalıdır
* "Xidmət Tab Terminallar" elementinin "href" atributunda "/az/xidmet-shebekeleri/odenish-terminallari" olmalıdır
* Brauzeri bağla

## UI-BRN-008 Bankomatlar tabına keçid
tags: ui, branches

* "chrome" brauzeri aç ve keçid et "/az/xidmet-shebekeleri/filiallar"
* "Xidmət Tab Bankomatlar" görsensin deye maksimum "20" saniye gözle
* "Xidmət Tab Bankomatlar" elementine JavaScript ile klik et
* URL "/az/xidmet-shebekeleri/bankomatlar" içermelidir
* "Xidmət Tab Aktiv" elementinin metni "Bankomatlar" olmalıdır
* "Xəritə Konteyneri" görsensin deye maksimum "20" saniye gözle
* Brauzeri bağla

## UI-BRN-009 Ödəniş terminalları tabına keçid
tags: ui, branches

* "chrome" brauzeri aç ve keçid et "/az/xidmet-shebekeleri/filiallar"
* "Xidmət Tab Terminallar" görsensin deye maksimum "20" saniye gözle
* "Xidmət Tab Terminallar" elementine JavaScript ile klik et
* URL "/az/xidmet-shebekeleri/odenish-terminallari" içermelidir
* "Xidmət Tab Aktiv" elementinin metni "Ödəniş terminalları" olmalıdır
* "Xəritə Konteyneri" görsensin deye maksimum "20" saniye gözle
* Brauzeri bağla

## UI-BRN-010 Bankomatlar səhifəsi birbaşa ünvanla açılır (F5 deep link)
tags: ui, branches

* "chrome" brauzeri aç ve keçid et "/az/xidmet-shebekeleri/bankomatlar"
* "Xəritə Konteyneri" görsensin deye maksimum "20" saniye gözle
* Sehifeni yenile
* "Xəritə Konteyneri" görsensin deye maksimum "20" saniye gözle
* "Xidmət Tab Aktiv" elementinin metni "Bankomatlar" olmalıdır
* Brauzeri bağla
