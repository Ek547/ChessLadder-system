import tkinter as tk
import csv
class ChessPlayer:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating  # Starting rating, you can adjust this as needed

    def __str__(self):
        return f"{self.name} (Rating: {self.rating})"

class ChessMatch:
    def __init__(self, player1, player2, outcome):
        self.player1 = player1
        self.player2 = player2
        self.outcome = outcome 
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")


        self.add_player_button = self.create_button("Add Player", self.add_player)
        self.remove_player_button = self.create_button("Remove Player", self.remove_player)
        self.create_match_button = self.create_button("Create Match", self.create_match)
        self.update_ratings_button = self.create_button("Update Ratings", self.update_ratings)
        self.display_ladder_button = self.create_button("Display Ladder", self.display_ladder)
        self.save_ladder_button = self.create_button("Save Ladder", self.save_ladder)

        self.add_player_button.pack()
        self.remove_player_button.pack()
        self.create_match_button.pack()
        self.update_ratings_button.pack()
        self.display_ladder_button.pack()
        self.save_ladder_button.pack()

        self.input_label = tk.Label(root, text="Enter player name:")
        self.input_entry = tk.Entry(root)
        self.input_label.pack()
        self.input_entry.pack()

        self.display_ladder_frame = None


    def create_button(self, text, command):
        return tk.Button(self.root, text=text, command=command)

    def add_player(self):
        # Call the function from the other object to add a player
        name = self.input_entry.get()
        ladder.add_player(ChessPlayer(name,1000))
        self.input_entry.delete(0, tk.END)

    def remove_player(self):
        # Call the function from the other object to remove a player
        delname = self.input_entry.get()
        #print(delname)
        player_to_remove = next((p for p in ladder.players if p.name == delname), None)
        if player_to_remove:
            ladder.remove_player(player_to_remove)
        #else:
            #print("Player not found.")
        self.input_entry.delete(0, tk.END)

    def create_match(self):
        # Call the function from the other object to create a match

            self.clear_main_page()
            self.input_label_1 = tk.Label(root, text="Enter the name of the white player:")
            self.input_entry_1 = tk.Entry(root)
            self.input_label_1.pack()
            self.input_entry_1.pack()

            self.input_label_2 = tk.Label(root, text="Enter the name of the black player: ")
            self.input_entry_2 = tk.Entry(root)
            self.input_label_2.pack()
            self.input_entry_2.pack()

            self.input_label_3 = tk.Label(root, text="Enter the outcome (white win(1), black win(-1), or draw(0)): ")
            self.input_entry_3 = tk.Entry(root)
            self.input_label_3.pack()
            self.input_entry_3.pack()

            self.add_match_button= self.create_button("Create match", self.add_match)
            self.add_match_button.pack()
        
            
    def add_match(self):
            player1_name = self.input_entry_1.get()
            player2_name = self.input_entry_2.get()
            outcome = self.input_entry_3.get()
            player1 = next((p for p in ladder.players if p.name == player1_name), None)
            player2 = next((p for p in ladder.players if p.name == player2_name), None)
            if player1 and player2:
                ladder.create_match(player1, player2, outcome)
                #print("Match created.")


            #else:
                #print("One or both players not found.")
            self.clear_main_page()
            self.show_main_page()

    def update_ratings(self):
            ladder.update_ratings()
            #print("Ratings updated based on match outcomes.")
    def display_ladder(self):
        # Call the function from the other object to display the ladder
        self.clear_main_page()

        # Create a new frame for the ladder display
        self.display_ladder_frame = tk.Frame(self.root)
        self.display_ladder_frame.pack()

        # Create ladder display content (you can replace this with your ladder display logic)
        ladder_label = tk.Label(self.display_ladder_frame, text="Ladder Display")
        ladder_label.pack()
        ladder_text = tk.Text(self.display_ladder_frame)
        ladder_text.pack()

        ladder.players.sort(key=lambda x: x.rating, reverse=True)
        #print("Chess Ladder:")
        for i, player in enumerate(ladder.players, 1):
            ladder_text.insert("50000.0",f"{i}. {player}\n")


        
        #ladder.display_ladder()
        back_button = self.create_button("Back", self.show_main_page)
        back_button.pack()
    def clear_main_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_page(self):
        if self.display_ladder_frame:
            self.display_ladder_frame.destroy()
        
        self.__init__(self.root)
            

    def save_ladder(self):
            ladder.save_ladder("chess_ladder.csv")
            #print("Ladder saved successfully.")



class ChessLadder:
    def __init__(self):
        self.players = []
        self.matches = []
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
            self.players.remove(player)

    def create_match(self, player1, player2, outcome):
        match = ChessMatch(player1, player2, outcome)
        self.matches.append(match)

    def display_ladder(self):
        self.players.sort(key=lambda x: x.rating, reverse=True)
        #print("Chess Ladder:")
        for i, player in enumerate(self.players, 1):
            ladder_text.insert(f"{i}. {player}")


    def save_ladder(self, filename):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Name", "Rating"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for player in self.players:
                writer.writerow({"Name": player.name, "Rating": player.rating})

    def load_ladder(self, filename):
        try:
            with open(filename, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                self.players = []
                for row in reader:
                    name = row["Name"]
                    rating = float(row["Rating"])
                    #print(name,rating)
                    self.add_player(ChessPlayer(name,rating))
            #print("Ladder loaded successfully.")
        except FileNotFoundError:
            #print("Ladder file not found. Starting with an empty ladder.")
            pass

    def update_ratings(self):
        for match in self.matches:
            if match.outcome == "1":
                winner = match.player1
                loser = match.player2
            elif match.outcome == "-1":
                winner = match.player2
                loser = match.player1
            else:
                continue  # Draw, no rating changes

            rating_difference = loser.rating - winner.rating
            k = 32  # Weighting factor
            expected_score = 1 / (1 + 10 ** (rating_difference / 400))
            rating_change = (k * (1 - expected_score))//1

            winner.rating += rating_change
            loser.rating -= rating_change
if __name__ == "__main__":
    ladder = ChessLadder()
    ladder.load_ladder("chess_ladder.csv")
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
