# test.py
from fusuk import getname

print("US male:", getname("us", "male"))
print("US female:", getname("us", "female"))
print("UK male:", getname("uk", "male"))
print("UK female:", getname("uk", "female"))

print("UK random:", getname("uk"))
print("US random:", getname("us"))