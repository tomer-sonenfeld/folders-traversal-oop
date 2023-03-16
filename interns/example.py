

class Intern:
    def __init__(self, name: str, degree: str):
        self._name = name
        self._degree = degree.strip()

    def __repr__(self):
        return f'Student name: {self._name}, learns {self._degree}'



if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7]
    interns = {'Shir': 'CS', "Sa'ar": 'ISE', 'Tomer': 'CS', 'Nir': 'CS'}
    # result = [2 for number in numbers if number % 2 == 0]
    # result = {key: value for key, value in interns.items() if value == 'CS'}
    # print(result)
