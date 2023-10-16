import pandas as pd
import openpyxl

#Reading data from an Excel file
def read_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        return None

#Writing data to an excel file
def write_excel(file_path, data):
    data.to_excel(file_path, index=False)

if __name__ == "__main__":
    #Read data from an existing Excel file
    input_file_path = "SAP_ABAP_Bootcamp.xlsx"
    read_data = read_excel(input_file_path)

    if read_data is not None:
        print("Data from Excel file:")
        print(read_data)

        #Write new data as a pandas DataFrame
        new_data = pd.DataFrame({
            "Day 6": ["Generating PDF in Smartforms"]}
        )

        #Write data to a new Excel file
        output_file_path = "Output.xlsx"
        write_excel(output_file_path, new_data)
        print(f"Data written to {output_file_path}")

    else:
        print(f"File {input_file_path} not found")
