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

    def convert(self, word):
        morse_code = ""
        word = word.lower()
        for i in word:
            morse_code += self.morse[i]
        return morse_code

    def print_morse(self,word):
        print(self.convert(word))

parse = Morse_Code()

def main():
    user_input = input("Enter a word or sentence: ")
    parse.print_morse(user_input)

if __name__ == "__main__":
    main()
