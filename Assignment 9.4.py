name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email]=counts.get(email,0)+1
    
big_count =None
big_email = None
for email,count in counts.items():
    if big_count is None or count > big_count:
        big_email = email
        big_count = count
        
print(big_email,big_count)    
