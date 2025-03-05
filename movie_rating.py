from datetime import datetime


def get_menu():
		print('''
			Movie Rating System
			1.Add a movie
			2.Rate a movie 
			3.View Average Ratings
			4.Exit


			''')

def get_movie_title(movie:str):
	if movie == "":
		return 'invalid input'

	return 'valid input'


def get_date(current_date):
	current_date = datetime.now().strftime('%y-%m-%d')


def get_time(time):

	current_time = datetime.now().strftime('%H:%M')




def get_movie_rate(rate):
	if  rate.isdigit() :
		return 'valid input'
	if rate > 0 and rate <= 5:
		return 'valid input'
	return 'invalid input'

def main():
	date = get_date
	time = get_time
	movie_collection = {}
	
	while True:
		get_menu()
		enter_choice = input('enter choice between 1-4: ')
		
		if enter_choice == '1':
			while True:
				enter_title = input('enter movie name: ')
				title = get_movie_title(enter_title)
				if title == 'valid input':
					break
				print('invalid title. please try again: ')

			movie_details = {
				'title': enter_title,
				'date': date,
				'time': time
				}
				 
			movie_collection['inception'] = movie_details
			print('movie',enter_title, 'added')

		elif enter_choice == '2':
			while True:
				movie_to_rate = input('Enter the movie name')
				if movie_to_rate in movie_collection:
					while True:
					
						enter_rate = input('Enter your rating(1-5)')
							rate = get_movie_rate(enter_rate)
							if rate == 'valid input'
								break
							print('invalid rating. please enter a number between(1-5)')
						
							movie_collection[movie_to_rate]['rating'] = enter_ rate
							print('rating added for', movie_to_rate)
				else print('movie not found')



if __name__ == '__main__':
	main()
   




				
			