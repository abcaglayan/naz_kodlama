f = open("race _ results.txt", "r")
lines = f.readlines()

points = {1:10, 2:8, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1}
racers = {}



for line in lines:
    if line != '***Race***\n':
        racers[line] = 0


for idx in range(len(lines)):
    if lines[idx] == '***Race***\n':
        for idx2 in range(1,8):
            racers[lines[idx+idx2]] += points[idx2]

for racer in racers.keys():
    print(f" {racer}      {racers[racer]}",end=" ")



print(racers)







f.close()