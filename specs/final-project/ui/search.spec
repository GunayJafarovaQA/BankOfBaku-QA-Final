# UI: Sayt axtarışı (UI-SRC)

Axtarış nəticə səhifəsi: /az/axtar?q=...

## UI-SRC-001 Mövcud söz üçün nəticələr tapılır
tags: ui, search, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/axtar?q=kart"
* "Axtarış Nəticə Sayı" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* JavaScript icra et "if(parseInt(document.querySelector('.result span').innerText,10)<=0) throw new Error('kart üçün nəticə tapılmadı')"
* Brauzeri bağla

## UI-SRC-002 Böyük və kiçik hərflə axtarış eyni nəticə sayı verməlidir (BUG-015)
tags: ui, search, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/axtar?q=kredit"
* "Axtarış Nəticə Sayı" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* JavaScript icra et "sessionStorage.setItem('countLower',document.querySelector('.result span').innerText)"
* "https://www.bankofbaku.com/az/axtar?q=KRED%C4%B0T" adresine keçid et
* "Axtarış Nəticə Sayı" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* JavaScript icra et "var a=sessionStorage.getItem('countLower'),b=document.querySelector('.result span').innerText;if(a!==b) throw new Error('BUG-015: kredit='+a+' nəticə, KREDİT='+b+' nəticə')"
* Brauzeri bağla

## UI-SRC-003 Boş sorğu bütün nəticələri qaytarmamalıdır (BUG-016)
tags: ui, search, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/axtar?q="
* "Axtarış Nəticə Sayı" görsensin deye maksimum "15" saniye gözle
* "3" saniye gözle
* "Axtarış Nəticə Sayı" elementinin metni "0" olmalıdır
* Brauzeri bağla
