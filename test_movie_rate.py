import unittest
import movie_rating 

class TestMovieRating(unittest.TestCase):
	def test_that_menu_function_exists(self):
		movie_rating.get_menu()


	def test_that_get_movie_title_exists(self):
		movie_rating.get_movie_title()

	
	def test_that_get_movie_title_return_valid_input(self):
		actual = movie_rating.get_movie_title("rita123")
		result = 'valid input'
		self.assertEqual(actual, result)



	def test_that_get_movie_title_returns_null(self):
		actual = movie_rating.get_movie_title(" ")
		result = 'valid input'
		self.assertEqual(actual, result)

	def test_that_date_fucntion_exist(self):
		movie_rating.get_date()

	def test_that_time_fucntion_exist(self):
		movie_rating.get_time()


	def test_that_get_movie_rate_exist(self):
		movie_rate.get_movie_rate



	def test_that_get_movie_rate_return_valid_input(self):
		actual = movie_rating.get_movie_rate(2)
		result = 'valid input'
		self.assertEqual(actual, result)



	def test_that_get_movie_rate_return_valid_input_1to5(self):
		actual = movie_rating.get_movie_rate(6)
		result = 'invalid input'
		self.assertEqual(actual, result)














if __name__ == '__main__':
    unittest.main() 













