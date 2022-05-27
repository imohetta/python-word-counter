#a program that opens a text file, finds unique words andshows how many times those words appear in the text.

def read_file_content(file): #opens and reads the file
    file = open(input ("Type the name of the textfile (make sure it is in the same directory as the program): "))
    return file.read()


def count_words(): #function to count the words
    text = read_file_content("")
    
    counts = dict()
    wordlist = text.split() #splits each word and returns an array of words
    
    #loops through the text and checks if the word already exists and updates the number in the "counts" dictionary
    for word in wordlist:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
                   
    return counts

print(count_words()) #prints the dictionary