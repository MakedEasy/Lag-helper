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
	if bool(dir) == False:
		print("Could not get current directory!")
	else:
		print("Successfully found working directory!")
		print("Directory: "+dir)
	print("Getting current home directory...")
	homedir = os.environ['HOME']
	if bool(homedir) == False:
		print("Could not get current home directory!")
	else:
		print("Successfully found the current home directory!")
		print("Home directory: "+homedir)
		
start()
input()
