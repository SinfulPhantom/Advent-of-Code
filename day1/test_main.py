from main import get_input, calculate_elf_sums, get_greatest_triplet_sum

INPUT_FILE = "input.txt"
EXPECTED_VALUE = 71924

def test_input_file_has_content():
    input_count = get_input(file=INPUT_FILE)
    assert input_count is not None
    
def test_elf_caloric_count_dict_creation():
    test_input = ['10\n', '20\n', '30\n', '\n']
    assert calculate_elf_sums(test_input) == {0: 60}

def test_max_elf_caloric_count():
    input = get_input(file=INPUT_FILE)
    catalog = calculate_elf_sums(input)
    assert max(catalog.values()) == EXPECTED_VALUE

def test_greatest_triplet_sum():
    elf_sums = {
        '0': 100,
        '1': 101,
        '2': 102,
        '3': 103,
        '4': 104,
        '5': 105
    }
    assert get_greatest_triplet_sum(elf_sums) == 312
