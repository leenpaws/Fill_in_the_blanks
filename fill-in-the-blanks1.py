# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


def gamebegin():

    level = raw_input("Please choose a level 1. easy 2. medium 3. hard : ")

    if level == '3':
        return play_game(test_string3, parts_of_speech)
    if level == '2':
        return play_game(test_string2, parts_of_speech)
    if level == '1':
        return play_game(test_string1, parts_of_speech)
    return False


# A list of replacement words to be passed in to the play game function.
parts_of_speech  = ["Blank1", "Blank2", "Blank3", "Blank4"]
answer1 = ["attributes", "opening", "closing", "markup"]

answer2 = []

answer3 = []


# The following are some test strings to pass in to the play_game function.
test_string1 = "HTML Attributes: Some tags accept additional values called Blank1.  Most HTML tags consist of an" \
               " Blank2 and a Blank3 tag.  HTML is a type of Blank4 language"
test_string2 = "Ways of Thinking: Blank1 thinking involves creating perfectly clear and unambiguous instructions for a computer to follow.  Blank2 means finding" \
               "similarity, or as programmers would say generality amongst seemingly different things.  Blank3 thinking happens when you break " \
               "a big problem into smaller pieces "
test_string3 = ""

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    print ml_string
    ml_string = ml_string.split()
    i = 0
    for word in ml_string:

        replacement = word_in_pos(word, parts_of_speech)
        count = 0
        if replacement != None:
                for count in range(0,5):
                    user_input = raw_input("Type in answer: " + replacement + " ")
                    if ml_string == test_string1 and user_input == answer1[i] and count <= 5:
                        word = word.replace(replacement, user_input)
                        replaced.append(word)
                        print " ".join(replaced)
                    elif count > 5:
                        break
                    else:
                        print "incorrect"
                        count += 1


        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced




print gamebegin()











sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
