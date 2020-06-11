#this is a borrowed concept from Fendy3d
#and is only for educational purposses

import hashlib

words_file_name="1MillionPasswords.txt" #file name
hashed_words_file_name ="1MillionPasswords_hashed.txt" #output file name
#variables
hash_type="md5"

def create_hash_md5_text_file(input_list, output_file_name,hash_type):
        input_list= list(map(str.strip, input_list)) #strips away the \n
        hashesToExport =[]
        #loops through the output  
        for word in input_list:
            if hash_type == "mdf":
                crypt =hashlib.md5()
            elif hash_type == "sha1":
                crypt =hashlib.sha1()
            crypt.update(bytes(word, encoding='utf-8'))
            hashOfword = crypt.hexdigest()

            hashesToExport .append(hashOfword)

        print("creating hash text file: {}...".format(output_file_name))

        #create the output file
        with open(output_file_name, 'w') as f:
            for hashOfword in hashesToExport:
                f.write("%s\n" % hashOfword)

        print("{} has been succefully created".format(output_file_name))

def get_list_of_words_from_file(filename):
    #opens the file
    print("opening file:{}".format(filename))
    list_of_words =open(filename, 'r', errors='ignore').readlines() 
    print("stripping breakline characters from the file:{}.".format(filename))
    list_of_words= list(map(str.strip, list_of_words))
    return (list_of_words)

#getting words from the file
words_list=get_list_of_words_from_file(words_file_name)

#create the hash
create_hash_md5_text_file(words_list, hashed_words_file_name, hash_type)
