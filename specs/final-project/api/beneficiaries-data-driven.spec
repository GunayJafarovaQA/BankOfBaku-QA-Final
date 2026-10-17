# Saxlanmış alıcılar — data-driven yoxlama: fullName sinifləri və valyuta (GRAD-101)

Eyni ssenari cədvəlin hər sətri üçün ayrıca işləyir (Gauge data table). Hər sətir bir ekvivalent sinif
və ya sərhəd dəyərini təmsil edir: etibarlı ad (201) və etibarsız ad (400 VALIDATION_ERROR). Hər ssenari yeni login
ilə təmiz sandbox-da başlayır, ona görə sətirlər bir-birindən asılı deyil.

   |ad                  |iban                        |valyuta|status|
   |--------------------|----------------------------|-------|------|
   |Li                  |AZ83AIIB40060019440000000001|AZN    |201   |
   |Əli-Vəli Məmmədov   |AZ83AIIB40060019440000000001|USD    |201   |
   |O'Neil Ümid         |AZ83AIIB40060019440000000001|EUR    |201   |
   |A                   |AZ83AIIB40060019440000000001|AZN    |400   |
   |Ali2                |AZ83AIIB40060019440000000001|AZN    |400   |
   |Ali@                |AZ83AIIB40060019440000000001|AZN    |400   |
   |-Ali                |AZ83AIIB40060019440000000001|AZN    |400   |

* Yeni təmiz sandbox ilə user1 kimi daxil ol

## TC-BEN-DD Alıcı yaradılması: ad sinifləri üzrə gözlənilən status (data-driven)

tags: grad-101, regression, data-driven, boundary

* Alıcı yarat ad <ad> iban <iban> valyuta <valyuta>
* Status kodunun <status> olmalıdır
