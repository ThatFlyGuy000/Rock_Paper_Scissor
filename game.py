import random
option=['Rock','Paper','Scissor']
computer=random.choice(option)
Player_score=0
Comp_score=0
Player=False

while True:
	Player=str(input())
	

	##Logic
	if(Player==computer):
		print('Tie')

	elif(Player=='Rock'):
		
		if(computer=='Paper'):
			print('Round Lost',computer,'Covers',Player)
			Comp_score+=1

		else:
			print('Round Won',Player,'Destroys',computer)
			Player_score+=1

	elif(Player=='Paper'):
		
		if(computer=='Scissor'):
			print("Round Lost",computer,'Cuts',Player)
			Comp_score+=1
		
		else:
			print("Round Won",Player,"Covers",computer)
			Player_score+=1	

	elif(Player=='Scissor'):

		if(computer=='Rock'):
			print('Round Lost',computer,'Smashes',Player)

		else:
			print('Round Won',Player,"Cuts",computer)
			Player_score+=1

	elif Player=='End':
		print("Here are Your Final Scores")
		print("Player_score:",Player_score)
		print("Comp_score:",Comp_score)

		break			




				