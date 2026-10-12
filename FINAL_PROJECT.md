# ABB Tech Academy – Yekun layihə (API + UI test avtomatlaşdırması)

**Müəllif:** Günay Cəfərova (GitHub: GunayJafarovaQA)
**Arxitektura:** müəllimin Gauge + Selenium + RestAssured + Maven framework-ü (dəyişdirilməyib).
README.md / README.az.md framework-ün özünün təsviridir; bu fayl yekun layihənin xülasəsidir.

## Test obyektləri
| Hissə | Obyekt | Ssenari sayı | Qovluq |
|---|---|---|---|
| API | Bank API (beneficiaries, billers, bill payments/history, cards) | 116 | `specs/final-project/api/` |
| UI | https://www.bankofbaku.com/az | 97 (75 sabit + 22 məlum bug) | `specs/final-project/ui/` |

## İşə salma
```bash
export JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.country=US"

# API
mvn test -Dgauge.specs.dir=specs/final-project/api -Dtags='grad-101'

# UI – sabit ssenarilər (hamısı keçməlidir)
mvn test -Dgauge.specs.dir=specs/final-project/ui -Dtags='ui & !known-bug'

# UI – məlum bug ssenariləri (bug-ları təsdiqləmək üçün, uğursuz olması gözlənilir)
mvn test -Dgauge.specs.dir=specs/final-project/ui -Dtags='ui & known-bug'
```
Hesabat: `reports/` qovluğu (Gauge HTML report).

## Sənədlər (`docs/`)
- `Final_Project_API_Test_Cases_v2.xlsx` – API test case-lər, avtomatlaşdırma planı, izlənmə matrisi
- `Final_Project_UI_Test_Cases.xlsx` – 274 UI test case (prioritet, tip, status, avtomatlaşdırma)
- `Final_Project_UI_Bug_Siyahisi.xlsx` – təsdiqlənmiş bug siyahısı (26 bug), screenshot-lar
- `Final_Project_UI_Ehate_Statusu.xlsx` – modul üzrə əhatə statusu

## UI nəticələri
- 24 modul, 20-si avtomatlaşdırılıb (83%)
- 274 test case: 202 Keçdi, 52 Uğursuz, 5 Bloklanıb, 15 İcra olunmayıb
- 97 Selenium ssenarisi: 75 sabit, 22 məlum bug (`known-bug` teqi ilə)

## Əhatədən kənar (məqsədli)
- İnternet bankçılıq / giriş səhifəsi, forma göndərilməsi, "Müraciət et" düymələrinin real istifadəsi
- Hücum xarakterli yoxlamalar (çox uzun URL, XSS/SQL sətirləri, kuki analizi)

## Əsas texniki qeyd
Sayt Angular SSR-dir: HTML dərhal görünür, lakin hidratasiya bir neçə saniyə sonra bitir. Ona görə erkən klik və yazı itir.
Həll: element görünəndən sonra 3–5 saniyə gözləmək, `scrollIntoView` və lazım olan yerdə JS klik.
