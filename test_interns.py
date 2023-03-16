from interns.class_method import Intern


def test_interns__has_cs_degree__get_only_cs_students():
    expected_result = {"Shir", "Tomer", "Nir"}
    result = set()

    for _intern in Intern.has_cs_degree('interns/interns'):
        result.add(_intern.name)


    assert result == expected_result