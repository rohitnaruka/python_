# import csv
# import json
# import datetime
# data=[]
# def process_csv(input_path,output_path):
#      with open("D:\GitHub\python_/new 1 - Copy.txt/output_csv_file.csv", mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             # print(row)
#             row["size"]=len(row['name'])
#             row['datetime']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             data.append(row)
#
#             current_datetime= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#             output_path=f"D:\GitHub\python_/new 1 - Copy.txt/output_json_file_{current_datetime}.json"
#             with open(output_path,'w') as json_file:
#                 json.dump(data,json_file,indent=2)
# print(process_csv(input_path="D:\GitHub\python_/new 1 - Copy.txt/output_csv_path.csv",output_path=f"D:\GitHub\python_/new 1 - Copy.txt/output_json_file))

# import csv
# import datetime
# data=[]
# def process_csv(input_path):
#     with open("D:\GitHub\python_\csv.txt", mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#
#             row['size'] = len(row[list(row.keys())[0]])
#
#             row['datetime']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             data.append(row)
#         return data
#         # print(data)
# print(process_csv(input_path="D:\GitHub\python_\csv.txt"))
#














#
# import csv
# import json
# def process_csv_json(input_path,output_path):
#     data = []
#     with open("D:\GitHub\python_/new 1.txt",  mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             # print(row)
#             row['size'] = len(row[list(row.keys())[0]])
#             data.append(row)
#     json_path=input_path.replace('.csv_path','_processed.json')
#     with open("D:\GitHub\python_/new 1.txt",'w') as json_file:
#         json.dump(data,json_file,indent=2)
#         return data
#         # print(data)
# result=process_csv_json(input_path="D:\GitHub\python_/new 1.txt",output_path="D:\GitHub\python_/new 1.txt")
# print(result)


#
#
# import csv
# import json
# import datetime
# def process_csv_json(input_path,output_path):
#     data = []
#     with open(r"D:\c_vmou\new 1.txt",  mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             # print(row)
#             row['size'] = len(row[list(row.keys())[0]])
#             data.append(row)
#     current_datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     data.append({"timestamp":current_datetime})
#     json_path=input_path.replace('.csv_path','_processed.json')
#     with open("D:\c_vmou\JSON.FILE",'w') as json_file:
#         json.dump(data,json_file,indent=2)
#         return data
#         # print(data)
# result=process_csv_json(input_path="D:\c_vmou/new 1.txt",output_path="D:\c_vmou\JSON.FILE")
# print(result)
# # #
# #
# #
# #
# import csv
# import json
# import datetime
# def process_csv_json(input_path,output_path):
#     data = []
#     with open(r"D:\c_vmou\new 1.txt",  mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             # print(row)
#             row['size'] = len(row[list(row.keys())[0]])
#             data.append(row)
#             current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             data.append({"timestamp":current_datetime})
#
#     json_path=input_path.replace('.csv_path','_processed.json')
#     with open("D:\c_vmou/new 1.txt",'w') as json_file:
#         json.dump(data,json_file,indent=2)
#         return data
#         # print(data)
# result=process_csv_json(input_path="D:\c_vmou\new 1.txt",output_path="D:\c_vmou\new 1.txt")
# print(result)
# # port csv
# # def process_csv(input_file_path):
# data = []
# with open(r"D:\c_vmou\new 1.txt", mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         row['size'] = len(row[list(row.keys())[0]])
#         data.append(row)
#         print(data)
# # input_path = 'r"D:\c_vmou\new 1.txt"'
# # print(input_path)







# import csv
# import json
# input_path="D:\GitHub\python_\new 2.txt"
# output_path="D:\GitHub\python_\new 2.txt"
# data = []
# with open("D:\GitHub\python_/new 2.txt",  mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             row['size'] = len(row[list(row.keys())[0]])
#             data.append(row)
# for row in  data:
#     row['size'] = len(row[list(row.keys())[0]])
# with open("D:\GitHub\python_\new 2.txt",'w') as json_file:
#         json.dump(data,json_file,indent=2)
# print(data)
#










import csv
import json
import datetime
data_list=[]
with open("D:\GitHub\python_\csv file.txt",mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row["size"]=len(row['name'])
        row["datetime"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_list.append(row)
current_datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
output_json_file="D:\GitHub\python_\csv file.txt {current_datetime}.json"
with open(output_json_file,'w') as json_file:
    json.dump(data_list,json_file,indent=2)
print(data_list)


# import csv
# # import json
# def process_csv(input_path,output_path):
#     data=[]
#     with open("D:\GitHub\python_\csv file.txt/output_csv_file.csv file.txt",'r') as csv_file:
#         csv_reader=csv.DictReader(csv_file)
#         for row in csv_reader:
#             data.append(row)
#     for row in data:
#         row['size']=len(row[list(row.keys())[0]])
#         # with open("D:\GitHub\python_\csv file.txt/output_json_file.csv file.txt",'w')as json_file:
#         #     json.dump(data,json_file,indent=2)
# print(process_csv(input_path="D:\GitHub\python_\csv file.txt",output_path="D:\GitHub\python_\output.json"))












