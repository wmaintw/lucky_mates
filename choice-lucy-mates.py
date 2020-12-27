from numpy import random
import datetime
import pytz

def choice_luck_mates(employee_ids):
    num_of_round = len(employee_ids)
    lucky_mates = [0, 0]
    random.seed()
    
    for i in range(num_of_round):
        lucky_mates = random.choice(employee_ids, size=(2))
        while lucky_mates[0] == lucky_mates[1]:
            lucky_mates = random.choice(employee_ids, size=(2))
    
    return lucky_mates
    

def show_lucky_mates(lucky_mates):
    tz = pytz.timezone('Asia/Shanghai')
    print(datetime.datetime.now(tz))
    print("恭喜第1位中奖小伙伴：{}".format(lucky_mates[0]))
    print("恭喜第2位中奖小伙伴：{}".format(lucky_mates[1]))




#-----------------------------------------------
employee_ids = ["wma", "ylran", "jchen"]

luck_mates = choice_luck_mates(employee_ids)
show_lucky_mates(luck_mates)
