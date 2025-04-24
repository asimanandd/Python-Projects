import random

print(" ")
print(" ")
print(" 🥳 WELCOME TO THIS CLASSIC HAND CRICKET MATCH BETWEEN YOU AND THE LORD COMPUTER 🥳")
print("____________________________________________________________________________")
print("____________________________________________________________________________")
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.out = False

class Game:
    def __init__(self):
        self.user = Player("User")
        self.computer = Player("Computer")
        self.user_bats_first = None

    def Toss(self):
        print("TOSS TIME! Choose HEADS or TAILS")
        user_choice = input("Enter H for Heads or T for tails").strip().upper()
        toss_result = random.choice(['H', 'T'])

        if user_choice == toss_result:
            print("CONGRATULATIONS 🎉, YOU WON THE TOSS")
            choice = input("What are you gonna do first?(BAT for Batting or BOWL for Bowling): ").strip().upper()
            self.user_bats_first = True if choice == "BAT" else False

        else:
            print("Computer won the toss! ")
            comp_choice = random.choice(['BAT', 'BOWL'])
            print(f"Computer chose to {'BAT' if comp_choice == 'BAT' else 'BOWL'} first.")
            self.user_bats_first = False if comp_choice == "BAT" else True

    def play_innings(self, batting_player, bowling_player, target=None):
        print(f"\n{batting_player.name} is batting now!")
        while not batting_player.out:
            try:
                user_input = int(input("Choose your run (1-6): ")) if batting_player.name == "User" else random.randint(1, 6)
                comp_input = random.randint(1, 6) if batting_player.name == "User" else int(input("Choose your run (1-6): "))

                print(f"{batting_player.name} chose: {user_input}")
                print(f"{bowling_player.name} chose: {comp_input}")

                if user_input == comp_input:
                    print(f"{batting_player.name} is OUT!")
                    batting_player.out = True
                else:
                    batting_player.score += user_input
                    print(f"{batting_player.name}'s score: {batting_player.score}")

                    if target and batting_player.score > target:
                        print(f"{batting_player.name} has chased the target successfully!")
                        break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")


    def start_game(self):
        self.Toss()  
        if self.user_bats_first:
            self.play_innings(self.user, self.computer)
            self.target = self.user.score + 1
            print(f"\nTarget for {self.computer.name}: {self.target}")
            self.play_innings(self.computer, self.user, self.target)
        else:
            self.play_innings(self.computer, self.user)
            self.target = self.computer.score + 1
            print(f"\nTarget for {self.user.name}: {self.target}")
            self.play_innings(self.user, self.computer, self.target)

        print("\n--- Match Result ---")
        if self.user.score > self.computer.score:
            print("🎉 You won the match!")
        elif self.user.score < self.computer.score:
            print("💻 Computer won the match!")
        else:
            print("🤝 It's a tie!")


if __name__ == "__main__":
    game = Game()
    game.start_game()
