

class Intern:
    def __init__(self, name: str, degree: str):
        self._name = name
        self._degree = degree

    @property
    def name(self):
        return self._name

    @property
    def degree(self):
        return self._degree


if __name__ == "__main__":
    with open('python-lesson-1/interns') as interns_file:
        content = interns_file.readlines()

    for record in content:
        intern_name, intern_degree = record.split(r'\t')
        if intern_degree.strip() == 'CS':
            intern = Intern(intern_name, intern_degree)
            print(f'{intern.name}: {intern.degree}')