# UI: Pul köçürmələri (UI-TRF)

Yalnız oxuma yoxlamaları. Real köçürmə edilmir.

## UI-TRF-007 Pul köçürmələri bölməsi iki xidməti göstərir
tags: ui, transfers, smoke

* "chrome" brauzeri aç ve keçid et "/az/pul-kocurmeleri"
* "6" saniye gözle
* Sehife başlığında "Pul köçürmələri" olmalıdır
* JavaScript icra et "var t=document.body.innerText;if(t.indexOf('Western Union')<0||t.indexOf('UPT')<0) throw new Error('Xidmətlər göstərilmir')"
* Brauzeri bağla

## UI-TRF-008 Western Union səhifəsi açılır
tags: ui, transfers

* "chrome" brauzeri aç ve keçid et "/az/pul-kocurmeleri/western-union"
* "6" saniye gözle
* URL "/az/pul-kocurmeleri/western-union" içermelidir
* Sehife başlığında "Western Union" olmalıdır
* JavaScript icra et "if(document.body.innerText.length<800) throw new Error('Məzmun boşdur')"
* Brauzeri bağla

## UI-TRF-009 UPT TÖS səhifəsi açılır
tags: ui, transfers

* "chrome" brauzeri aç ve keçid et "/az/pul-kocurmeleri/upt-tos"
* "6" saniye gözle
* URL "/az/pul-kocurmeleri/upt-tos" içermelidir
* Sehife başlığında "UPT" olmalıdır
* JavaScript icra et "if(document.body.innerText.length<800) throw new Error('Məzmun boşdur')"
* Brauzeri bağla

## UI-TRF-010 Menyuda köçürmə xidmətlərinin linkləri var
tags: ui, transfers

* "chrome" brauzeri aç ve keçid et "/az"
* "6" saniye gözle
* JavaScript icra et "var hs=[].slice.call(document.querySelectorAll('a[href]')).map(function(a){return a.getAttribute('href')});if(hs.indexOf('/az/pul-kocurmeleri/western-union')<0||hs.indexOf('/az/pul-kocurmeleri/upt-tos')<0) throw new Error('Menyuda köçürmə linki yoxdur')"
* Brauzeri bağla
