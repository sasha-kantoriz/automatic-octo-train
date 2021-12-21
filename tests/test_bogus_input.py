import pytest
from main import (_read_input, get_minimum, get_maximum, get_sum, get_multiplication)



def test_read_from_file():
    file_name = 'tests/data/input_wrong.data'
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        _read_input(file_name)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
