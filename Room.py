import csv as csv

class Room:
	rooms = []

	def __init__(self, campus, region, bldg, ac, stname, capacity, roomnum, sqft, roomtype, subfree):
		"""Creates a room object."""
		# campus: Pomona, ...
		# region: North, South
		# bldg: Dorm building
		# ac: boolean
		# suitename
		# roomnum: room number
		# sqft: square footage of room
		# roomtype: single, double1, double2
		# subfree: boolean
		self.campus = campus
		self.region = region
		self.bldg = bldg
		self.ac = ac
		self.stname = stname
		self.capacity = capacity
		self.roomnum = roomnum
		self.sqft = sqft
		self.roomtype = roomtype
		self.subfree = subfree
		Room.rooms.append(self)

	def __str__(self):
		return "campus: %s, region: %s, bldg: %s, ac: %s, stname: %s, capacity: %s, roomnum: %s, sqft: %s, roomtype: %s, subfree: %s" % (self.campus, self.region, self.bldg, self.ac, self.stname, self.capacity, self.roomnum, self.sqft, self.roomtype, self.subfree)

	def __repr__(self):
		return "campus: %s, region: %s, bldg: %s, ac: %s, stname: %s, capacity: %s, roomnum: %s, sqft: %s, roomtype: %s, subfree: %s" % (self.campus, self.region, self.bldg, self.ac, self.stname, self.capacity, self.roomnum, self.sqft, self.roomtype, self.subfree)


def getCapacity(input, roomarray = Room.rooms):
    """returns all rooms in suites of a given capacity"""
    output = []
    for room in roomarray:
    	if room.capacity == input:
    		output.append(room)
    return output

def getRegion(inpcam, inpreg, roomarray = Room.rooms):
	"""returns all rooms on a given region of a given campus"""
	output = []
	for room in roomarray:
		if room.campus == inpcam & room.region == inpreg:
			output.append(room)
	return output

def getRoom(inpbldg, inpnum, roomarray = Room.rooms):
	output = []
	for room in roomarray:
		if room.bldg == inpbldg & room.roomnum == inpnum:
			output.append(room)
	return output


def getSuite(inpsuite, roomarray = Room.rooms):
	output = []
	for room in roomarray:
		if room.stname == inpsuite:
			output.append(room)
	return output


def main():

	ifile  = open('harwood_rooms.csv', "rU")
	reader = csv.reader(ifile, dialect=csv.excel)

	rownum = 0
	for row in reader:
	    # Save header row.
	    if rownum == 0:
	        header = row
	    else:
	    	Room(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
	    	#print row[0]
	        #colnum = 0
	        #for col in row:
	        #    print '%-8s: %s' % (header[colnum], col)
	        #    colnum += 1
	            
	    rownum += 1

	ifile.close()

def main2():

	with open("harwood_rooms.csv", "rU") as roomdata:
		reader = csv.reader(roomdata)
		for line in reader:
			print line
		for line in reader:
			campus = line[0] 
			region = line[1] 
			bldg = line[2]  
			ac = line[3] 
			stname = line[4] 
			capacity = line[5]  
			roomnum = line[6] 
			sqft = line[7] 
			roomtype = line[8]  
			subfree = line[9] 
			Room(campus, region, bldg, ac, stname, capacity, roomnum, sqft, roomtype, subfree)

			

	roomdata.close()


# Sample code entered in terminal
# main()
# fours = getCapacity("4")
# fours 
# getSuite("0A", fours)

