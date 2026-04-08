import json
import csv

def json_to_csv(json_data, csv_file_name):
    # Open the CSV file in write mode
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
        
        # Write the header (fieldnames)
        writer.writeheader()
        
    
        writer.writerows(json_data)
    
    print(f"Data successfully written to {csv_file_name}")

if __name__ == "__main__":

    json_data = [
        {"name": "Rupesh", "age": 30, "city": "Delhi"},
        {"name": "OM", "age": 22, "city": "Pune"},
        {"name": "Yogesh", "age": 32, "city": "Mumbai"}
    ]
    
    
    json_to_csv(json_data, "output.csv")