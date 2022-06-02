"""

Program: doctor.py
Author: Ken
Conduct an interactive session of nondirective
psychotherapy
"""

import random

hedges = ("Please tell me more. ",
              "Many of my patients tell me the same thing.",
              "Please continue.")

qualifiers = ("Why do you say that ",
                  "You seems to say that ",
                  "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
                     "we":"you", "us":"you", "mine":"yours"}

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + sentence

    def main():
            """Handles the interaction between patient and doctor."""
            print("Good morning, I hope you are well today.")
            print("What can I do for you?")
            while True:
                 sentence = input("\n>> ")
                 if sentence.upper() == "QUIT":
                    print("Have a nice day!")
                    break
                 print(reply(sentence))

        # The entry point for program execution
    if __name___ == ' __main':__
    main()