
def get_numbers(input_collection):
    try:
        if isinstance(input_collection, list):
            return input_collection
    except Exception as e:
        raise e


if __name__ == "__main__":

    # Different Types of Creating Numbers

    # Single Variable Creation
    num_a = 100
    print(f"Single Variable Assignment --> {num_a}")

    # Multiple Variable Assignment
    num_b, num_c = 200, 300
    print(f"Multiple Variable Assignment --> {num_b} & {num_c}")

    # Create numbers from list
    # num_list_a, num_list_b, num_list_c = get_numbers([101, 102, 103])
    num_list_a, num_list_b, num_list_c = [101, 102, 103]
    print(f"Create numbers from list --> {num_list_a} & {num_list_b} & {num_list_c}")
