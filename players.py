
# # COMBOS GAGNANT
# lign= [(1,2,3), (4,5,6),(7,8,9)]
# column=[(1,4,7), (2,5,8), (3,6,9)]
# diagonal=[(1,5,9), (3,5,7)]

# def find_winner(board):
#     winning = [[lign, column,diagonal]

#     for player in ['X', 'O']:
#         for i, j, k in winning:
#             combo = [board[i], board[j], board[k]]
#             if combo == [player, player, player]:
#                 return player

# #

#DEFINIR LES TOURS


# turn=[1,2,3,4,5,6,7,8,9]

# match turn % 2 :
#   case 1:
#     print(f"{playerX}à toi de jouer !")
#   case 0:
