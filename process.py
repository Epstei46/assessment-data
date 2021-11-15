log_file = open("um-server-01.txt") # opens the file specified in quatation marks

def sales_reports(log_file): # defines function sales_reports with input (log_file)
    for line in log_file: # iterates through each line in the file opened on line 1
        line = line.rstrip() # strips white space off of each line
        day = line[0:3] # between cursor position 0 and (spaced in) 3, focuses on the characters between those positions = first 3 letter on each line
        if day == "Mon": # if those first 3 letters on each line == "Tue"
            print(line) # then print the entire line

sales_reports(log_file) # this invokes the function outlined above, which while will print each line starting with the 3 characters matching what is specified on line 8.

# Below is extra credit function that prints out all of the melon orders that delivered over 10 melons
def big_orders(log_file):
    for line in log_file:
        line = line.rstrip()
        amount = int(line[16:18])
        if amount > 10:
            print(line)

big_orders(log_file) 