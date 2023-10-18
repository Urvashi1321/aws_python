class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, condition):
        #Use a lambda function and list comprehension to filter data based on a condition
        filtered_data = [item for item in self.data if condition(item)]
        return filtered_data

    def transform_data(self, transformation):
        #Use a Lambda function & List comprehension to transform data
        transformed_data = [transformation(item) for item in self.data]
        return transformed_data

    def create_dictionary(self, key_function, value_function):
        #Use dictionary comprehension to create a dictionary from the data
        data_dict = {key_function(item): value_function(item) for item in self.data}
        return data_dict

data = [1,2,3,4,5,6,7]

#Create an instance of the DataProcessor class
processor = DataProcessor(data)

#Example 1: Filter data using lambda function
filtered_data = processor.filter_data(lambda x: x % 2 == 0)
print("Filtered Data:", filtered_data)

#Example 2: Transform data using a lambda function
transformed_data = processor.transform_data(lambda x: x * 2)
print("Transformed Data:", transformed_data)

#Example 3: Create a dictionary using lambda function
key_function = lambda x: f"key_{x}"
value_function = lambda x: x ** 2
data_dict = processor.create_dictionary(key_function, value_function)
print("Dictionary:", data_dict)

