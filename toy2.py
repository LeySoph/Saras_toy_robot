#import regular expressions
import re

location = [-1, -1, "UNPLACED"]


def move_robot( x, y, direction):
		
	
	if direction == "NORTH":
		if y < 4:
			y = y+1
	#		location[1] = location[1] + 1
	elif direction == "SOUTH":
		if y > 0:
			y = y-1
	#		location[1] = location[1] - 1
	elif direction == "EAST":
		if x < 4:
			x = x+1
	#		location[0] = location[0] + 1
	elif direction =="WEST":
		if x > 0:
			x = x-1
	#		location[0] = location[0] - 1
	else:
		print("you are completely lost, which way are you going 1?")
		
	
	#location = [x2, y2, direction]
	location[0] = x
	location[1] = y
	# print (location)
	# print("x", x)
	# print("y", y)


def turn_robot(direction, turn):
		
	if direction == "NORTH":
			if turn == "LEFT":
				direction = "WEST"
			elif turn == "RIGHT":
				direction = "EAST"
			else:
				print(" no change in direction 1")
	elif direction == "SOUTH":
			if turn == "LEFT":
				direction = "EAST"
			elif turn == "RIGHT":
				direction = "WEST"
			else:
				print(" no change in direction 2")			
	elif direction == "EAST":
			if turn == "LEFT":
				direction = "NORTH"
			elif turn == "RIGHT":
				direction = "SOUTH"
			else:
				print(" no change in direction 3")
	elif direction == "WEST":
			if turn == "LEFT":
				direction = "SOUTH"
			elif turn == "RIGHT":
				direction = "NORTH"
			else:
				print(" no change in direction 4")
	else:
		print("you are completely lost, which way are you going 2?")
	
	location[2] = direction
	# print ("direction", direction)


  
exitloop = False


placed = False

file = open('robotcommands.txt','r')


content=file.readlines()
# debug line to see text strings in lines
# print(content)
file.close()

# remove new line characters from lines in text file
# input_text1 = content[5].rstrip("\n")

  
# while  (exitloop == False):
for i in range(0,len(content)):
	#print("enter string for test")
	
	# input_text1 = input( "enter robot commands\n")
	input_text1 = content[i].rstrip("\n")
	
	# convert input text to upper case for easier comparison
	input_text1 = input_text1.upper() 

	# repeat/echo input text for debug 
	print (input_text1)
	
	
	#	Example Input and Output:
	#	a)
	#	PLACE 0,0,NORTH
	#	MOVE
	#	REPORT
	#	Output: 0,1,NORTH
	#	
	#	b)
	#	PLACE 0,0,NORTH
	#	LEFT
	#	REPORT
	#	Output: 0,0,WEST
	#	
	#	c)
	#	PLACE 1,2,EAST
	#	MOVE
	#	MOVE
	#	LEFT
	#	MOVE
	#	REPORT
	#	Output: 3,3,NORTH
	
	
	findplace = re.search("^PLACE", input_text1) 
	if findplace:
		# print("test Search successful.")
		coordinates = input_text1.split(",")
		# print(coordinates)
		stripped_coord = input_text1.strip("PLACE ")
		# print(stripped_coord)
		coordinates =stripped_coord.split(",")
		#print coordinates for debut
		# print(coordinates)
		x = int(coordinates[0])
		y = int(coordinates[1])
		
		# convert the text coordinates to an integer for the array
		coordinates[0] = int(coordinates[0])
		coordinates[1] = int(coordinates[1])
		
		# check to make sure the placement is valid and do nothing if off the board
		if ((x <= 4) and (y<=4) and (x >= 0) and (y>=0) and
			(coordinates[2] == "NORTH" or coordinates[2] == "SOUTH" or coordinates[2] == "EAST" or coordinates[2] == "WEST")): 
			location[0] = x
			location[1] = y
			location[2] = coordinates[2]
			# enable other commands to be used once place has been done
			placed = True
			# print("x", x)
			# print("y", y)
			# print(coordinates)
			# move_robot(coordinates[0],coordinates[1],coordinates[2])
		
		
	else:
		# print("test Search unsuccessful.")	
		#do nothing (pass does nothing but fills a line)
		pass	
	
	findmove = re.search("^MOVE", input_text1)
	if findmove:
		# print("test Search for move successful.")
		if placed == True :
			move_robot(location[0],location[1],location[2])
	else:
		# print("test Search for move unsuccessful.")
		#do nothing (pass does nothing but fills a line)
		pass	
	
	findleft = re.search("^LEFT", input_text1)
	if findleft:
		#print("test Search for left successful.")
		if placed == True :
			turn_robot(location[2], "LEFT")
	else:
		#print("test Search for left unsuccessful.")  
		#do nothing (pass does nothing but fills a line
		pass
	
	findright = re.search("^RIGHT", input_text1)
	if findright:
		# print("test Search for right successful.")
		if placed == True :
			turn_robot(location[2], "RIGHT")
	else:
		# print("test Search for right unsuccessful.")
		#do nothing (pass does nothing but fills a line
		pass
	
	findreport = re.search("^REPORT", input_text1)
	if findreport:
		#print("test Search for report successful.")
		# print output and concatenate the location data into text strings
		print("OUTPUT:", str(location[0]) + "," + str(location[1]) + "," + location[2] )
	else:
		#print("test Search for report unsuccessful.")
		#do nothing (pass does nothing but fills a line
		pass		
	
	
	# findexit = re.search("^EXIT", input_text1) 
	# if findexit:
		# print("test Search for exit loop successful.\n")
		# exitloop = True
	# else:
		# # print("test Search for exit loop unsuccessful.\n")	
		# exitloop = False
		# #do nothing (pass does nothing but fills a line)
		# pass
	
  
  
  
  
  
  
  
  
  
  
  
  
  
   