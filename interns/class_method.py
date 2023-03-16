

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

    @classmethod
    def has_cs_degree(cls, interns_file_path: str):
        with open(interns_file_path, 'r') as interns_file:
            content = interns_file.readlines()

        for record in content:
            intern_name, intern_degree = record.split(r'\t')
            if intern_degree.strip() == 'CS':
                print("before yield")
                yield cls(intern_name, intern_degree)
                print("after yield")


if __name__ == "__main__":
    for intern in Intern.has_cs_degree('interns/interns'):
        print(f'{intern.name}: {intern.degree}')