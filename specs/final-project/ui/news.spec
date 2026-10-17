# UI: Xəbərlər (UI-NWS)

## UI-NWS-007 Xəbərlər siyahısı yüklənir
tags: ui, news, smoke

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('a.news-card').length;if(n<5) throw new Error('Xəbər sayı az: '+n)"
* Brauzeri bağla

## UI-NWS-008 Hər xəbərin tarixi gg.aa.yyyy formatındadır
tags: ui, news

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var re=new RegExp('^[0-9]{2}[.][0-9]{2}[.][0-9]{4}$');var bad=[].slice.call(document.querySelectorAll('time.news-card__time')).filter(function(t){return !re.test(t.innerText.trim())});if(bad.length>0) throw new Error('Tarix formatı səhv: '+bad[0].innerText)"
* Brauzeri bağla

## UI-NWS-009 Xəbərlər tarixə görə yenidən köhnəyə sıralanıb
tags: ui, news

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "var ds=[].slice.call(document.querySelectorAll('time.news-card__time')).map(function(t){var p=t.innerText.trim().split('.');return Number(p[2]+p[1]+p[0])});for(var i=1;i<ds.length;i++){if(ds[i]>ds[i-1]) throw new Error('Sıralama pozulub: '+ds.join(', '))}"
* Brauzeri bağla

## UI-NWS-010 Xəbərin ətraflı səhifəsi açılır
tags: ui, news

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* "Xəbər Kartı" elementine klik et
* "5" saniye gözle
* URL "/az/xeberler/" içermelidir
* JavaScript icra et "if(document.querySelector('time.article__time')===null) throw new Error('Xəbər tarixi yoxdur')"
* JavaScript icra et "if(document.body.innerText.indexOf('Siyahıya geri dön')<0) throw new Error('Geri düyməsi yoxdur')"
* Brauzeri bağla

## UI-NWS-011 Səhifələmə ikinci səhifəyə keçir
tags: ui, news

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* JavaScript icra et "sessionStorage.setItem('n1',document.querySelector('a.news-card').getAttribute('href'))"
* "5" saniye gözle
* JavaScript icra et "var li=[].slice.call(document.querySelectorAll('ul.pagination li')).filter(function(l){return l.innerText.trim()==='2'})[0];li.querySelector('a').click()"
* "6" saniye gözle
* JavaScript icra et "if(document.querySelectorAll('a.news-card').length===0) throw new Error('DIAG url='+location.href+' title='+document.title+' len='+document.body.innerText.length+' txt='+document.body.innerText.slice(0,150).split(String.fromCharCode(10)).join(' / '))"
* JavaScript icra et "if(document.querySelector('a.news-card').getAttribute('href')===sessionStorage.getItem('n1')) throw new Error('Siyahı dəyişmədi')"
* JavaScript icra et "var a=document.querySelector('ul.pagination li.active');if(a===null||a.innerText.trim()!=='2') throw new Error('Aktiv səhifə 2 deyil')"
* Brauzeri bağla

## UI-NWS-012 Xəbər şəkilləri yüklənir
tags: ui, news

* "chrome" brauzeri aç ve keçid et "/az/xeberler"
* "Xəbər Kartı" görsensin deye maksimum "20" saniye gözle
* "4" saniye gözle
* JavaScript icra et "var bad=[].slice.call(document.querySelectorAll('.news-card__cover img')).filter(function(i){return !i.complete||i.naturalWidth===0});if(bad.length>0) throw new Error('Yüklənməyən şəkil sayı: '+bad.length)"
* Brauzeri bağla
