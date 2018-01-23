from tkinter import *
import requests
import pprint
root=Tk()
root.title("The Location Detail Tool")
root.geometry("1360x900")
def rot1():
	root1=Tk()
	root1.title("Get the Lattude Longitude and Full Address of the place")
	root1.geometry("810x400")
	def fo1():
		#print("First Name: %s" % (e1.get()))
		URL = "http://maps.googleapis.com/maps/api/geocode/json"
		# location given here
		location = str(e1.get())
		# defining a params dict for the parameters to be sent to the API
		PARAMS = {'address':location}
		# sending get request and saving the response as response object
		r = requests.get(url = URL,params = PARAMS)
		# extracting data in json format
		data = r.json()
		#pprint.pprint (data)
		#print(data.keys())
		# extracting latitude, longitude and formatted address 
		# of the first matching location
		latitude = data['results'][0]['geometry']['location']['lat']
		longitude = data['results'][0]['geometry']['location']['lng']
		formatted_address = data['results'][0]['formatted_address']
		res.configure(text="Latitude ---> %s\nLongitude ---> %s\nFormatted Address --> %s" %(latitude,longitude,formatted_address))
		# printing the output
		#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" %(latitude, longitude,formatted_address))
	l1=Label(root1,text="Enter the Location",height=5,relief=FLAT)
	l1.place(x=0,y=0)
	e1=Entry(root1,bd=5,width=50)
	e1.place(x=150,y=20)
	Button(root1, text='Show', command=fo1).place(x=0,y=50)
	Button(root1,text='Quit',command=root1.destroy).place(x=50,y=50)
	res=Label(root1,relief=RAISED,width=100)
	res.place(x=0,y=100)	
def rot2():
	root2=Tk()
	root2.title("Get the shortest path distance")
	root2.geometry("810x400")
	def fo2():
		URL='https://maps.googleapis.com/maps/api/directions/json?'
		key=''#Place your own API key here for proper execution of this code
		origin=str(e1.get()).replace(' ','+')
		destination=str(e2.get()).replace(' ','+')
		nav_req='origin={}&destination={}&key={}'.format(origin,destination,key)
		request=URL+nav_req
		r=requests.get(request)
		data=r.json()
		#pprint.pprint(data)
		dist=data['routes'][0]['legs'][0]['distance']['text']
		tim=data['routes'][0]['legs'][0]['duration']['text']
		res.configure(text="Approximate Distance ---> %s\nTotal Time to reach Destination ---> %s" %(dist,tim))
	l1=Label(root2,text="Enter the Origin Location",height=5,relief=FLAT)
	l1.place(x=0,y=0)
	e1=Entry(root2,bd=5,width=50)
	e1.place(x=160,y=20)
	l2=Label(root2,text="Enter the Destination",height=5,relief=FLAT)
	l2.place(x=0,y=50)
	e2=Entry(root2,bd=5,width=50)
	e2.place(x=160,y=70)
	Button(root2, text='Show',command=fo2).place(x=0,y=110)
	Button(root2,text='Quit',command=root2.destroy).place(x=60,y=110)
	res=Label(root2,relief=RAISED,width=100)
	res.place(x=0,y=150)
logo=PhotoImage(file="1.png")
l1=Label(root,image=logo,relief=RAISED)
logo1=PhotoImage(file="2.png")
l2=Label(root,image=logo1,relief=RAISED)
l1.place(x=0,y=0)
l2.place(x=650,y=0)
b1=Button(root,text='Click to Find', width=25, command=rot1)
b1.place(x=200,y=610)
b2=Button(root,text='Click to Find',width=25,command=rot2)
b2.place(x=950,y=610)
Button(root,text='Quit',command=root.destroy).place(x=600,y=630)
root.mainloop()
