#딕셔너리란
#딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요소값을 구하지 않고,
#Key를 통해 Value를 얻으며 이것이 딕셔너리의 가장 큰 특징임
#{Key1:Value1, Key2:Value2, Key3:Value3 ···}
#Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있음
#각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있음
dic = {'name':'pey','phone':'0119993323','birth':'1118'}
a = {1:'hi'}#Key로 정수값 1, Value로 ‘hi’라는 문자열을 사용함
a = {'a':[1,2,3]}# Value에 리스트도 넣을 수 있음
#딕셔너리 쌍 추가, 삭제하기
#1. 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)#{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
#2. 딕셔너리 요소 삭제하기
del a[1]
print(a)#{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
#딕셔너리를 사용하는 방법
#딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey':10 , 'julliet':9}
print(grade['pey'])
print(grade['julliet'])
a = {1:'a',2:'b'}
print(a[1])
print(a[2])
a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])
#딕셔너리를 만들 때 주의할 사항
a = {1:'a', 1:'b'}
print(a)#{1: 'b'}
#a = {[1, 2]:'hi'} #unhashable type: 'list'

#딕셔너리 관련 함수
#Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())#dict_keys(['name', 'phone', 'birth'])
for k in a.keys():
    print(k)

print(list(a.keys()))
#Value 리스트 만들기(values)
print(a.values())#dict_values(['pey', '0119993323', '1118'])
# Key, Value 쌍 얻기(items)
print(a.items())
#dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

#Key : Value 쌍 모두 지우기(clear)
a.clear()
print(a)#{}
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('nokey'))#None
#print(a['nokey']) #KeyError: 'nokey'
print( a.get('foo', 'bar') )
#딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, ‘디폴트 값‘)을 사용하면 편리함
#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)#True
print('email' in a)#False


