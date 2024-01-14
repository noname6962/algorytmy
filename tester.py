from opt import faults_opt
from lru import faults_lru
from generator_page import page_generation


faults_list_opt, faults_list_lru = [], []
for i in range(2000):

    page_generation()

    input_file = open("dane_page.txt", "r")
    odniesienia = list(map(int, input_file.readline().split()))
    slots = int(input_file.readline())
    input_file.close()

    faults_list_opt.append(int(faults_opt(odniesienia, slots)))
    faults_list_lru.append(int(faults_lru(odniesienia, slots)))

print(f"average faults for lru {sum(faults_list_lru) / len(faults_list_lru)}")
print(f"average faults for opt {sum(faults_list_opt) / len(faults_list_opt)}")
