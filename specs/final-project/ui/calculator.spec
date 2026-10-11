# UI: Kredit kalkulyatoru (UI-CAL)

Test mühiti: https://www.bankofbaku.com/az — formalar göndərilmir, yalnız hesablama və validasiya yoxlanır.

## UI-CAL-001 İlkin vəziyyət: minimum dəyərlər və hesablama
tags: ui, calculator, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Göstərici" elementin içinde "500" yazısı var
* "Müddət Göstərici" elementin içinde "3" yazısı var
* "Aylıq Ödəniş" elementinin metni "169.70" olmalıdır
* "Ümumi Məbləğ" elementinin metni "509.11" olmalıdır
* Brauzeri bağla

## UI-CAL-002 Düzgün məbləğ və müddət ilə hesablama
tags: ui, calculator, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "8000" yaz ve Tab düymesine bas
* "Müddət Input" elementini temizle
* "Müddət Input" elementine "12" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Məbləğ Input" input deyeri "8000" olmalıdır
* "Müddət Input" input deyeri "12" olmalıdır
* "Aylıq Ödəniş" elementinin metni "706.68" olmalıdır
* "Ümumi Məbləğ" elementinin metni "8480.16" olmalıdır
* Brauzeri bağla

## UI-CAL-003 Minimum sərhəd: 500 AZN / 3 ay qəbul olunur
tags: ui, calculator

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "500" yaz ve Tab düymesine bas
* "Müddət Input" elementini temizle
* "Müddət Input" elementine "3" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Aylıq Ödəniş" elementinin metni "169.70" olmalıdır
* Brauzeri bağla

## UI-CAL-004 Minimumdan aşağı məbləğ (499) rədd edilməlidir (BUG-003)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "499" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Kalkulyator Xəta Mesajı" görünür olmalıdır
* Brauzeri bağla

## UI-CAL-005 Sıfır məbləğ rədd edilməlidir (BUG-003)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "0" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Kalkulyator Xəta Mesajı" görünür olmalıdır
* Brauzeri bağla

## UI-CAL-006 Maksimumdan yuxarı məbləğ (80001) rədd edilməlidir (BUG-001)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "80001" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Kalkulyator Xəta Mesajı" görünür olmalıdır
* Brauzeri bağla

## UI-CAL-007 Maksimumdan yuxarı müddət (60) rədd edilməlidir (BUG-002)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Müddət Input" görsensin deye maksimum "15" saniye gözle
* "Müddət Input" elementini temizle
* "Müddət Input" elementine "60" yaz ve Tab düymesine bas
* "1" saniye gözle
* "Kalkulyator Xəta Mesajı" görünür olmalıdır
* Brauzeri bağla

## UI-CAL-008 Kredit növü dəyişəndə seçim yenilənir
tags: ui, calculator

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Kredit Növü Seçimi" görsensin deye maksimum "15" saniye gözle
* "Kredit Növü Seçimi" elementine klik et
* "Kredit Növü Seçimləri" siyahısında "Lombard krediti" metnli elemente klik et
* "Kredit Növü Seçilmiş" elementin içinde "Lombard krediti" yazısı var
* Brauzeri bağla

## UI-CAL-009 Kalkulyatorun defolt kredit növü neytral olmalıdır (BUG-007)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Kredit Növü Seçilmiş" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "if(/Səhiyyə/.test(document.querySelector('.calculator__container .select_box .selected').innerText)) throw new Error('BUG-007: defolt növ özəl kredit növüdür')"
* Brauzeri bağla

## UI-CAL-010 Cəmi ödəniş = aylıq ödəniş × müddət (BUG-005)
tags: ui, calculator, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "1000" yaz ve Tab düymesine bas
* "Müddət Input" elementini temizle
* "Müddət Input" elementine "12" yaz ve Tab düymesine bas
* "1" saniye gözle
* JavaScript icra et "var m=parseFloat(document.querySelector('.calculator__container .payment').innerText),t=parseFloat(document.querySelector('.calculator__container .total-sum').innerText);if(Math.abs(m*12-t)>0.011) throw new Error('BUG-005: '+m+' x 12 = '+(m*12).toFixed(2)+', göstərilən '+t)"
* Brauzeri bağla
