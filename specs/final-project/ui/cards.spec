# UI: Kartlar (UI-CRD)

Yalnız oxuma yoxlamaları. "Müraciət et" düymələri basılmır, formalar göndərilmir.

## UI-CRD-007 Debet kartlar siyahısı yüklənir
tags: ui, cards, smoke

* "chrome" brauzeri aç ve keçid et "/az/kartlar/debet"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('a.btn-m.white').length;if(n<5) throw new Error('Debet kart sayı az: '+n)"
* "Xidmət Tab Aktiv" elementinin metni "Debet" olmalıdır
* Brauzeri bağla

## UI-CRD-008 Kredit kartları tabına keçid
tags: ui, cards

* "chrome" brauzeri aç ve keçid et "/az/kartlar/debet"
* "Kart Tab Kredit kartları" görsensin deye maksimum "20" saniye gözle
* "Kart Tab Kredit kartları" elementine JavaScript ile klik et
* "3" saniye gözle
* URL "/az/kartlar/kredit-kartlari" içermelidir
* "Xidmət Tab Aktiv" elementinin metni "Kredit kartları" olmalıdır
* JavaScript icra et "var n=document.querySelectorAll('a.btn-m.white').length;if(n<5) throw new Error('Kredit kart sayı az: '+n)"
* Brauzeri bağla

## UI-CRD-009 Debet kartın ətraflı səhifəsi açılır
tags: ui, cards

* "chrome" brauzeri aç ve keçid et "/az/kartlar/debet"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* "Ətraflı Düyməsi" elementine JavaScript ile klik et
* "4" saniye gözle
* URL "/az/kartlar/debet/" içermelidir
* JavaScript icra et "if(document.body.innerText.length<500) throw new Error('Detal səhifəsi boşdur')"
* Brauzeri bağla

## UI-CRD-010 Müraciət düymələri düzgün ünvana yönləndirir (basılmır)
tags: ui, cards

* "chrome" brauzeri aç ve keçid et "/az/kartlar/debet"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var re=new RegExp('kredit[.]bankofbaku[.]com/az/|/az/sorgular/');var l=[].slice.call(document.querySelectorAll('a.btn-m')).filter(function(a){return a.innerText.trim()!=='Daha ətraflı'});if(l.length<5) throw new Error('Müraciət düyməsi az: '+l.length);l.forEach(function(a){if(!re.test(a.href)) throw new Error('Yanlış ünvan: '+a.href)})"
* Brauzeri bağla
