import sys
import csv
import sre_yield
import re


def metadosi_periorismwn(eisagomeni_le3i,staurole3o,grammi):
    diaforetika_grammata=''.join(set(eisagomeni_le3i))
    for k in range(2,len(grammi),2):
        le3i=staurole3o[grammi[k]][1]
        if "." in le3i or "]" in le3i:
            le3i_me_periorismous=""
            le3i=list(le3i)
            le3i[grammi[k+1]]= "["+diaforetika_grammata+"]"
            for m in le3i:
                le3i_me_periorismous+=m
            staurole3o[grammi[k]][1]=le3i_me_periorismous
    return staurole3o


def logos_gnwstwn_pros_mege8os_le3ewn(staurole3o,mege8os_le3ewn): 
    plh8os_periorismwn=[0 for k in range(0,len(staurole3o))]
    for k in range(0,len(staurole3o)):
        if "]" in staurole3o[k][1]: 
            plh8os_periorismwn[k]=staurole3o[k][1].count("]")
    megaluteros_logos=0
    for k in range(0,len(plh8os_periorismwn)):
        logos=plh8os_periorismwn[k]/mege8os_le3ewn[k]
        if logos>megaluteros_logos:
            megaluteros_logos=logos
            megaluteros_logos_8esi=k
    return megaluteros_logos_8esi


def sumplirwse_staurole3o(staurole3o,mege8os_le3ewn,pi8anes_le3eis,dokimasmena_kanoniki_ekfrasi): 
    global gemato_staurole3o
    if len(dokimasmena_kanoniki_ekfrasi)>=len(staurole3o): 
        gemato_staurole3o=1
        for grammi in staurole3o:
            for k in range(0,len(pi8anes_le3eis)):
                for le3i in pi8anes_le3eis[k]:
                    if le3i==grammi[1]:
                        print(grammi[0],kanoniki_ekfrasi_list[k][0],grammi[1])   
    if gemato_staurole3o!=1:
        grammi_epilegmenis_le3is=logos_gnwstwn_pros_mege8os_le3ewn(staurole3o,mege8os_le3ewn)
        current_kanoniki_ekfrasi=re.compile(staurole3o[grammi_epilegmenis_le3is][1]) 
        for k in range(0,len(pi8anes_le3eis)):
            if k not in dokimasmena_kanoniki_ekfrasi:
                for le3i in pi8anes_le3eis[k]:
                    if current_kanoniki_ekfrasi.match(le3i) and len(le3i)==mege8os_le3ewn[grammi_epilegmenis_le3is]:    
                        proigoumeni_katastasi=[]
                        for grammi in staurole3o:
                            endiamesa=[]
                            for kommati in grammi:
                                endiamesa.append(kommati)
                            proigoumeni_katastasi.append(endiamesa)
                        previous_dokimasmena_kanoniki_ekfrasi=[kanoniki_ekfrasi for kanoniki_ekfrasi in dokimasmena_kanoniki_ekfrasi]
                        dokimasmena_kanoniki_ekfrasi.append(k)
                        staurole3o[grammi_epilegmenis_le3is][1]=le3i 
                        staurole3o=metadosi_periorismwn(le3i,staurole3o,staurole3o[grammi_epilegmenis_le3is])
                        sumplirwse_staurole3o(staurole3o,mege8os_le3ewn,pi8anes_le3eis,dokimasmena_kanoniki_ekfrasi)
                        dokimasmena_kanoniki_ekfrasi=previous_dokimasmena_kanoniki_ekfrasi
                        staurole3o=proigoumeni_katastasi
     

onoma_staurole3ou=sys.argv[1]
kanoniki_ekfrasi_file_name=sys.argv[2]
kanoniki_ekfrasi_list=[]
with open(kanoniki_ekfrasi_file_name) as kanoniki_ekfrasi_file:
    csvreader = csv.reader(kanoniki_ekfrasi_file, delimiter=',') #isws na min 8elei delimeter
    for grammi in csvreader:
        kanoniki_ekfrasi_list.append(grammi)

staurole3o=[]
with open(onoma_staurole3ou) as arxeio_staurole3ou:
    csvreader = csv.reader(arxeio_staurole3ou) #isws na min 8elei delimeter
    for grammi in csvreader:
        staurole3o.append(grammi)

pi8anes_le3eis=[]
for pattern in kanoniki_ekfrasi_list:
    pi8anes_le3eis.append(set(sre_yield.AllStrings(pattern[0],max_count=5))) #set=monadikes

for k in range(0,len(staurole3o)):
    for m in range(0,len(staurole3o[k])):
        if staurole3o[k][m].isdigit():
            staurole3o[k][m]=int(staurole3o[k][m])

staurole3o.sort()
mege8os_le3ewn=[len(grammi[1]) for grammi in staurole3o]
gemato_staurole3o=0

for k in range(0,len(staurole3o)):
    if "." not in staurole3o[k][1]:
        le3i=staurole3o[k][1]
        grammi_le3is=staurole3o[k]

dokimasmena_kanoniki_ekfrasi=[]
current_kanoniki_ekfrasi=re.compile(grammi_le3is[1])
for k in range(0,len(pi8anes_le3eis)):
    if k not in dokimasmena_kanoniki_ekfrasi:
        for m in pi8anes_le3eis[k]:
                if current_kanoniki_ekfrasi.match(m):
                    dokimasmena_kanoniki_ekfrasi.append(k)

staurole3o=metadosi_periorismwn(le3i,staurole3o,grammi_le3is)
sumplirwse_staurole3o(staurole3o,mege8os_le3ewn,pi8anes_le3eis,dokimasmena_kanoniki_ekfrasi)
