class Morse_Code:
    morse = {
        " ": " / ",
        "a":".- ",
        "b":"-... ",
        "c":"-.-. ",
        "d":"-.. ",
        "e":". ",
        "f":"..-. ",
        "g":"--. ",
        "h":".... ",
        "i":".. ",
        "j":".--- ",
        "k":"-.- ",
        "l":".-.. ",
        "m":"-- ",
        "n":"-. ",
        "o":"--- ",
        "p":".--. ",
        "q":"--.- ",
        "r":".-. ",
        "s":"... ",
        "t":"- ",
        "u":"..- ",
        "v":"...- ",
        "w":".-- ",
        "x":"-..- ",
        "y":"-.-- ",
        "z":"--.. ",
        "1":".---- ",
        "2":"..--- ",
        "3":"...-- ",
        "4":"....- ",
        "5":"..... ",
        "6":"-.... ",
        "7":"--... ",
        "8":"---.. ",
        "9":"----. ",
        "0":"----- "
    }

    def convert(self, word:str) -> str:
        """

        :param word:
        :return: Returns Morse Code
        """
        morse_code = ""
        word = word.lower()
        for i in word:
            morse_code += self.morse[i]
        return morse_code

    def print_morse(self,word):
        print(self.convert(word))

parse = Morse_Code()

def menu():
    return  "1 - Convert to Morse\n" \
            "0 - Exit"
def main():
    option = int(input("Enter Choice"))
    print(menu())
    while option != 0:
        if option == 1:
            user_input = input("Enter a word or sentence: ")
            while user_input is None or len(user_input) == 0:
                user_input = input("Please enter something")
            parse.print_morse(user_input)
        else:
            option = 0
            print("Goodbye")

if __name__ == "__main__":
    main()
