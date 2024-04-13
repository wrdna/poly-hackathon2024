import random

# Define the move directions
move_directions = ['N', 'E', 'S', 'W']

# Define the special characters
special_characters = ['P', 'D']

# Function to generate random letters
def generate_random_letters(length):
    letters = []
    i = 0
    while i < length:
        # Generate a random letter from move directions or special characters
        if random.random() < 0.8:  # 80% chance of generating a move direction
            letter = random.choice(move_directions)
        else:  # 20% chance of generating a special character
            letter = 'P'
            letters.append(letter)
            i += 1
            
            # Generate a random move direction for 'D'
            d_direction = random.choice(move_directions)
            
            # Ensure the delta of move directions between 'P' and 'D' is not zero
            while d_direction == letter:
                d_direction = random.choice(move_directions)
            
            letters.append('D')
            i += 1
        
        letters.append(letter)
        i += 1
    letters.append('D')
    return ''.join(letters)

# Example usage
length = 10000
random_letters = generate_random_letters(length)
print(random_letters)
