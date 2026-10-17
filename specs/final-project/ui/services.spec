# UI: Onlayn və digər xidmətlər (UI-SRV)

Yalnız oxuma yoxlamaları. İnternet bankçılıq girişinə toxunulmur.

## UI-SRV-019 Onlayn xidmətlər bölməsi açılır
tags: ui, services, smoke

* "chrome" brauzeri aç ve keçid et "/az/onlayn-xidmetler"
* "6" saniye gözle
* Sehife başlığında "Onlayn xidmətlər" olmalıdır
* JavaScript icra et "if(document.body.innerText.length<800) throw new Error('Məzmun boşdur')"
* Brauzeri bağla

## UI-SRV-020 Dostbank mobil bankçılıq səhifəsi açılır
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/onlayn-xidmetler/dostbank-mobil-bankciliq"
* "6" saniye gözle
* Sehife başlığında "Dostbank" olmalıdır
* JavaScript icra et "if(document.body.innerText.length<1500) throw new Error('Məzmun az: '+document.body.innerText.length)"
* Brauzeri bağla

## UI-SRV-021 Digər xidmətlər bölməsi açılır
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler"
* Sehife başlığında "Digər xidmətlər" olmalıdır
* Brauzeri bağla

## UI-SRV-022 Tariflər səhifəsində iki PDF linki var
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/hesablasma-emeliyyatlari/tarifler"
* "6" saniye gözle
* JavaScript icra et "var ls=[].slice.call(document.querySelectorAll('a[target=_blank]')).filter(function(a){return a.getAttribute('href').indexOf('site-api.bankofbaku.com/storage/')>=0});if(ls.length<2) throw new Error('PDF link sayı: '+ls.length)"
* JavaScript icra et "var t=document.body.innerText;if(t.indexOf('Fiziki şəxs üzrə tariflər')<0||t.indexOf('Hüquqi şəxs üzrə tariflər')<0) throw new Error('Tarif linkinin adı yoxdur')"
* Brauzeri bağla

## UI-SRV-023 FAQ səhifəsində suallar siyahısı var
tags: ui, services, faq

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/kart-emeliyyatlari/faq"
* "FAQ Sual" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('.faq__box').length;if(n<5) throw new Error('Sual sayı az: '+n)"
* JavaScript icra et "var a=document.querySelectorAll('.faq__box.active').length;if(a>0) throw new Error('Başlanğıcda açıq sual var: '+a)"
* Brauzeri bağla

## UI-SRV-024 FAQ sualına klik cavabı açır
tags: ui, services, faq

* Angular səhifəsini aç "/az/diger-xidmetler/kart-emeliyyatlari/faq" hazır element "FAQ Sual"
* "FAQ Sual" elementine klik et
* "2" saniye gözle
* JavaScript icra et "var b=document.querySelector('.faq__box.active');if(b===null) throw new Error('Cavab açılmadı');var a=b.querySelector('.faq__answer').getBoundingClientRect();if(a.height<20) throw new Error('Cavab görünmür');if(b.querySelector('.faq__question').getAttribute('aria-expanded')!=='true') throw new Error('aria-expanded true deyil')"
* Brauzeri bağla

## UI-SRV-025 FAQ sualına ikinci klik cavabı bağlayır
tags: ui, services, faq

* Angular səhifəsini aç "/az/diger-xidmetler/kart-emeliyyatlari/faq" hazır element "FAQ Sual"
* "FAQ Sual" elementine klik et
* "2" saniye gözle
* "FAQ Sual" elementine klik et
* "2" saniye gözle
* JavaScript icra et "var a=document.querySelectorAll('.faq__box.active').length;if(a>0) throw new Error('Cavab bağlanmadı: '+a)"
* Brauzeri bağla

## UI-SRV-026 Apple Pay səhifəsi açılır
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/odenis-sistemleri/applepay"
* "6" saniye gözle
* URL "/applepay" içermelidir
* JavaScript icra et "if(document.body.innerText.indexOf('Apple Pay')<0) throw new Error('Apple Pay mətni yoxdur')"
* Brauzeri bağla

## UI-SRV-027 Google Pay səhifəsi açılır
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/odenis-sistemleri/googlepay"
* "6" saniye gözle
* URL "/googlepay" içermelidir
* JavaScript icra et "if(document.body.innerText.indexOf('Google Pay')<0) throw new Error('Google Pay mətni yoxdur')"
* Brauzeri bağla

## UI-SRV-028 Loyallıq klubu səhifəsində üç bölmə var
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/diger/loyalliq-klubu"
* "6" saniye gözle
* JavaScript icra et "var t=document.body.innerText;if(t.indexOf('imtiyazları')<0||t.indexOf('kart növləri')<0||t.indexOf('necə üzv')<0) throw new Error('Bölmə çatışmır')"
* Brauzeri bağla

## UI-SRV-029 Tez-tez verilən suallar səhifəsi alt bölməyə yönləndirir
tags: ui, services, faq

* "chrome" brauzeri aç ve keçid et "/az/diger-xidmetler/tez-tez-verilen-suallar"
* "6" saniye gözle
* URL "/tez-tez-verilen-suallar/top10" içermelidir
* JavaScript icra et "var n=document.querySelectorAll('h2').length;if(n<3) throw new Error('Sual sayı az: '+n)"
* Brauzeri bağla

## UI-SRV-030 Təklif və iradlar səhifəsində əlaqə məlumatları göstərilir
tags: ui, services

* "chrome" brauzeri aç ve keçid et "/az/teklif-ve-iradlar"
* "6" saniye gözle
* Sehife başlığında "Təkliflər və iradlar" olmalıdır
* JavaScript icra et "var t=document.body.innerText;if(t.indexOf('shikayet@bankofbaku.com')<0||t.indexOf('145')<0) throw new Error('Əlaqə məlumatı yoxdur')"
* Brauzeri bağla
