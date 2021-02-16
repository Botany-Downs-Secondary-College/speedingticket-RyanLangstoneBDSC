#speeding tickit program
#by ryan langstone
import time
wanted_list = ["jef","jhon","lucy","simon"]
penalties = [{"condition": 0, "penalty_statment": "because he is only just over the speedlimit, no penalty will be given", "fine": 0 },
{"condition": 5, "penalty_statment": "because he is speeding he will recieve a $150 fine", "fine": 150},
{"condition": 10, "penalty_statment": "because he is speeding by a big amount he will recieve a $1000 fine", "fine": 1000},
{"condition": 20, "penalty_statment": "because he is dangerosly speeding he will be sent to jail", "fine":"jail"}]
summary = []

def number_input(phrase):
    number = ""
    while number == "":
        try: 
            number = int(input(phrase))
        except:
            print("needs to be a number")
    return  number

def speeder():
    global penalties
    global summary
    fine = penalties[len(penalties)-1]["fine"]
    name = input("what is the speeders name\n")
    if name in wanted_list:
        print(name +" is already wanted for murder charges and has been given the death penalty")
        fine = "death"
    else:
        speed_limit = number_input("what was the speed in the area\n")
        speed = number_input("how fast was " + name + " going\n")

        if speed_limit < speed :
            speed_over = speed - speed_limit
            print(name + " was speeding by "+str(speed_over))
            penalty_number = len(penalties) -1
            for x in range(len(penalties)):
                if speed_over < penalties[x]["condition"]:
                    penalty_number = x-1
                    fine = penalties[x-1]["fine"]
                    break
            try:
                print(penalties[penalty_number]["penalty_statment"])
            except:
                print("you cant add, "+name+" was not speeding")
                time.sleep(1.0)
                print("see ya")
            if penalty_number > 0:
                print(name +" has been apropriattly punished thanks to you, and been put to justice")
        else:
            print("you cant add, "+name+" was not speeding")
            time.sleep(1.0)
            print("see ya")
    dictonary = {"name":name, "fine":fine}
    summary.append(dictonary) 

start = input("do you want to enter a speeder (yes or no)\n")
if start == "yes":
    while start == "yes":
        speeder()
        start = input("do you want to enter another speeder\n")
    print("sumary list...")
    for x in summary:
        
        if isinstance(x["fine"], int):
            print(x["name"] + "has been fined $" + str(x["fine"]))
        else:
            print(x["name"] + "has been sentenced to " + x["fine"])
else:
    print("well then why the hell are you runing this program")
    time.sleep(1.5)
    print("see ya")