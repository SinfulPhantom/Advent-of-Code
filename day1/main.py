def get_input(file):
    file_input = open(file, 'r')
    input = file_input.readlines()

    return input

def calculate_elf_sums(elf_inputs):
    current_elf = 0
    caloric_sum = 0
    elf_catalog = {}
    
    for input in elf_inputs:
        converted_input = input.strip()
        if converted_input:
            caloric_sum = caloric_sum + int(converted_input)
        else:
            elf_catalog[current_elf] = caloric_sum
            current_elf += 1
            caloric_sum = 0
    
    return elf_catalog

def get_greatest_triplet_sum(catalog):
    catalog_values_list = list(catalog.values())
    catalog_values_list.sort(reverse=True)
    catalog_values_list = catalog_values_list[:3]
    return sum(catalog_values_list)

    
if __name__ == "__main__":
    input = get_input('input.txt')
    elf_catalog = calculate_elf_sums(input)
    
    # Part 1 answer
    print(max(elf_catalog.values()))
    # Part 2 answer
    print(get_greatest_triplet_sum(elf_catalog))
