import pandas as pd

data1 = pd.read_csv('./sandbox/data/Freight.csv',delimiter=';')
#data2 = pd.read_csv('./sandbox/data/Orders.csv')

df1 = pd.DataFrame(data1)
#df2 = pd.DataFrame(data2)


city_set_1 = set(df1['Departure'])
city_set_2 = set(df1['Arrival'])

city = city_set_1.union(city_set_2)
#print(city_set_1.union(city_set_2))

post=[]

city_post = {}


for i in city_set_1:
	post = list(df1.loc[df1['Departure']==i,'DeparturePostCode'])

	key_value ={i:post[0]}

	city_post.update(key_value)
print(city_post)	

for i in city_set_2:
	post = list(df1.loc[df1['Arrival']==i,'ArrivalPostCode'])

	key_value ={i:post[0]}

	city_post.update(key_value)
print(city_post)
print('Number of all city')
print(len(city_post))

#print(" Freight has depart and arrival, Orders has only arrival")
#sortDepart = df1.sort_values('Departure')

#print('departure city')
sortDepart = df1.groupby(['Departure']).size().sort_values(ascending=False)
#print(sortDepart)

numDepart = df1.groupby(['Departure'])['Departure'].count()
print('Number of Departure Citys')
print(len(df1.groupby(['Departure'])))

#print('\n arrival city')
sortArrival = df1.groupby(['Arrival']).size().sort_values(ascending=False)
#print(sortArrival)
print('Number of Arrival Citys')
print(len(df1.groupby(['Arrival'])))

# All citys

#city = df1.groupby(['Departure','Arrival']).size()
#print('\n All city')
#print(city)





#print("sort by Arrival")
#sortArrival = df1.sort_values('Arrival')
#print(sortArrival)

#print("Freight price relates to the weight and volume")
#sortPrice = df1.sort_values('Price')
#print(sortPrice)

#print("Sort by date")
#sortDate = df2.sort_values('InvoiceDate')
#print(sortDate)


#sortProduct = df2.sort_values('ProductCode')
#print(sortProduct)

#print(" To see which the most popular/needed product")
#sortQuantity = df2.sort_values('Quantity',ascending=False)
#print(sortQuantity)

#print(" Most frequent order customer")
#sortCustomer = 
#df2.groupby(['CustomerCode'])['InvoiceNumber'].size().sort_values(ascending=False)
#print(sortCustomer)

#print(" Main departure city")
#sortCity = df1.groupby(['Departure']).size().sort_values(ascending=False)


#print(sortCity)

