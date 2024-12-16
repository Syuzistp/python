# import random


# # random barer fayli mijic
# def random_words():
#     with open('random_words.txt','r') as file:
#         words = file.read().split()
#         rand = random.choice(words)
#         return rand


# # marduki kaxvelu hertakanutyuny
# def picture():
#     picture_list = ['''
#        +---+
#            |
#            |
#            |
#           ===''', '''
#        +---+
#        O   |
#            |
#            |
#           ===''', '''
#        +---+
#        O   |
#        |   |
#            |
#           ===''', '''
#        +---+
#        O   |
#       /|   |
#            |
#           ===''', '''
#        +---+
#        O   |
#       /|\  |
#            |
#           ===''', '''
#        +---+
#        O   |
#       /|\  |
#       /    |
#           ===''', '''
#        +---+
#        O   |
#       /|\  |
#       / \  |
#           ===''']
#     return picture_list


# def hangman_game(word):

#     # gushakac tareri list
#     guessed_letters = []

#     # yntrvac bary nerkayis vijaky
#     output = []

#     pict = picture()

#     # bari tesqy
#     for let in word:
#         output.append('*')
    

#     print('initial output', ''.join(output))

    
#     index = -1

#     # te inchqan jamanak bdi ashxati mer kody
#     while(index < 7):

#         index += 1

#         if index == len(pict) - 1:
#             # print kene verji nkary
#             print(pict[6])

#             print('You Lose, the word is: ', word)

#             # krveluc heto break kene
#             break

#         # print enenq hangman-in yst mer erac sxalneri
#         print(pict[index])
        
#         answer = input('Write Letter:' ).upper()

#         # ete mer gushakac tary ka
#         if answer in word:
#             # avelacnenq mer gushakac tareri listin
#             guessed_letters.append(answer)
#              # indexic -1 enenq vorpesi nkary araj chancni u mardu mas chkaxe
#             index -= 1
      
#          # flag unenanq en depqi hamar erb or xaxy khaxtenq
#         flag = True
#         for k, w in enumerate(word):
#             if w not in guessed_letters:

#                 # flagy false sarqenq ete bari tareric voreve meky gushakvac che
#                 flag = False

#              # ete gushakac tary ka bari mej
#             if w == answer:

#                 # poxel output listy gushakvac tarov
#                 output[k] = w
                
#         # tpel bari nerkayis vijaky
#         print('output', ''.join(output))
         
#         # ete xaxacoxy gushakel e bari bolor tarery
#         if flag:
#             print("You Win")
#             # xaxy avartenq 
#             break


# word = random_words().upper()
# hangman_game(word)