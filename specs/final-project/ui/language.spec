# UI: Dil davranışı (UI-LNG)

Sayt kök URL-də İngilis dilində açılır. Bütün testlər dili açıq şəkildə /az ilə başladır.

## UI-LNG-002 Birbaşa /az linki Azərbaycan dilində açılır
tags: ui, language, smoke

* "chrome" brauzeri aç ve keçid et "/az"
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* "Kalkulyator Başlıq" elementinin metni "Kredit Kalkulyatoru" olmalıdır
* JavaScript icra et "if(document.documentElement.lang!=='az') throw new Error('html lang az deyil: '+document.documentElement.lang)"
* URL "/az" içermelidir
* Brauzeri bağla

## UI-LNG-005 Dil menyusundan EN seçimi
tags: ui, language

* "chrome" brauzeri aç ve keçid et "/az"
* "Dil Menyusu" görsensin deye maksimum "15" saniye gözle
* "Dil Menyusu" elementine klik et
* "Dil EN" elementine JavaScript ile klik et
* "Kalkulyator Başlıq" elementin içinde "Loan Calculator" yazısı var
* URL "/en" içermelidir
* Brauzeri bağla

## UI-LNG-005b Dil menyusundan RU seçimi
tags: ui, language

* "chrome" brauzeri aç ve keçid et "/az"
* "Dil Menyusu" görsensin deye maksimum "15" saniye gözle
* "Dil Menyusu" elementine klik et
* "Dil RU" elementine JavaScript ile klik et
* URL "/ru" içermelidir
* Brauzeri bağla

## UI-LNG-003 /en linkində html lang İngilis dilindədir (BUG-008)
tags: ui, language, known-bug

* "chrome" brauzeri aç ve keçid et "/en"
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "if(document.documentElement.lang!=='en') throw new Error('BUG-008: /en səhifəsində html lang='+document.documentElement.lang)"
* Brauzeri bağla

## UI-LNG-003b /en linkində başlıq (title) İngilis dilindədir (BUG-009)
tags: ui, language, known-bug

* "chrome" brauzeri aç ve keçid et "/en"
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "if(/Sizə yaxın/.test(document.title)) throw new Error('BUG-009: /en səhifəsində başlıq Azərbaycan dilindədir: '+document.title)"
* Brauzeri bağla

## UI-LNG-008 Dil keçidindən sonra başlıq tərcümə açarı olmamalıdır (BUG-010)
tags: ui, language, known-bug

* "chrome" brauzeri aç ve keçid et "/az"
* "Dil Menyusu" görsensin deye maksimum "15" saniye gözle
* "Dil Menyusu" elementine klik et
* "Dil EN" elementine JavaScript ile klik et
* "Kalkulyator Başlıq" elementin içinde "Loan Calculator" yazısı var
* "2" saniye gözle
* JavaScript icra et "if(/site-title|pages[.]/.test(document.title)) throw new Error('BUG-010: başlıq tərcümə açarıdır: '+document.title)"
* Brauzeri bağla

## UI-LNG-006 Dil seçimi yenilədikdən sonra saxlanılır
tags: ui, language

* "chrome" brauzeri aç ve keçid et "/az"
* "Dil Menyusu" görsensin deye maksimum "15" saniye gözle
* "Dil Menyusu" elementine klik et
* "Dil EN" elementine JavaScript ile klik et
* "Kalkulyator Başlıq" elementin içinde "Loan Calculator" yazısı var
* Sehifeni yenile
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* "Kalkulyator Başlıq" elementin içinde "Loan Calculator" yazısı var
* Brauzeri bağla
