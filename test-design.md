Таблиця проєктування тестів
| Тест-кейс | Вхідні дані | Очікуваний результат | Техніка | Статус |
|---|---|---|---|---|
| TC-01 | add_book("Harry Potter") | Книга додана | EP, positive | pass |
| TC-02 | add_book("") | ValueError | BVA, negative | pass |
| TC-03 | add_book("   ") | ValueError | BVA, negative | pass |
| TC-04 | add_book("1984") повторно | ValueError | EP, negative | pass |
| TC-05 | search_book("Dune") | True | EP, positive | pass |
| TC-06 | search_book("dune") | True | EP, positive | pass |
| TC-07 | search_book("Metro") | False | EP, negative | pass |
| TC-08 | search_book("") | ValueError | BVA, negative | pass |
| TC-09 | borrow_book("Metro 2033") | Book borrowed | EP, positive | pass |
| TC-10 | borrow_book("Unknown Book") | ValueError | EP, negative | pass |
