from pprint import pprint
import re 
import csv

def read_file(file):
	with open(file,'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=",")
		contacts_list = list(reader)
	return contacts_list 

def reorganization_phones(contacts_list):

	pattern = r"(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d*)\s*\(*(\bдоб\b\.)*\s*(\d*)\)*"
	replace = "+7 (\\2) \\3-\\4-\\5 \\6\\7"
	reorganization_number = []

	for contact in contacts_list:
		string_value = ','.join(contact)
		print(string_value)
		clear_string = re.sub(pattern, replace, string_value)
		list_value = clear_string.split(',')
		reorganization_number.append(list_value)
	return reorganization_number

def full_names(reorganization_number):
	new_tab = []
	for element in reorganization_number:
		full_name_list = " ".join(element[0:3]).split()
		if len(full_name_list) !=3:
			full_name_list.append("")
		result = full_name_list + element[3:]
		new_tab.append(result)
	pprint(new_tab)
	return new_tab

def final_format(result_list):
    final_list = list()
    for c in result_list:
        for contact_in_final_list in final_list:
            if contact_in_final_list[:1] == c[:1]:
                final_list.remove(contact_in_final_list)
                c = [x if x != "" else y for x, y in zip(contact_in_final_list, c)]
        final_list.append(c)

    pprint(final_list)
    return final_list

def write_file(new_tab):
    with open("phonebook.csv", "w",encoding='utf-8') as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(new_tab)