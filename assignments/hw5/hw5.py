"""
Name: <Belle Fortson>
<hw5>.py

Problem: <This program solves a number of problems involving strings and inputs.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    names1 = input('Input name here (first last): ')
    word = names1.split()
    final = word[::-1]

    print(', '.join(final))


def company_name():
    company = input('Enter a domain: ')
    names2 = company.split('.')[1]

    print(names2.capitalize())


def initials():
    students = eval(input("How many students are in the class? "))

    for i in range(1, students + 1):
        print("What is the name of student", i, "? ")
        names3 = input("")
        final = [s[0] for s in names3.split()]
        print(''.join(final))


def names():
    names4 = input('Enter a list of names: ')
    split = names4.split(', ')
    for i in split:
        split2 = i.split(' ')
        first = split2[0]
        last = split2[1]
        first_initial = first[0]
        second_initial = last[0]
        final = first_initial + second_initial
        print(final, end=' ')


def thirds():
    total_sent = ''
    sentences = eval(input('Enter the number of sentences: '))
    for i in range(sentences):
        text = input('Enter sentence: ')
        slice1 = text[::3]
        total_sent = total_sent + slice1
    print(total_sent)


def word_average():
    sentence = input('enter a sentence: ')
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)


def pig_latin():
    original = input('enter a sentence to convert to pig latin: ')
    words = original.split()
    pig = ''
    for i in words:
        first = i[0]
        rest = i[1:]
        end = "ay "
        pig = pig + rest + first + end
        pig = pig.lower()

    print(pig.rstrip())


if __name__ == "__main__":

    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()

