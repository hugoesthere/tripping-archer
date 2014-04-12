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

class School :
	"""An object for an entire school:
	   ex: Pomona, Mudd, Pitzer"""
	pass

class Campus :
	"""An object for a region of campus:
	   ex: North and South campus for Pomona
	       North, Mid, and South quad for CMC"""
	pass

class Building :
	"""An object for a dorm bulding:
	   ex: Sontag, Lawry, Clark III"""
	pass

class Suite :
	"""An object for a specific suite in a bulding
	   ex: Clark III 113-116"""
	pass

class Room :
	"""An object a specific room:
	   ex: Clark III 114"""
	pass

