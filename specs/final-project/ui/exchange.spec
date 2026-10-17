# UI: Valyuta məzənnəsi (UI-FX)

## UI-FX-001 Valyuta cədvəlləri yüklənir
tags: ui, exchange, smoke

* "chrome" brauzeri aç ve keçid et "/az"
* "Məzənnə Cədvəli Nağd" elementine scroll et
* "Məzənnə Cədvəli Nağd" görsensin deye maksimum "15" saniye gözle
* "Məzənnə Cədvəli" elementlerinin sayı en az "3" olmalıdır
* "Məzənnə Sətirləri Nağd" elementlerinin sayı "5" olmalıdır
* "Məzənnə Cədvəli Nağd" elementin içinde "USD" yazısı var
* "Məzənnə Cədvəli Nağd" elementin içinde "Alış" yazısı var
* "Məzənnə Cədvəli Nağd" elementin içinde "Satış" yazısı var
* Brauzeri bağla

## UI-FX-002 Alış məzənnəsi satış məzənnəsindən kiçik və ya bərabərdir
tags: ui, exchange

* "chrome" brauzeri aç ve keçid et "/az"
* "Məzənnə Cədvəli Nağd" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('table.tg').forEach(function(t,i){t.querySelectorAll('tr').forEach(function(r,j){if(j===0)return;var c=r.querySelectorAll('td');var a=parseFloat(c[1].innerText),s=parseFloat(c[2].innerText);if(!(a<=s)) throw new Error('Cədvəl '+(i+1)+' sətir '+j+': alış '+a+' > satış '+s)})})"
* Brauzeri bağla

## UI-FX-003 Məzənnə fərqi (spread) 10%-dən çox olmamalıdır (OBS-001)
tags: ui, exchange, known-bug

* "chrome" brauzeri aç ve keçid et "/az"
* "Məzənnə Cədvəli Nağd" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('table.tg').forEach(function(t,i){t.querySelectorAll('tr').forEach(function(r,j){if(j===0)return;var c=r.querySelectorAll('td');var a=parseFloat(c[1].innerText),s=parseFloat(c[2].innerText);if((s-a)/a>0.10) throw new Error('OBS-001 cədvəl '+(i+1)+' '+c[0].innerText.trim()+': alış '+a+' satış '+s)})})"
* Brauzeri bağla
