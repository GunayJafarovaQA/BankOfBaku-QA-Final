# UI: Mobil görünüş (UI-MOB)

Pəncərə 500x900 ölçüsündədir (Chrome-un minimum eni səbəbindən 375px əvəzinə).

## UI-RSP-009 Hamburger menyu açılır və bölmələri göstərir
tags: ui, mobile, smoke

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* Pencere ölçüsünü "500" x "900" et
* "Mobil Menyu Düyməsi" görsensin deye maksimum "15" saniye gözle
* "Mobil Menyu Düyməsi" elementine JavaScript ile klik et
* "2" saniye gözle
* "Mobil Menyu Açıq" görsensin deye maksimum "10" saniye gözle
* JavaScript icra et "var n=document.querySelectorAll('.mobile-menu > ul > li').length;if(n<8) throw new Error('Mobil menyuda bölmə sayı az: '+n)"
* Brauzeri bağla

## UI-RSP-010 Hamburger menyu ikinci kliklə bağlanır
tags: ui, mobile

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* Pencere ölçüsünü "500" x "900" et
* "Mobil Menyu Düyməsi" görsensin deye maksimum "15" saniye gözle
* "Mobil Menyu Düyməsi" elementine JavaScript ile klik et
* "Mobil Menyu Açıq" görsensin deye maksimum "10" saniye gözle
* "Mobil Menyu Düyməsi" elementine JavaScript ile klik et
* "2" saniye gözle
* JavaScript icra et "if(document.querySelector('.mobile-menu.active')!==null) throw new Error('Menyu ikinci kliklə bağlanmadı')"
* Brauzeri bağla

## UI-RSP-011 Ana səhifədə üfüqi sürüşmə yoxdur
tags: ui, mobile

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* Pencere ölçüsünü "500" x "900" et
* "Kalkulyator Başlıq" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "var d=document.documentElement;if(d.scrollWidth>d.clientWidth+1) throw new Error('Üfüqi sürüşmə var: '+d.scrollWidth+' > '+d.clientWidth)"
* Brauzeri bağla

## UI-RSP-012 Kredit kalkulyatoru mobil enində işləyir
tags: ui, mobile

* "chrome" brauzeri aç ve keçid et "https://www.bankofbaku.com/az"
* Pencere ölçüsünü "500" x "900" et
* "Məbləğ Input" görsensin deye maksimum "15" saniye gözle
* "Məbləğ Input" elementini temizle
* "Məbləğ Input" elementine "3000" yaz ve Tab düymesine bas
* "2" saniye gözle
* "Məbləğ Input" input deyeri "3000" olmalıdır
* JavaScript icra et "var t=document.querySelector('.payment').innerText.trim();if(!t||isNaN(parseFloat(t))) throw new Error('Aylıq ödəniş hesablanmadı: '+t)"
* Brauzeri bağla
