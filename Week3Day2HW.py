#1.1

# def library_update(books, library):
#     new_books = []
#     for book in books:
#         book_update(book, library, new_books)
#     print(library)
#     return new_books
#
#
# def book_update(books, library, new_books):
#     for book in books:
#         if book not in library:
#             print ('The book, {}, is new!'.format(book))
#             new_books.append(book)
#         library.add(book)

#1.2

# def compute_winner(player_1, player_2):
#     if player_1 == player_2:
#         print ("It's a tie!")
#     elif player_1 == 'r' and player_2 == 's':
#         print('Player 1 wins!')
#     elif player_1 == 'r' and player_2 == 'p':
#         print('Player 2 wins!')
#     elif player_1 == 'p' and player_2 == 'r':
#         print('Player 1 wins!')
#     elif player_1 == 'p' and player_2 == 's':
#         print('Player 2 wins!')
#     elif player_1 == 's' and player_2 == 'r':
#         print('Player 2 wins!')
#     elif player_1 == 's' and player_2 == 'p':
#         print('Player 1 wins!')
#     else:
#         print("Someone didn't play right!")
#
# def play_rock_paper_scissors(n_rounds):
#     for i in range(n_rounds):
#         player_1 = raw_input('Player 1 play (r/p/s): ')
#         player_2 = raw_input('Player 2 play (r/p/s): ')
#         compute_winner(player_1, player_2)
#
# play_rock_paper_scissors(4)

#1.3

def repeat_list_of_file_line(file_name, line_num, num_copies):


    # if not line:
    #     copies_of_line = 'There were not {} lines in the document'.format(line_num)
    # else:

    return copies_of_line

def find_line(file_name, line_num):
    line = None
    with open(file_name) as f:
        for i, file_line in enumerate(f, 1):
            if i == line_num:
                line = file_line.strip()

def copy_line(num_copies):
    find_line(file_name, line_num)
    copies_of_line = [line for _ in range(num_copies)]
    return copies_of_line

copy_line(num_copies)    
