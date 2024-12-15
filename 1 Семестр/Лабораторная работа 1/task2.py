# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
lines = 50
chars = 25
disketa_space_kb = 1.44 * 1024
kbytes_per_char = 4/1024


kbytes_per_str = kbytes_per_char * chars
kbytes_per_page = kbytes_per_str * lines
kbytes_per_book = kbytes_per_page * pages
qty_books = int(disketa_space_kb / kbytes_per_book)

print("Количество книг, помещающихся на дискету:", qty_books)
