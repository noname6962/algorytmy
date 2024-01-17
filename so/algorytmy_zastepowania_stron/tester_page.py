from opt import faults_opt
from lru import faults_lru
from RandomReplacement import faults_random_replacment
from fifo1 import faults_fifo
from generator_page import page_generation


faults_list_opt, faults_list_lru, faults_list_random_replacment, faults_list_fifo = [], [], [], []
hit_list_opt, hit_list_lru, hit_list_random_replacment, hit_list_fifo = [], [], [], []
faults_opt_value, faults_lru_value, faults_random_replacment_value, faults_fifo_value = 0, 0, 0, 0
hit_opt, hit_lru, hit_random_replacment, hit_fifo = 0, 0, 0, 0

for i in range(100000):
    page_generation()

    input_file = open("dane_page.txt", "r")
    odniesienia = list(map(int, input_file.readline().split()))
    slots = int(input_file.readline())
    input_file.close()

    faults_opt_value, hit_opt = faults_opt(odniesienia, slots)
    faults_lru_value, hit_lru = faults_lru(odniesienia, slots)
    faults_fifo_value, hit_fifo = faults_fifo(odniesienia, slots)
    faults_random_replacment_value, hit_random_replacment = faults_random_replacment(odniesienia, slots)

    faults_list_opt.append(faults_opt_value)
    faults_list_lru.append(faults_lru_value)
    faults_list_fifo.append(faults_fifo_value)
    faults_list_random_replacment.append(faults_random_replacment_value)

    hit_list_opt.append(hit_opt)
    hit_list_lru.append(hit_lru)
    hit_list_fifo.append(hit_fifo)
    hit_list_random_replacment.append(hit_random_replacment)

with open("raport_page_100k.txt", "w") as report_file:
    report_file.write("porownanie wynikow dla 100 000 powtorzen\n\n")
    report_file.write(f"total sum of faults for opt {sum(faults_list_opt)}\n")
    report_file.write(f"total sum of hits for opt {sum(hit_list_opt)}\n")
    report_file.write(f"average faults for opt {sum(faults_list_opt) / len(faults_list_opt)}\n")
    report_file.write(f"hit to faults ratio for opt {sum(hit_list_opt) / sum(faults_list_opt)}\n")
    report_file.write(f"total sum of faults for lru {sum(faults_list_lru)}\n")
    report_file.write(f"total sum of hits for lru {sum(hit_list_lru)}\n")
    report_file.write(f"average faults for lru {sum(faults_list_lru) / len(faults_list_lru)}\n")
    report_file.write(f"hit to faults ratio for lru {sum(hit_list_lru) / sum(faults_list_lru)}\n")
    report_file.write(f"total sum of faults for opt {sum(faults_list_fifo)}\n")
    report_file.write(f"total sum of hits for opt {sum(hit_list_fifo)}\n")
    report_file.write(f"average faults for fifo {sum(faults_list_fifo) / len(faults_list_fifo)}\n")
    report_file.write(f"hit to faults ratio for fifo {sum(hit_list_fifo) / sum(faults_list_fifo)}\n")
    report_file.write(f"average faults for random replacment {sum(faults_list_random_replacment) / len(faults_list_random_replacment)}\n")
    report_file.write(f"hit to faults ratio for random replacment {sum(hit_list_random_replacment) / sum(faults_list_random_replacment)}\n")

print(f"total sum of faults for opt {sum(faults_list_opt)}")
print(f"total sum of hits for opt {sum(hit_list_opt)}")
print(f"average faults for opt {sum(faults_list_opt) / len(faults_list_opt)}")
print(f"hit to faults ratio for opt {sum(hit_list_opt) / sum(faults_list_opt)}")
print(f"total sum of faults for lru {sum(faults_list_lru)}")
print(f"total sum of hits for lru {sum(hit_list_lru)}")
print(f"average faults for lru {sum(faults_list_lru) / len(faults_list_lru)}")
print(f"hit to faults ratio for lru {sum(hit_list_lru) / sum(faults_list_lru)}")
print(f"total sum of faults for fifo {sum(faults_list_fifo)}")
print(f"total sum of hits for fifo {sum(hit_list_fifo)}")
print(f"average faults for fifo {sum(faults_list_fifo) / len(faults_list_fifo)}")
print(f"hit to faults ratio for fifo {sum(hit_list_fifo) / sum(faults_list_fifo)}")
print(f"total sum of hits for random replacment {sum(hit_list_random_replacment)}")
print(f"total sum of faults for random replacment {sum(faults_list_random_replacment)}")
print(f"average faults for random replacment {sum(faults_list_random_replacment) / len(faults_list_random_replacment)}")
print(f"hit to faults ratio for random replacment {sum(hit_list_random_replacment) / sum(faults_list_random_replacment)}")
