# KOMBO.unit — landing page food & coffee

Gotowa strona w HTML, CSS i JavaScript, przygotowana na podstawie prezentacji KOMBO.unit i portfolio Krystiana Pakieły. Bez procesu budowania i bez zewnętrznych zależności podczas wyświetlania.

## Podgląd

Otwórz `index.html` w przeglądarce lub uruchom w folderze projektu:

```sh
python3 -m http.server 8765
```

Następnie otwórz http://localhost:8765.

## Zawartość

- Identyfikacja z PDF-u: Poppins, czerwień, biel, czerń, duża typografia.
- Portfolio: wybrane realizacje, ruchomy podgląd 12 dodatkowych zdjęć i pełna rozwijana galeria 65 zdjęć.
- Dwanaście pełnych realizacji video — 6 dotychczasowych i 6 nowych poziomych: automatyczne odtwarzanie bez dźwięku, pętla, natywne kontrolki, pauza poza ekranem i obsługa ograniczonego ruchu.
- Wersje video H.264/AAC MP4 (około 93 MB łącznie); źródła zapisane w `references/video-sources.json`.
- Strategia, produkcja foto/video, obsługa social media.
- Pakiety jednorazowe, abonamenty i strategia zgodnie z prezentacją.
- Portrety i opis Michała Traczyka oraz Krystiana Pakieły.
- Klikalny telefon i e-mail, kontakt vCard, oferta PDF.
- Responsywny układ, obsługa klawiaturą, podgląd fotografii, ograniczony ruch.

## GitHub Pages

Workflow `.github/workflows/pages.yml` publikuje stronę po pushu na `main`.
W repozytorium wybierz **Settings → Pages → Source → GitHub Actions**.
Workflow wysyła wyłącznie `index.html`, `style.css`, `app.js` i `assets/`.
Publiczny adres: https://krispaki.github.io/kombo-landing/
Metadane Open Graph i canonical wskazują ten adres.

## Skille

Zainstalowane również lokalnie w `~/.codex/skills/`:
- `frontend-design` — https://github.com/anthropics/skills/tree/main/skills/frontend-design
- `web-design-guidelines` — https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

Kopie skilli (oraz dołączona przez Anthropic licencja) znajdują się w `.agents/skills/`, tak aby skille trafiły do repozytorium wraz ze stroną.

## Źródła i prawa

Treści, ceny, dane kontaktowe i portrety: dostarczony `KOMBO.unit_oferta_content.pdf`.
Fotografie: https://krystianpakiela.pl/foodphotography — mapowanie URL-i w `references/image-sources.json`.
Zdjęcia należą do ich właścicieli; kod projektu nie nadaje praw do ich ponownego wykorzystania.
Poppins: Google Fonts, SIL Open Font License (`assets/FONT-LICENSE.txt`).
Lista marek przedstawia doświadczenie twórców z prezentacji, z podziałem na strategię i produkcję.
PDF nie określa, czy ceny są netto/brutto; strona tego nie dopowiada.
