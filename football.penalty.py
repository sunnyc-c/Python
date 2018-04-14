from random import choice


for i in range(0,5):
    
    score_you = 0
    score_com = 0

    def penalty(pen,score_you,score_com):
    
        if pen == 1:
            action_you = "kick"
            action_com = "save"
            action_first = "Goal!"
            action_second = "Oops!"
        else:
            action_you = "save"
            action_com = "kick"
            action_first = "Saved!"
            action_second = "Oops..."
        
        print("====round %d --- you %s! ====" %(i+1,action_you))

        print ("Choose one side to %s."%(action_you))
        direction = ("left","center","right")
        print ("left, center, right")
        you = input()
        print ("You %sed %s." %(action_you,you))
        com = choice(direction)
        print("Computer %sd %s."%(action_com,com))
        if pen == 1:
            if you != com:
                print(action_first)
                score_you = score_you + 1
            else:
                print(action_second)
           
        else:
            if you == com:
                print(action_first)
            else:
                print(action_second)
                score_com += 1
        print("Score:%d(you)-%d(com)" %(score_you,score_com))

    penalty(1,score_you,score_com)

    penalty(0,score_you,score_com)
