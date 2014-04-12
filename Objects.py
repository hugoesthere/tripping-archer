# Objects.py

# Room types: single, one-room double, two room double
# Suite types: 3-6 person suites available
# Buildings available


# Suite object comprised of Room objects
# Suite object:
	# Number of people
	# boolean subfree variable
	# two special suites that must be same gender
	# Room draw numbers that have lived in room in the past
# Room object:
	# Square footage
	# type of room (sing, one/two room double)
	# room draw numbers that have lived in room before
	
# Object hierarchy:
# School -> Campus -> Building -> Suite -> Room

class Campus :
	"""An object for an entire school:
	   ex: Pomona, Mudd, Pitzer"""
	# School Name
	def __init__(self, schoolname):
		self.campus = schoolname

	def getCampus():
		return campus

	def __str__(self): 
		return "%s" % (self.campus)

class Region(Campus):
	"""An object for a region of campus:
	   ex: North and South campus for Pomona
	       North, Mid, and South quad for CMC"""
	# Region
	def __init__(self, region):
		self.region = region


	def __str__(self): pass

class Building(Region):
	"""An object for a dorm bulding:
	   ex: Sontag, Lawry, Clark III"""
	# Name 
	# AC
	def __init__(self, bldg, ac = False):
		self.bldg = bldg
		self.ac = ac
	def __str__(self): pass

class Suite(Building):
	"""An object for a specific suite in a bulding
	   ex: Clark III 113-116"""
	# Number of people
	# Suite number/room numbers
	def __init__(self, suitename, capacity):
		self.suitename = suitename
		self.capacity = capacity
	def __str__(self): pass

class Room(Suite):
	"""An object a specific room:
	   ex: Clark III 114"""

	# roomnum - Number
	# sqft - Square footage
	# subfree - Subfree/not subfree
	# type - Room type
	def __init__(self, roomnum, sqft, rmtype, subfree = False):
		self.roomnum = roomnum
		self.sqft = sqft
		self.rmtype = rmtype
		self.subfree = subfree
	def __str__(self): pass


