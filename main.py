import os

print("┌────────────────────┐")
print("│ ┌────────────────┐ │")
print("│ │CHAT CLEAR V 1.0│ │")
print("│ └────────────────┘ │")
print("└────────────────────┘")
print("")

def start():
	print("Getting current working directory...")
	dir = os.getcwd()
	if bool(dir) == false:
		print("Could not get current directory!")
	else:
		print("Successfully found working directory!")
		print("Directory: "+dir)
		
start()
input()
