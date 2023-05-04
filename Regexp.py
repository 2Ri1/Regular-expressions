from functions import read_file, reorganization_phones, full_names, final_format, write_file

if __name__ == '__main__':
	read_1 = read_file('phonebook_raw.csv')
	change_the_format = reorganization_phones(read_1)
	organize = full_names(change_the_format)
	final_list_format = final_format(organize)
	write_1 = write_file(final_list_format)
	print('Success')