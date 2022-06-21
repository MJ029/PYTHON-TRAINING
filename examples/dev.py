from collections import OrderedDict
import json


class JSONHandler:

    filter_keys = ["symbol", "shortName", "longName", "address1", "address2", "city",
                   "country", "exchange", "exchangeTimezoneName", "phone"]

    def __init__(self, input_path: str, output_path: str):
        self.input_file_path = input_path
        self.output_file_path = output_path

    def read_json(self):
        try:
            with open(self.input_file_path, "r") as file_stream:
                data_dict = json.load(file_stream)
            return data_dict
        except Exception as e:
            raise e

    def write_json(self, json_data: dict):
        try:
            output_file_path = self.output_file_path.format(json_data["shortName"])
            with open(output_file_path, "w") as file_stream:
                json.dump(json_data, file_stream, indent=4)
        except Exception as e:
            raise e

    def filter_records(self, json_data: dict):
        try:
            return {elem: json_data[elem] for elem in self.filter_keys}
        except Exception as e:
            raise e

    def run_model(self):
        try:
            # Stage - 1: Read Data
            company_info = self.read_json()

            # Stage - 2: Filter Records
            filtered_company = self.filter_records(json_data=company_info)

            # Stage - 3: Write Output
            self.write_json(json_data=filtered_company)
        except Exception as e:
            raise e


if __name__ == "__main__":

    input_path = "D:\\Github\\PYTHON-TRAINING\\dataset\\INFO.json"
    output_path = "D:\\Github\\PYTHON-TRAINING\\dataset\\output\\{}.json"

    handler = JSONHandler(input_path=input_path, output_path=output_path)
    handler.run_model()

    # data_dict = dict()
    # file_path = "D:\\Github\\PYTHON-TRAINING\\dataset\\INFO.json"
    # output_path = "D:\\Github\\PYTHON-TRAINING\\dataset\\output\\{}.json"
    # # Stage - 1: [Reading]
    # with open(file_path, "r") as file_stream:
    #     data_dict = json.load(file_stream)
    #
    # # Stage - 2: Filter
    # filter_keys = ["symbol", "shortName", "longName", "address1", "address2", "city",
    #                "country", "exchange", "exchangeTimezoneName", "phone"]
    # result = {elem: data_dict[elem] for elem in filter_keys}
    #
    # # Stage - 3: File Writing
    # output_file_path = output_path.format(result["shortName"])
    # with open(output_file_path, "w") as file_stream:
    #     json.dump(result, file_stream, indent=4)