import getpass

def delfind(searchval, solution):
    found = False
    for char in solution:       
        if char == searchval:
            solution = solution.replace(char,'')
            found = True
    return [solution, found]

def updateguess(char, sol, guess_state):
    for index, val in enumerate(sol):
        if char == sol[index]:
            guess_state = guess_state[:index] + char + guess_state[index +1:]
    return guess_state

class hangman:
    #creates hang man instance with answer so that game can start

    stages = ["________", #1
              " |\n |\n |\n_|_______", #2
              " ______\n |\n |\n |\n_|_______", #3
              " ______\n |  ó\n |\n |\n_|_______", #4
              " ______\n |  ó\n |  |\n |\n_|_______", #5
              " ______\n |  ó\n | /|\\\n |\n_|_______", #6
              " ______\n |  ó\n | /|\\\n | / \\ \n_|_______\n Game Over!" ] #7

    def __init__(self):
        self.answer = None
    
    def set_answer(self, answer):
        self.answer = answer
        return self

def hangman_game():
    game = hangman()
    answer = getpass.getpass(prompt="type in answer, and don't show anyone ")
    static_answer = answer
    counter = 0
    guessresponse = len(answer) * "_"
    print(f"this is the current word {guessresponse}")

    while counter < len(game.stages):
        guess = input(f"guess number {counter + 1}: ")        
        if len(guess) > 1 and guess == static_answer:
            print(f"Looks like we got a badass over here!, the word was indeed {static_answer}!!!")
            return
        elif len(guess) > 1 and guess != static_answer:
            print(game.stages[counter])
        elif delfind(guess, answer)[1] == False: #function that returns false if guessed character not in solution, also returns updated answer if true
            print(game.stages[counter])
            counter += 1
        else:
            answer = delfind(guess, answer)[0]
            guessresponse = updateguess(guess,static_answer,guessresponse)
            if guessresponse == static_answer:
                print("Good job, you got the answer!!!")
                break
            else:    
                print(f"Nice! the current status is {guessresponse}\n")
    print(f"The word was: {static_answer}")


hangman_game()

