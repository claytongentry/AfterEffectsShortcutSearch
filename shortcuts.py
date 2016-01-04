import csv

COMMANDS_FILE = "commands.csv"

def run():
    key = raw_input("Key: ")
    if key.lower() == "exit":
        return False
    else:

        if key_is_clean(key.lower().strip()):
            results = get_results(key)
            # display_results(results)
        else:
            print "Error: Invalid key."
        return True

def key_is_clean(key):
    f1_arr = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]
    special_arr = ["shift", "command", "control", "delete", "option", "enter", "escape", "tab", "up arrow", "left arrow", "right arrow", "down arrow"]
    if key in f1_arr or key in special_arr or len(key) == 1:
        return True
    else:
        return False

# Gets commands from dataset that include key
def get_results(key):
    with open(COMMANDS_FILE, "r") as f:
        csvreader = csv.reader(f)
        data = []
        formatted_key = format_key(key)
        for row in csvreader:
            if len(row) > 0:
                if formatted_key in row[2].split(" ") or formatted_key in row[2].split("+"):
                    data_tup = (row[2], row[0])
                    data.append(data_tup)
                    print row[2] + ": " + row[0] + "\n"
        if len(data) == 0:
            print "No commands for " + key + " key."
        return data

def format_key(key):
    key_arr = key.split(" ")
    formatted_key_arr = []
    for string in key_arr:
        formatted_key_arr.append(string.capitalize())
    return " ".join(formatted_key_arr)

# Prints results attractively
def display_results(results):
    for result in results:
        print result


if __name__ == "__main__":

    print "\nAFX Keyboard Shortcuts"
    print 'Enter "exit" to quit.\n'

    go = True
    while go:
        go = run()
