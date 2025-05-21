file = open("file.txt","w")
import random as rnd
# student_registeration = file.readlines()
def s_r(ns,nsa):

    classroom= nsa-6
    class_letter = rnd.choice(["A","B","C","D","E","F"])
    class_total = str(classroom) + class_letter
    student_number = rnd.randint(100,200)
    grade = 0
    str_to_add = f"{student_number}, {ns}, {nsa}, {class_total}, {grade} \n"
    file.write(str_to_add)


s_r("naz ç",18)
s_r("a c",18)

file.close()
