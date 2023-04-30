
# Hw1

# Question2

class Solution(object):
    
    # Ages 10 and below, are charged $10 per ticket
    # Ages 11-59, are charged $30 per ticket
    # Ages 60 and above, are charged $20 per ticket 
    
    def movieTickets(self, age, amount_of_tickets):
        total = 0
        if age <= 10:
            total = 10 * amount_of_tickets
        elif age > 10 and age <= 59:
            total = 30 * amount_of_tickets
        else:
            total = 20 * amount_of_tickets
        
        
        return total
    
    #  wordlen() takes a list of strings and prints out the length of each strins line by line
    # if any of the string in the list is empty it doesn't print
    
    def wordLen(self, word_list):
        
        if len(word_list) == 0:
            print("This list is empty!")
        else:
            for x in word_list:
                if len(x) != 0:
                    print(len(x))
        

test = Solution()
# print(test.movieTickets(79,4))
lst1 = ["Hello", "Python", "Mushi", "Flexi", "Java"]
lst2 = ["JavaScript", "", "Ruby", "R"]
lst3 = []
test.wordLen(lst3)