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
# A list of replacement words to be passed in to the play game function.
parts_of_speech = ["__1__", "__2__", "__3__", "__4__"]
answer1 = ["attributes", "opening", "closing", "markup"]

answer2 = ['procedural', 'abstract', 'systems', 'debugging']

answer3 = ['columns', 'key']

# The following are some test strings to pass in to the play_game function.
test_string1 = "HTML Attributes: Some tags accept additional values called __1__.  Most HTML tags consist of an" \
               " __2__ and a __3__ tag.  HTML is a type of __4__ language"
test_string2 = "Ways of Thinking: Blank1 thinking involves creating perfectly clear and unambiguous instructions" \
               " for a computer to follow.  __2__ means finding" \
               "similarity, or as programmers would say generality amongst seemingly different things.  __3__ thinking happens when you break " \
               "a big problem into smaller pieces.  __4__ is a systematic process of relentlessly identifying the cause of a computer program" \
               "failure"
test_string3 = "Rules Summary for Normalized Tables: 1. Every row has the same number of __1__.  2.  There is a  unique key and everything " \


def gamebegin():
    level = raw_input("Please provide answer in all lower case!!" \
                      "Please choose a level 1. easy 2. medium 3. hard : ")
    if level == '3':
        print test_string3
        return play_game(test_string3, parts_of_speech, answer3)
    if level == '2':
        print test_string2
        return play_game(test_string2, parts_of_speech, answer2)
    if level == '1':
        print test_string1
        return play_game(test_string1, parts_of_speech, answer1)
    return False


# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None



# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.

def play_game(ml_string, parts_of_speech, answer):
    i = 0
    user_tries = 5
    while user_tries != 0:
        replacement = word_in_pos(ml_string, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a value for  " + replacement + ":")
            if user_input == answer[i] and user_tries > 0:
                ml_string = ml_string.replace(replacement, answer[i])
                user_tries = 5
                i += 1
                print "Correct " + ml_string
            else:
                user_tries -= 1
                print "Incorrect, you have " + str(user_tries) + " tries left"
        else:
            break



print gamebegin()
