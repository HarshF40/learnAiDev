# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100,50,25]
# coinsd = {"galleons" : 100, "sickles" : 50, "knuts" : 25}
# ##to pass all the value individually directly
# print(total(*coins), "knuts")
# print(total(**coinsd), "knuts")

def func(*args, **kwargs):
    print("Poitional: ", args)
    print("Name: ",kwargs)
    
func(1,2,3,galleons = 10,sickles = 100,knuts = 190)