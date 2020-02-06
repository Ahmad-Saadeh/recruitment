def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	print("Welcome to the special recruitment program, please answer the following questions:")
	name = input("What's your name? ")
	cv['name'] = name
	age = input("How old are you? ")
	age = int(age)
	cv['age'] = age
	experience = input("How many years of experience do you have? ")
	cv['experience'] = experience
	cv['skills'] = []
	print("\n Skills:")
	for index in range(len(skills)):
		print(str(index+1)+". "+skills[index])
	skill = input("\nChoose a skill from above by entering its number: ")
	get_skill = skills[int(skill)-1]
	cv['skills'].append(get_skill)
	skill_2 = input("Choose another skill from above by entering its number: ")
	get_skill_2 = skills[int(skill_2)-1]
	cv['skills'].append(get_skill_2)
	if age > 25 and age < 40:
		if int(experience)> 5:
			if int(skill)==6 or int(skill_2)==6:
				print("You have been accepted, {}.".format(name))
			else:
				print("Sorry! You have been rejected")
	#write your code here

if __name__ == '__main__':
	main()
