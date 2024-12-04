from json import load
f=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\books.json")
data=load(f)
# for book in data:
#     print(book)

all_titles=[book.get("title") for book in data]
# print(all_titles)

page_filter=[book.get("title")for book in data if book.get("pages")<250]
# print(page_filter)

all_genres=[book.get("genre")for book in data]
# print(set(all_genres))

genre_count={genre:all_genres.count(genre)for genre in all_genres }
# print(genre_count)

# print costly book
maximum_price=max(data,key=lambda d:d.get("price"))
# print(maximum_price)

# author with more than one book
all_author=[book.get("author")for book in data]
# print(all_author)
author_count={author:all_author.count(author)for author in all_author}
# print(author_count)
more_than_onebook={k:v for k,v in author_count.items() if v>1}
print(more_than_onebook)