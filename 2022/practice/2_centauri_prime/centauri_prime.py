# Read the number of cases:
n_cases = int(input())

# Associates a set of letter to a player's name
LETTER_TO_PLAYER = {
    "Alice": ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'],
    "nobody": ['y', 'Y']
}

def get_player_name(last_letter):
    player_name = "Bob"
    for k, v in LETTER_TO_PLAYER.items():
        if last_letter in v:
            player_name = k
    return player_name

for case_i in range(n_cases):
    kingdom_name = str(input())
    ruler_name = get_player_name(kingdom_name[-1])
    
    print(f"Case #{case_i+1}: {kingdom_name} is ruled by {ruler_name}.")
