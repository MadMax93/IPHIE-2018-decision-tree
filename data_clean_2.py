# Remove patients with following dischage codes
# discharge_disposition_id: (11, 13, 14, 19, 20, 21)
discharge_disposition_id = {'11', '13', '14', '19', '20', '21'}
data = open('diabetic_data.csv', 'r')
line1 = data.readline()
output = open('temp1_new.csv','w')
output.write(line1)
for line in data:
    items = line.strip('\n').split(',')
    if items[7] not in discharge_disposition_id:
        output.write(line)
data.close()
output.close()

data1 = open('temp1_new.csv', 'r')
line1 = data1.readline()
pt_encounter = dict()
for line in data1:
    items = line.strip('\n').split(',')
    encounter_id = items[0]
    pt_id = items[1]
    if pt_id not in pt_encounter:
        pt_encounter[pt_id] = encounter_id
    elif int(items[0]) < int(pt_encounter[pt_id]):
        pt_encounter[pt_id] = items[0]
print ('finish part1')
data1.close() 
print (len(pt_encounter))         
        
    
# Recoding "readmitted"
# ">30": 0, NO:  0, "<30" : 1
data2 = open('temp1_new.csv', 'r')
output2 = open('temp2_new.csv', 'w')
line1 = data2.readline()
output2.write(line1.strip('\n') + ',' + 'readmitted_new' + '\n')
for line in data2:
    items = line.strip('\n').split(',')
    if pt_encounter[items[1]] == items[0]:
        if items[49] == '>30':
            readmitted_new = 0
        elif items[49] == 'NO':
            readmitted_new = 0
        else:
            readmitted_new = 1
        output2.write(line.strip('\n') + ',' + str(readmitted_new) + '\n')
data2.close()
output2.close()

## Recoding "diag_1" items[18]
# 1: 390–459, 785
# 2: 460–519, 786
# 3: 520–579, 787
# 4: 250.xx
# 5: 800–999
# 6. 710–739
# 7. 580–629, 788
# 8. 140–239, 780, 781, 784, 790–799, 240–279, without 250, 680–709, 782, 001–139
# 9. 290–319, E–V, 280–289, 320–359, 630–679, 360–389, 740–759


# 
data3 = open ('temp2_new.csv', 'r')
line1 = data3.readline()
output3 = open('temp3_new.csv', 'w')
output3.write(line1.strip('\n') + ','+ 'diag_1_new' + '\n')

import re
for line in data3:
    items = line.strip('\n').split(',')
    if re.match(r'[^E_V].', items[18]):
        diag = float(items[18])
        rules_1 = [diag >= 390 and diag <= 459,diag == 785]
        rules_2 = [diag >= 460 and diag <= 519,diag == 786]
        rules_3 = [diag >= 520 and diag <= 579, diag == 787]
        rules_4 = [diag > 250 and diag < 251]
        rules_5 = [diag >= 800 and diag <= 999]
        rules_6 = [diag >= 710 and diag <= 793]
        rules_7 = [diag >= 580 and diag<= 629, diag == 788]
        rules_8 = [diag >= 140 and diag <= 239, diag == 780, diag == 781, diag == 784, diag >= 790 and diag <= 799,
                   diag >= 240 and diag <= 279, diag != 250, diag >= 680 and diag <= 709, diag == 782, diag >= 1 and diag <= 139]
        rules_9 = [diag >= 290 and diag <= 319, diag >= 289 and diag <= 289, diag >= 320 and diag <= 359, diag >= 630 and diag <= 679,
                   diag >= 360 and diag <= 389, diag >= 740 and diag <= 759]
        if all(rules_1):
            diag_1_new = 1
        elif all(rules_2):
            diag_1_new = 2
        elif all(rules_3):
            diag_1_new = 3
        elif all(rules_4):
            diag_1_new = 4
        elif all(rules_5):
            diag_1_new = 5
        elif all(rules_6):
            diag_1_new = 6
        elif all(rules_7):
            diag_1_new = 7
        elif all(rules_8):
            diag_1_new = 8
        elif all(rules_9):
            diag_1_new = 9
        else:
            diag_1_new = 9
        output3.write(line.strip('\n') + ',' + str(diag_1_new) + '\n')

data3.close()
output3.close()
print ('finish all')            
        
        
    



    
    









            
        
    
    

                            
