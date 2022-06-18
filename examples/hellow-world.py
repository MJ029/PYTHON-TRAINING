from core.SAMPLE_1 import HelloWorld


if __name__ == "__main__":

    # print("Hello World"
    print("ENTRY")
    handler = HelloWorld("Surya")
    print("OBJECT CREATED")
    handler.print_info()
    print("FIRST METHOD PASS")
    handler.updated_info("Bhaie")
    print("SECOND METHOD PASS")