# UI: Əmanətlər (UI-DEP)

Əmanət kalkulyatoru yoxlamaları. Formalar göndərilmir.

Qeyd: səhifə açılandan sonra komponentin hazır olması üçün 3 saniyə gözlənilir. Kalkulyator sahəni
təmizləyən kimi ilkin dəyəri (məbləğ 100, müddət 1) geri qaytarır; buna görə normal testlərdə dəyər
təmizlənmir, ilkin dəyərin üstünə əlavə olunur (100 + "00" = 10000, 1 + "2" = 12, 1 + "8" = 18).

## UI-DEP-007 Dinamik əmanət: ilkin vəziyyət və hesablama
tags: ui, deposits, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/dinamik-emanet"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" input deyeri "100" olmalıdır
* "Müddət Input" input deyeri "1" olmalıdır
* "Aylıq Ödəniş" elementinin metni "100.58" olmalıdır
* Brauzeri bağla

## UI-DEP-008 Dinamik əmanət: 10000 AZN, 12 ay
tags: ui, deposits

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/dinamik-emanet"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" elementine "00" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Müddət Input" elementine "2" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Məbləğ Input" input deyeri "10000" olmalıdır
* "Müddət Input" input deyeri "12" olmalıdır
* "Aylıq Ödəniş" elementinin metni "10950.00" olmalıdır
* Brauzeri bağla

## UI-DEP-009 Dinamik əmanət: 10000 AZN, 18 ay
tags: ui, deposits

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/dinamik-emanet"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" elementine "00" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Müddət Input" elementine "8" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Müddət Input" input deyeri "18" olmalıdır
* "Aylıq Ödəniş" elementinin metni "11462.50" olmalıdır
* Brauzeri bağla

## UI-DEP-010 Digital Depozit: ilkin vəziyyət və hesablama
tags: ui, deposits

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/digital-depozit"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" input deyeri "100" olmalıdır
* "Aylıq Ödəniş" elementinin metni "100.60" olmalıdır
* Brauzeri bağla

## UI-DEP-011 Maksimumdan böyük müddət rədd edilməli və ya xəta göstərilməlidir (BUG-019)
tags: ui, deposits, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/dinamik-emanet"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Müddət Input" elementini temizle
* "1" saniye gözle
* "Müddət Input" elementine "37" yaz ve Tab düymesine bas
* "3" saniye gözle
* JavaScript icra et "var m=parseInt(document.querySelector('input.range_input_month').value);var e=document.querySelector('.calculator__container [class*=error],.calculator__container [class*=warn]');if(m>36&&!e) throw new Error('BUG-019: 36 aydan böyük müddət ('+m+') qəbul edildi, xəta mesajı yoxdur')"
* Brauzeri bağla

## UI-DEP-012 Maksimumdan çox məbləğ rədd edilməli və ya xəta göstərilməlidir (BUG-018)
tags: ui, deposits, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/dinamik-emanet"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" elementini temizle
* "1" saniye gözle
* "Məbləğ Input" elementine "10000001" yaz ve Tab düymesine bas
* "3" saniye gözle
* JavaScript icra et "var v=parseFloat(document.querySelector('input.range_input').value);var e=document.querySelector('.calculator__container [class*=error],.calculator__container [class*=warn]');if(v>10000000&&!e) throw new Error('BUG-018: maksimumdan çox məbləğ ('+v+') qəbul edildi, xəta mesajı yoxdur')"
* Brauzeri bağla

## UI-DEP-013 Digital Depozit: 10000 AZN, 12 ay
tags: ui, deposits

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/emanetler/digital-depozit"
* "Məbləğ Input" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* "Məbləğ Input" elementine "00" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Müddət Input" elementine "2" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Məbləğ Input" input deyeri "10000" olmalıdır
* "Aylıq Ödəniş" elementinin metni "10975.00" olmalıdır
* Brauzeri bağla
