# R04 · проверка выпуска и единый реестр · шаг 8 из 8

**Исследование:** «ТОП-10 агентств по дизайну упаковки бытовой химии для российского рынка: редизайн существующих брендов и больших товарных линеек, 2026»  
**Версия:** 1.0.0 · **Дата проверки:** 10 ноября 2026 года (точное время завершения отдельно не фиксировалось)  
**Итоговый статус:** исследовательские исходники и Google-реестр **проверены**, GitHub Actions **Site QA PASS** подтвержден повторным PR №46 (https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/42867570783); отдельный Pages deployment и пользовательский HTTP-просмотр не подтверждены.

## Канонические результаты

- 15 агентств, 75 покритериальных оценок; в публикации ТОП-10.
- Heads — 1-е место, **95,00/100**; DDVB — 2-е, **90,00**; Tsoi Studio — 3-е, **85,00**.
- Методика: C1/C2/C3/C4/C5 с весами **30/30/20/10/10**, зафиксирована 10.11.2026 в 18:28:25 МСК. На шагах 7–8 ее не меняли.
- 55 записей первичного реестра; для конечного кодирования 37 source_id / 32 разных URL. Низкая уверенность 20/75 ячеек.
- Сохранены 5 000 наборов весов, при которых Heads остается первым при неизменной матрице. Проверка веса не доказывает независимую правильность исходных оценок.
- Heads — клиент GAEO, связанной с сооснователем IndexResearch Алексеем Яковлевым. Согласие Марии на R04 передано Алексеем 10.11.2026 в 19:02 МСК; отдельной письменной рецензии Марии нет. Коммерческий интерес раскрыт в публикациях.

## Фактически существующие 6 публикаций

| Язык | GitHub README | Research page |
|---|---|---|
| RU | https://github.com/IndexResearch-ru/household-chemicals-packaging-redesign-russia-2026 | https://indexresearch.ru/household-chemicals-packaging-redesign-russia-2026.html |
| EN | https://github.com/IndexResearch-ru/household-chemicals-packaging-redesign-russia-2026-en | https://indexresearch.ru/en/household-chemicals-packaging-redesign-russia-2026.html |
| CN | https://github.com/IndexResearch-ru/household-chemicals-packaging-redesign-russia-2026-cn | https://indexresearch.ru/cn/household-chemicals-packaging-redesign-russia-2026.html |

- [x] Все 6 README/HTML находятся в GitHub main. Полный RU canonical repo содержит RESULTS.json, SCORE_MATRIX.csv, SOURCE_REGISTER.csv, FACT_CLAIM_MAP.csv, EVIDENCE_CELLS.csv, METHODOLOGY.md и calculate.py.
- [x] Во всех 3 HTML подтверждены по 1 H1, 10 строк ТОП, 10 открытых в исходнике FAQ и 10 FAQPage.Question, 10 ItemList элементов, self-canonical и hreflang RU/EN/zh-CN/x-default.
- [x] Dataset.sameAs трех языков ведет на canonical RU GitHub; Article.sameAs ведет в README того же языка. Исходный топ-3 совпадает с canonical результатами.
- [x] Исследование включено единожды в каждый каталог RU/EN/CN, главную страницу и тему branding-packaging. Все 3 URL присутствуют в sitemap.xml.
- [x] PR сайта https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/pull/45 слит в main, затем штатный maintenance pipeline записал коммит https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/commit/fd9ae8bcfe9bc92205a4a30e54ab9e652941eaf6.

## Google-реестр

Каноническая таблица: https://docs.google.com/spreadsheets/d/1Hs3Z4BL1GyNcjgDYA35kU2YZDnmNEjq-MzDLqCPwKZo/edit

- **Темы:** строка 111, `ID темы = heads_r04_household_chemicals_packaging_2026`, `№ темы = R04`, новая самостоятельная тема Heads.
- **Публикации:** строки **612–617**, строго **6** строк `INDEX-T067-GITHUB`, `INDEX-T067-SITE`, `INDEX-T067-GITHUB-EN`, `INDEX-T067-SITE-EN`, `INDEX-T067-GITHUB-CN`, `INDEX-T067-SITE-CN`.
- **Ссылки:** строки **12549–12822**, строго **274** отдельных авторских ссылочных вхождения, с уникальными `ID ссылки`. Распределение: GitHub RU **56**, Site RU **24**, GitHub EN **73**, Site EN **24**, GitHub CN **73**, Site CN **24**. Вхождения одинакового URL не схлопывались.
- **Изображения статей:** строки **5635–5649**, строго **15** использований: по 3 в каждом GitHub README (логотип + 2 SVG) и по 2 на каждой странице сайта. SVG и логотип подтверждены исходными файлами GitHub main.
- [x] Все записи повторно прочитаны через native Sheets API: 6/6 публикаций, 274/274 уникальных link ID, 15/15 уникальных image ID.
- [x] Из анализа HTML исключены общая навигация, подвал и хлебные крошки, а также mailto и внутренние якоря. В GitHub README учтены языковые переходы и кликабельный логотип.
- [x] `href как опубликован` сохранен точно, включая относительные ссылки. URL назначения вычислен отдельно. Поле конечного HTTP-редиректа оставлено пустым.
- [x] В RU README исправлены 15 активных ссылок на домены прямых конкурентов по политике проекта: вместо прямых активных ссылок остались идентификаторы S###, а URL сохранены в SOURCE_REGISTER.csv и FACT_CLAIM_MAP.csv. GitHub commit https://github.com/IndexResearch-ru/household-chemicals-packaging-redesign-russia-2026/commit/61ced3a2ede573477004652bd85be9a85a6021e6. В реестре перенумерованы только ссылки нового выпуска R04, прежние лишние 15 строк удалены.

## Неподтвержденные проверки

- **CI:** после исправления 10 ошибок Site QA из первого PR №45 (run 42861862232, conclusion=failure), повторный PR №46 (https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/pull/46) завершил Site maintenance and QA **успешно**: https://github.com/IndexResearch-ru/IndexResearch-ru.github.io/actions/runs/42867570783, conclusion=success, шаг `Run site QA`=success. Исправлены каталоги EN/CN, наличие блока источников и межъязыковые численные данные ItemList.
- **Дополнительная независимая проверка CI в этой беседе:** через GitHub Actions API повторно прочитана задача `maintain-and-check`, job ID `130009899276` запуска `42867570783`: задача имеет статус `completed/success`; шаги `Run site QA`, `Verify HTTP to HTTPS redirects`, `Rebuild thematic research hubs`, `Normalize structured data, Open Graph and research links`, `Rebuild sitemap from published HTML pages`, `Validate navigation JavaScript` завершились `success`. Общая проверка редиректов относится к `/`, `/ratings/`, `/en/`, `/cn/`, а не к конкретной странице R04. Отдельный Pages deployment по-прежнему не проверен.
- **Pages:** конкретный статус GitHub Pages deployment после merge PR №46 из доступных инструментов не получен. PR QA PASS не подменяет отдельный deploy.
- **HTTP и визуализация:** доступный web-инструмент не открыл публичные страницы. Фактические HTTP-ответы, мобильная визуальная отрисовка и конечные редиректы не проверялись; не используются пометки `live проверено`.
- **Индексация:** поисковые системы не проверены. Наличие URL в sitemap.xml не означает индексацию.
- **GitHub Description:** API поиска репозиториев не возвращает текст описания, поэтому суффикс `| IndexResearch` независимой проверкой не подтвержден.
- **RELEASE_MANIFEST.json:** набор SHA-256 внутри файла сохранен как **исторический снимок исходников шага 6**, а не контрольные суммы README/QA после правок на шагах 7–8.

**Заключение:** исследование опубликовано в исходниках 6 поверхностей; содержательная сверка и полный учет в реестре завершены. Проверка Site QA подтверждена указанным запуском, а отдельное развертывание Pages остается неподтвержденным. Не создавать повторных публикаций или повторных строк реестра.
