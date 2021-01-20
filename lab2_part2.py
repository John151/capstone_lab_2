# Lab 2, Part 2: Author Class no Repeats, John Cokins


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        # book title is made lowercase to check, user might enter a duplicate title capitalized
        # differently and we want to catch that
        title = title.lower()
        if title in self.books:
            print(f'The title {title.title()} is already listed')
        else:
            self.books.append(title)

    def __str__(self):
        # list comprehension used to capitalize each word in title
        title_capitalized = [book.title() for book in self.books]
        titles = ', '.join(title_capitalized) or 'No titles yet published'
        return f'{self.name}. Books: {titles}'


def main():
    wodehouse = Author('P.G. Wodehouse')
    wodehouse.publish('My Man Jeeves')
    wodehouse.publish('A Prefect\'s Uncle')
    wodehouse.publish('The Gold Bat')
    wodehouse.publish('The Gold Bat')
    print(wodehouse)


main()
