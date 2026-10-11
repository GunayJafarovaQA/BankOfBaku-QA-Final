# UI: Ana səhifə (UI-HOM)

Yalnız oxuma yoxlamaları. Heç bir forma doldurulmur.

## UI-HOM-007 Ana səhifə yüklənir
tags: ui, home, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "if(document.title.indexOf('Bank of Baku')<0) throw new Error('Başlıq səhv: '+document.title)"
* JavaScript icra et "if(document.body.innerText.length<500) throw new Error('Səhifə məzmunu boşdur')"
* Brauzeri bağla

## UI-HOM-008 Əsas menyu bölmələrinə linklər mövcuddur
tags: ui, home

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "var need=['/az/kartlar','/az/kreditler','/az/emanetler','/az/pul-kocurmeleri','/az/onlayn-xidmetler','/az/diger-xidmetler','/az/bank-haqqinda','/az/biznes'];var hs=[].slice.call(document.querySelectorAll('a[href]')).map(function(a){return a.getAttribute('href')});var miss=need.filter(function(n){return hs.indexOf(n)<0});if(miss.length>0) throw new Error('Menyuda link yoxdur: '+miss.join(', '))"
* Brauzeri bağla

## UI-HOM-009 Banner slayderi mövcuddur
tags: ui, home

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('swiper-slide').length;if(n<1) throw new Error('Slayd tapılmadı')"
* Brauzeri bağla

## UI-HOM-010 Footer-də sosial şəbəkə linkləri var
tags: ui, home

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "var need=['facebook.com','x.com','linkedin.com','t.me','wa.me','youtube.com'];var hs=[].slice.call(document.querySelectorAll('footer a[href]')).map(function(a){return a.getAttribute('href')}).join(' ');var miss=need.filter(function(n){return hs.indexOf(n)<0});if(miss.length>0) throw new Error('Footer-də yoxdur: '+miss.join(', '))"
* Brauzeri bağla

## UI-HOM-011 Footer-də daxili səhifə linkləri var
tags: ui, home

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "var need=['/az/bank-haqqinda','/az/xeberler','/az/teklif-ve-iradlar','/az/diger-xidmetler/tez-tez-verilen-suallar'];var hs=[].slice.call(document.querySelectorAll('footer a[href]')).map(function(a){return a.getAttribute('href')});var miss=need.filter(function(n){return hs.indexOf(n)<0});if(miss.length>0) throw new Error('Footer-də yoxdur: '+miss.join(', '))"
* Brauzeri bağla

## UI-HOM-012 Ana səhifədə son xəbərlər göstərilir
tags: ui, home

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* "6" saniye gözle
* JavaScript icra et "var n=[].slice.call(document.querySelectorAll('a[href]')).filter(function(a){return a.getAttribute('href').indexOf('/az/xeberler/')===0}).length;if(n<3) throw new Error('Xəbər sayı az: '+n)"
* Brauzeri bağla
