import requests
import json
variable=requests.get('http://saral.navgurukul.org/api/courses')
var=variable.text
D=json.loads(var)
id_list=[]
num=1
for c in D:
	for i in D[c]:
		for j in i:
			if j=='name':
				print(num,'.',i[j])
				num+=1
			elif j=='id':
				id_list.append(i[j])
chose_cource=int(input('  ENTER ANY COURCE NUMBER :'))
user_id=id_list[chose_cource-1]
variable_id=requests.get(f'http://saral.navgurukul.org/api/courses/{user_id}/exercises')
vard=variable_id.text
data=json.loads(vard)
num=1
list=[]
subject=[]
for e in data:
	for xx in data[e]:
		for exercise in xx:
			if exercise=='name':
				print(num,'.',xx[exercise])
				list.append(xx[exercise])
				num+=1
			elif exercise=='slug':
				subject.append(xx[exercise])
choose=int(input(' ENTER EXERCISE YOU WANT TO PRACITICE NUMBER :'))
user=subject[choose-1]
able=requests.get(f'http://saral.navgurukul.org/api/courses/{user_id}/exercise/getBySlug?slug={user}')
var_slug=able.text
slug_file=open('Data.json','w')
slug_file.write(var_slug)
slug_file.close()
slugfile=open('Data.json','r')
slug_data=json.load(slugfile)
slugfile.close()
for CONTENT in slug_data:
	if CONTENT=='content':
		print(slug_data[CONTENT])



