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

	def getCapacity(self, input, roomarray = Room.rooms):
	    """returns all rooms in suites of a given capacity"""
	    output = []
	    for room in roomarray:
	    	if room.capacity == input:
	    		output.append(room)
	    return output

	def getRegion(self, inpcam, inpreg, roomarray = Room.rooms):
		"""returns all rooms on a given region of a given campus"""
		output = []
		for room in roomarray:
			if room.campus == inpcam & room.region == inpreg:
				output.append(room)
		return output

	def getRoom(self, inpbldg, inpnum, roomarray = Room.rooms):
		output = []
		for room in roomarray:
			if room.bldg == inpbldg & room.roomnum == inpnum:
				output.append(room)
		return output

	
	def getSuite(self, inpsuite, roomarray = Room.rooms):
		output = []
		for room in roomarray:
			if room.stname == inpsuite:
				output.append(room)
		return output

