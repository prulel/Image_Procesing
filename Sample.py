import sys

######################
# FUNCTION DEFINITIONS
######################

def doBrightness(param):
    print("Function doBrightness invoked with param: " + param)
    print("This is TO BE IMPLEMENTED...")

def doContrast(param):
    print("Function doContrast invoked with param: " + param)
    print("This is TO BE IMPLEMENTED...")

# .....

###########################
# HERE THE MAIN PART STARTS
###########################

print("\n\nThis example shows how you can read and handle cmdline params in you app.")
print("Note, that image filename(s) may also be handled in this way.\n\n")

if len(sys.argv) == 1:
    print("No command line parameters given.\n")
    sys.exit()

if len(sys.argv) == 2:
    print("Too few command line parameters given.\n")
    sys.exit()

command = sys.argv[1]
param = sys.argv[2]
# .....

if command == '--brightness':
    doBrightness(param)
elif command == '--contrast':
    doContrast(param)
# .....
else:
    print("Unknown command: " + command)
print("")
