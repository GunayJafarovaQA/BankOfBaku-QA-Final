# UI: Kreditlər (UI-LON)

Yalnız oxuma yoxlamaları. Müraciət formaları açılmır və göndərilmir.

## UI-LON-008 Nağd pul kreditləri siyahısı yüklənir
tags: ui, loans, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-krediti"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('a.btn-m.white').length;if(n<5) throw new Error('Kredit sayı az: '+n)"
* Brauzeri bağla

## UI-LON-009 Kreditlər bölməsi nağd pul kreditinə yönləndirir
tags: ui, loans

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* URL "/az/kreditler/nagd-pul-krediti" içermelidir
* Brauzeri bağla

## UI-LON-010 Kreditin ətraflı səhifəsi açılır
tags: ui, loans

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-krediti"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* "Ətraflı Düyməsi" elementine JavaScript ile klik et
* "4" saniye gözle
* URL "/az/kreditler/nagd-pul-krediti/" içermelidir
* JavaScript icra et "if(document.body.innerText.length<500) throw new Error('Detal səhifəsi boşdur')"
* Brauzeri bağla

## UI-LON-011 İpoteka krediti siyahısı yüklənir
tags: ui, loans

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/ipoteka-krediti"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('a.btn-m.white').length;if(n<3) throw new Error('İpoteka sayı az: '+n)"
* Brauzeri bağla

## UI-LON-012 Müraciət düymələri düzgün ünvana yönləndirir (basılmır)
tags: ui, loans

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-krediti"
* "Ətraflı Düyməsi" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var re=new RegExp('kredit[.]bankofbaku[.]com/az/');var l=[].slice.call(document.querySelectorAll('a.btn-m')).filter(function(a){return a.innerText.trim()==='Müraciət et'});if(l.length<5) throw new Error('Müraciət düyməsi az: '+l.length);l.forEach(function(a){if(!re.test(a.href)) throw new Error('Yanlış ünvan: '+a.href)})"
* Brauzeri bağla

## UI-LON-013 Səhv yazılmış ünvan (nagd-pul-kreditleri) düzgün səhifəyə yönləndirir
tags: ui, loans

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-kreditleri/133"
* "4" saniye gözle
* URL "/az/kreditler/nagd-pul-krediti/133" içermelidir
* Brauzeri bağla

## UI-LON-015 Latın sözlərdə kiril hərfi olmamalıdır: "Maks." (BUG-023)
tags: ui, loans, known-bug

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/nagd-pul-krediti/129"
* "4" saniye gözle
* JavaScript icra et "var t=document.body.innerText;var cyr=new RegExp('['+String.fromCharCode(1024)+'-'+String.fromCharCode(1279)+']');var lat=new RegExp('[A-Za-z]');var words=t.split(' ').join('~').split(String.fromCharCode(10)).join('~').split('~');var bad=words.filter(function(w){return cyr.test(w)&&lat.test(w)});if(bad.length>0) throw new Error('BUG-023: latın söz içində kiril hərfi: '+bad[0]+' ('+bad.length+' yer)')"
* Brauzeri bağla
