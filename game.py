import chimp
import spear_the_shark


def main():
    print("Please choose which game you'd like to play:")
    user_choice = input("shark or chimps? ")
    user_choice.lower()
    print()
    print("You chose " + user_choice + ". Enjoy!")

    if user_choice == 'shark' or user_choice == 'sharks':
        spear_the_shark.main()
    elif user_choice == 'chimps' or user_choice == 'chimp':
        chimp.main()
    else:
        print("Sorry that was not an option. Goodbye.")
        quit()


main()
