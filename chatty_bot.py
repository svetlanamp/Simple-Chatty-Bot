# teaching the bot to introduce itself
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

# teaching the bot to greet the user
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# teaching the bot to guess the user's age
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

# teaching the bot to count
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# teaching the bot to ask multiple-choice questions
def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Which one is the false statement about indexing?")
    print("1. Indexing is zero-based.")
    print("2. To access an element of a list by its index, you need to use square brackets.")
    print("3. If you try to access an element with a non-existing index, you'll get an error SyntaxError.")
    print("4. You can't modify contents of a string wit indexes.")
    answer = int(input())
    while answer != 3:
        print("Please, try again.")
        answer = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()