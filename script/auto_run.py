#!/usr/bin/python3
import os
import sys
from os.path import join
from os import makedirs
import math
import multiprocessing as mp
home = "/home/johncreed/"
tmp = join(home, "tmp")
out_path = ""
program_path = join(home, "liblr_test/train")

# reg data
data_path =  join(home, "reg")
command_param = " -s 11 -C -e 0.001"
big_data_list = ['log1p.E2006.train', 'YearPredictionMSD', 'E2006.train'] 
small_data_list = [ f for f in os.listdir(data_path) if f not in big_data_list ]

'''
# clv data
data_path = join(home, clv)
command_param = " -s 0 -C"
data_list = [ f for f in os.listdir(data_path) if f not in big_data_list ]
small_data_list = [
  "news20.binary",
  "rcv1_train.binary",
  "w8a",
  "real-sim",
  "yahoojp",
  "yahookr",
  "url_combined",
  "HIGGS",
  "kdda",
  "kddb",
  # "webspam_wc_normalized_trigram.svm",
]
'''


# Functions 
def go( file ):
    cmd = program_path + command_param + " " + join(data_path, file) + " > "+ join(out_path, file)
    print (cmd)
    os.system(cmd)

train_list = []
def choose_list():
    global train_list
    train_list = input("train big or small (B/S): ")
    if train_list == 'B':
        train_list = big_data_list
    else:
        train_list = small_data_list

def choose_output_folder():
    global out_dir, out_path
    out_dir = input("Which folder to store output: ")
    if out_dir in os.listdir(tmp):
        cmf = input("Replace the elements(y/n) ? ")
        if cmf == 'n':
            sys.exit("Retry Again")
    else:
        makedirs(join(tmp, out_dir))
    out_path = join(tmp, out_dir)
    return

def __main__():
    choose_output_folder()
    choose_list()
    if train_list == big_data_list :
        my_str = ""
        count = 0
        for file in train_list:
            print (file)
            my_str = my_str + str(count) + ":" + file + " "
            count += 1
        print (my_str)
        file = train_list[int(input(my_str))]
        go(file)
    else:
        for file in train_list:
            go(file)


__main__()

