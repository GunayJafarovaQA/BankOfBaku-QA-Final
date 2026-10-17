# UI: Valyuta konvertoru (UI-FX)

Formalar göndərilmir. Yalnız hesablama və validasiya yoxlanır.

## UI-FX-004 AZN → USD (Nağd) hesablaması düzgündür
tags: ui, converter, smoke

* "chrome" brauzeri aç ve keçid et "/az"
* "Konvertor Satış Məbləği" elementine scroll et
* "Konvertor Satış Məbləği" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* "Konvertor Satış Məbləği" elementini temizle
* "Konvertor Satış Məbləği" elementine "100" yaz
* "Konvertor Nəticə" input deyeri "58.82" olmalıdır
* Brauzeri bağla

## UI-FX-005 Konvertor mənfi məbləği rədd etməlidir (BUG-014)
tags: ui, converter, known-bug

* "chrome" brauzeri aç ve keçid et "/az"
* "Konvertor Satış Məbləği" elementine scroll et
* "Konvertor Satış Məbləği" görsensin deye maksimum "15" saniye gözle
* "Konvertor Satış Məbləği" elementini temizle
* "Konvertor Satış Məbləği" elementine "-100" yaz
* "2" saniye gözle
* JavaScript icra et "var v=parseFloat(document.querySelector('.convertor input[name=converted]').value);if(v<0) throw new Error('BUG-014: mənfi məbləğ üçün nəticə '+v)"
* Brauzeri bağla
