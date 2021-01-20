# Lab 2, Part 1: Author Class, John Cokins


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No titles yet published'
        return f'{self.name}. Books: {titles}'


def main():
    wodehouse = Author('P.G. Wodehouse')
    wodehouse.publish('My Man Jeeves')
    wodehouse.publish('A Prefect\'s Uncle')
    wodehouse.publish('The Gold Bat')
    print(wodehouse)


main()
