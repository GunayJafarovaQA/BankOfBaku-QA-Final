# ABB Tech Academy – Yekun layihə (API + UI test avtomatlaşdırması)

**Müəllif:** Günay Cəfərova (GitHub: GunayJafarovaQA)
**Arxitektura:** müəllimin Gauge + Selenium + RestAssured + Maven framework-ü (dəyişdirilməyib).
README.md / README.az.md framework-ün özünün təsviridir; bu fayl yekun layihənin xülasəsidir.

## Test obyektləri
| Hissə | Obyekt | Ssenari sayı | Qovluq |
|---|---|---|---|
| API | Ayrıca sandbox bank API-si, api.anarabbas.com (beneficiaries, billers, bill payments/history, cards) | 123 (116 + 7 data-driven) | `specs/final-project/api/` |
| UI | https://www.bankofbaku.com/az | 97 (75 sabit + 22 məlum bug) | `specs/final-project/ui/` |

## İşə salma
Bir komanda ilə hər iki dəst (API + UI sabit ssenarilər): `bash run_all.sh`

Ayrı-ayrılıqda:
```bash
export JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.country=US -Djava.net.preferIPv4Stack=true"

# API (hamısı)
mvn test -Dgauge.specs.dir=specs/final-project/api

# UI – sabit ssenarilər (hamısı keçməlidir)
mvn test -Dgauge.specs.dir=specs/final-project/ui -Dtags='ui & !known-bug'

# UI – məlum bug ssenariləri (bug-ları təsdiqləmək üçün, uğursuz olması gözlənilir)
mvn test -Dgauge.specs.dir=specs/final-project/ui -Dtags='ui & known-bug'
```
Hesabat: `reports/html-report/index.html` (Gauge HTML report).

Data-driven nümunə: `specs/final-project/api/beneficiaries-data-driven.spec` (Gauge data table, 7 sətir).
JSON schema yoxlamaları: `src/test/resources/schema/` (beneficiary, beneficiary-list, card, error).

## Sənədlər (`docs/`)
- `Final_Project_API_Test_Cases_v2.xlsx` – API test case-lər, avtomatlaşdırma planı, izlənmə matrisi
- `Final_Project_UI_Test_Cases.xlsx` – 278 UI test case (prioritet, tip, status, avtomatlaşdırma)
- `Final_Project_UI_Bug_Siyahisi.xlsx` – təsdiqlənmiş bug siyahısı (27 bug), screenshot-lar
- `Final_Project_UI_Ehate_Statusu.xlsx` – modul üzrə əhatə statusu

## UI nəticələri
- 24 modul, 20-si avtomatlaşdırılıb (83%)
- 278 test case: 205 Keçdi, 54 Uğursuz, 5 Bloklanıb, 14 İcra olunmayıb
- 97 Selenium ssenarisi: 75 sabit, 22 məlum bug (`known-bug` teqi ilə)

## Əhatədən kənar (məqsədli)
- İnternet bankçılıq / giriş səhifəsi, forma göndərilməsi, "Müraciət et" düymələrinin real istifadəsi
- Hücum xarakterli yoxlamalar (çox uzun URL, XSS/SQL sətirləri, kuki analizi)

## Əsas texniki qeyd
Sayt Angular SSR-dir: HTML dərhal görünür, lakin hidratasiya bir neçə saniyə sonra bitir. Ona görə erkən klik və yazı itir.
Həll: element görünəndən sonra 3–5 saniyə gözləmək, `scrollIntoView` və lazım olan yerdə JS klik.
