# UI: Səhifə başlıqları (UI-SEO)

Hər səhifənin brauzer başlığı (title) unikal olmalıdır.

## UI-PRF-005 Debet və kredit kartları səhifələrinin başlığı fərqli olmalıdır (BUG-017)
tags: ui, seo, known-bug

* "chrome" brauzeri aç ve keçid et "/az/kartlar/debet"
* "5" saniye gözle
* JavaScript icra et "sessionStorage.setItem('t1',document.title)"
* "/az/kartlar/kredit-kartlari" adresine keçid et
* "5" saniye gözle
* JavaScript icra et "var a=sessionStorage.getItem('t1'),b=document.title;if(a===b) throw new Error('BUG-017: iki fərqli səhifənin başlığı eynidir: '+b)"
* Brauzeri bağla

## UI-PRF-006 Nağd pul və ipoteka kreditləri səhifələrinin başlığı fərqli olmalıdır (BUG-017)
tags: ui, seo, known-bug

* "chrome" brauzeri aç ve keçid et "/az/kreditler/nagd-pul-krediti"
* "5" saniye gözle
* JavaScript icra et "sessionStorage.setItem('t1',document.title)"
* "/az/kreditler/ipoteka-krediti" adresine keçid et
* "5" saniye gözle
* JavaScript icra et "var a=sessionStorage.getItem('t1'),b=document.title;if(a===b) throw new Error('BUG-017: iki fərqli səhifənin başlığı eynidir: '+b)"
* Brauzeri bağla

## UI-PRF-007 Digər xidmətlər alt səhifələrinin başlığı fərqli olmalıdır (BUG-017)
tags: ui, seo, known-bug

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/kart-emeliyyatlari/3d-secure"
* "5" saniye gözle
* JavaScript icra et "sessionStorage.setItem('t1',document.title)"
* "/az/diger-xidmetler/kart-emeliyyatlari/pin-change" adresine keçid et
* "5" saniye gözle
* JavaScript icra et "var a=sessionStorage.getItem('t1'),b=document.title;if(a===b) throw new Error('BUG-017: iki fərqli səhifənin başlığı eynidir: '+b)"
* Brauzeri bağla
