import json
import hashlib

class CountryReader():
    def __init__(self, file_name: str):
        self.cursor = - 1
        with open(file_name, 'r', encoding='utf8') as file:
            self.countries = json.load(file)


    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.countries):
            raise StopIteration
        return self.countries[self.cursor]['name']['common']


if __name__ == '__main__':
    countries_reader = CountryReader('countries.json')
    with open('result.txt', 'w', encoding='utf8') as file:
        counter = 0
        for country in countries_reader:
            counter += 1
            file.write(f'{country} - https://en.wikipedia.org/wiki/{country.replace(" ", "_")}\n')
        file.write(f'\nнайдено {counter} стран')

    def LineReader(filename: str):

        with open(filename, 'r', encoding='utf8') as my_file:
            while True:
                line = my_file.readline()
                if line:
                    yield hashlib.md5(line.encode('utf8')).hexdigest()
                else:
                    break



    for item in LineReader('result.txt '):
        print(item)


