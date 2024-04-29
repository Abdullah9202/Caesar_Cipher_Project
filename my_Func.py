import os

# Creating an alphabet list (Double the alphabets to overcome the error of index out of range ==> If user enter z then it will loop to the next positions)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Fuction to clear the terminal
def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


# # Function that takes the text and encrypts it according to the shifts
# def encrypt(plain_text, shfits):
#     encrypted_Text = "" # To store the encrypted data
#     # Using for loop to change position of alphabets according to the shifts
#     for letters in plain_text:
#         # Current position of alphabet in the list
#         position = alphabets.index(letters)
        
#         # Modified position (Shifts added)
#         mod_Position = position + shfits
        
#         # Assigining the new alphabet according to the modified postion
#         new_Letter = alphabets[mod_Position]
     
#         # Adding to encrypted_Text at each iteration
#         encrypted_Text += new_Letter
    
#     # Print out
#     print(f"Encrypted Text : {encrypted_Text}")
    
    
# # Function that takes the encrypted text and decrypts it according to the shifts
# def decrypt(encrypted_text, shifts):
#     decrypted_text = "" # To store the decrypted data
#     # Using for loop to change position of alphabets according to the shifts
#     for letters in encrypted_text:
#         # Current position of alphabet in the list
#         position = alphabets.index(letters)
        
#         # Modified position
#         mod_Position = position - shifts
        
#         # Assigining the new alphabet according to the modified postion
#         new_Letter = alphabets[mod_Position]
        
#         # Assigining new letter to the decrypted text at each iteration
#         decrypted_text += new_Letter
     
#     # Print out
#     print(f"Decrypted Text : {decrypted_text}")
    
    
# Creating a combine function named caesar that encrypts as well as decrypts
def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		#TODO-3: What happens if the user enters a number/symbol/space?
		#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
		#e.g. start_text = "meet me at 3"
		#end_text = "•••• •• •• 3"
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f"Here's the {cipher_direction}d result: {end_text}")