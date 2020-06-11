# This is a partially borrowed concept from fendy3d
import time
import multiprocessing
import math

#create a function "chunk"with i and n:
def chunks(LIST,NUMBER_OF_PARTS):
    for i in range(0, len(LIST),NUMBER_OF_PARTS):
        #create an index range for 1 of n items:
        yield LIST[i:i+NUMBER_OF_PARTS]

hashed_password_file_name ='1Million password_hashed.txt'
hashed_guess_words_file_name ='english_hashed.txt'

no_of_cpu =multiprocessing.cpu_count()

start =time.perf_counter()

####opening the hashed password file####
print("opening file: {}".format(hashed_password_file_name))
hashed_passwords_list =open(hashed_password_file_name, 'r').readlines()
hashed_words_list= list(map(str.strip, hashed_passwords_list)) #strips away all the \n
finish =time.perf_counter()

####opening the hashed guessed words file####
print("opening file :{}". format(hashed_guess_words_file_name))
hashed_words_list =open(hashed_guess_words_file_name, 'r').readlines()
hashed_words_list =list(map(str.strip, hashed_words_list)) #strips away all the \n
finish =time.perf_counter()

####splitting the hashed password file ####
print("this laptop has {0} number of cpus. commencing splitting of password  list into {0} part".format(no_of_cpu))
no_of_elements_in_sublist =math.ceil(len(hashed_passwords_list)/no_of_cpu)
chunks_of_passwords_lists=list(chunks(hashed_passwords_list, no_of_elements_in_sublist))

####start dictionary attack ####
print("start dictionary attack on the {} password lists..".format(len(chunks_of_passwords_lists)))

def crack(hashed_passwords_lists, cpu_number):
    number_of_cracked_password=0
    number_of_passwords_scanned=0

    for hashed_word in hashed_words_list:
        number_of_passwords_scanned += 1
    if hashed_word in hashed_passwords_list:
        number_of_cracked_password += 1
    if number_of_passwords_scanned %1000 == 0:
        finish =time.perf_counter()
        print("cpu{}: {}/{} password has been cracked. {} minutes elapsed.".format(cpu_number, number_of_cracked_password, len(hashed_passwords_list),round((finish-start)/60,2)))



