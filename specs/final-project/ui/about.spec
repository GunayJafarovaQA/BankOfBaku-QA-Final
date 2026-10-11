# UI: Bank haqqında, Kampaniyalar, Biznes (UI-ABT, UI-CMP, UI-BIZ)

## UI-ABT-007 Bank haqqında səhifəsi açılır
tags: ui, about, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/bank-haqqinda"
* "6" saniye gözle
* JavaScript icra et "if(document.title.indexOf('Bank haqqında')<0) throw new Error('Başlıq səhv: '+document.title)"
* JavaScript icra et "if(document.body.innerText.length<800) throw new Error('Məzmun boşdur')"
* Brauzeri bağla

## UI-CMP-006 Kampaniyalar səhifəsi açılır
tags: ui, campaigns, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kampaniyalar"
* "6" saniye gözle
* JavaScript icra et "if(document.title.indexOf('Kampaniyalar')<0) throw new Error('Başlıq səhv: '+document.title)"
* JavaScript icra et "var h=[].slice.call(document.querySelectorAll('h2')).map(function(e){return e.innerText.trim()});if(h.indexOf('Kampaniyalar')<0) throw new Error('Kampaniyalar başlığı yoxdur')"
* Brauzeri bağla

## UI-CMP-007 Kredit kampaniyaları səhifəsində üç kampaniya var
tags: ui, campaigns

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/kreditler/kampaniyalar"
* "6" saniye gözle
* JavaScript icra et "var t=document.body.innerText;if(t.indexOf('Maaşa özəl kredit')<0||t.indexOf('Kreditini bizə gətir')<0||t.indexOf('KOMİSSİYASIZ kredit')<0) throw new Error('Kampaniya çatışmır')"
* Brauzeri bağla

## UI-BIZ-005 Biznes bölməsi açılır
tags: ui, business

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az/biznes"
* "6" saniye gözle
* URL "/az/biznes" içermelidir
* JavaScript icra et "if(document.body.innerText.length<800) throw new Error('Məzmun boşdur')"
* Brauzeri bağla
