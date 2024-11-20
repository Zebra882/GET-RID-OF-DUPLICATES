student_data={'id1': {'name':['LEON'], 'class':['four'], 'subject':['English','Nepali','Maths']},
'id2': {'name':['ROCKY'], 'class':['four'], 'subject':['English','Nepali','Maths']},
'id3': {'name':['MORTIS'], 'class':['four'], 'subject':['English','Nepali','Maths']}, 
'id4': {'name':['LEON'], 'class':['four'], 'subject':['English','Nepali','Maths']}, 
'id5': {'name':['HASSAN'], 'class':['four'], 'subject':['English','Nepali','Maths']},           
              }
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)