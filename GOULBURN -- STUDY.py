import random
import time


Legislation = ["s.169a-RTA","s.142-RTA","s.175-RTA","s.36-LEPRA","s.76-RTA",
               "s.107-RTA","s.108-RTA","s.109-RTA","s.110-RTA","s.111-RTA",
               "s.112-RTA","cl.4(sh3)-RTA","cl.5(sh3)-RTA","cl.11(sh3)-RTA","cl.13(sh3)-RTA",
               "cl.14(sh3)-RTA","cl.15(sh3)-RTA","cl.12(sh3)-RTA","s.117(1)-RTA","s.117(2)-RTA",
               "s.117(3)-RTA","s.118-RTA","s.51a-CA","s.52a-CA","s.177-RTA",
               "s.224-RTA","s.52a(7)-CA","s.287-RTA","s.4-SOA","s.61H-CA",
               "s.61J-CA","s.43-CYPCPA","s.27-CYPCPA","s.61HA-CA","s.61I-CA"
               "s.61L-CA","s.61N-CA","s.23-CYPCPA","s.4a-SOA","s.5-SOA"
               "s.82-LEPRA","s.83-LEPRA","s.84-LEPRA","s.85-LEPRA","s.86-LEPRA",
               "s.87-LEPRA","s.9-LEPRA","s.10-LEPRA","s.37-CDPVA"]


 
def test():
        Copy = Legislation
        for i in range(len(Legislation)):
            answer = input("Next question? ")
            if answer == "n":
                print("\nExiting")
                break
            else:
                Index = random.randrange(0,len(Copy))
                Question = Copy[Index]
                del Copy[Index]
                print(Question)
                time.sleep(2)
        print("\nThat's all the legislation!")
        time.sleep(10)
        print("Quitting")

print(len(Legislation))
test()
