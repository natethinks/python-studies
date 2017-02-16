if __name__ == '__main__':
	students = []
	for _ in range(int(input())):
		name = input()
		score = float(input())
		student = [name, score]
		students.append(student)
		print(student)
		print(students)
