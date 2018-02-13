import ast
import csv
from glob import glob


def merge_text_files(input_file_directory, output_file, header):
    """
    This function will merge all the text files into the output file.

    :param input_file_directory: Directory path which consist of all the state text files
    :param output_file:          It is the resulting merged file of all state text files
    :param header:               Header of the output file
    :return:                     Returns None
    """

    # Create the output file
    with open(output_file, "w") as output:

        # Add the header to the output file
        output.write(header)

        # Loop for all the text files present int the directory
        for text_file in glob(input_file_directory):

            # Read the content of the current text file
            with open(text_file) as file:

                # Write the text file contents into the output file
                output.write(file.read())


def merge_movie_files(input_file_1, input_file_2, output_file):
    movie_dict = {}
    header = ["Movie ID", "Title", "Year", "First_name","Last_name", "Name"]
    write_csv_file(output_file, [header], 'w')

    res = []
    with open(input_file_1, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[3]
            year = row[11]
            title = row[17]

            movie_dict[key] = [key, title, year]

    with open(input_file_2, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[0]
            cast = ast.literal_eval(str(row[2]))
            # print(type(cast),cast)
            for item in cast:
                # print(item)
                name = str(item["name"]).split(" ")
                first_name = name[0]
                last_name = ""
                if len(name) == 2:
                    last_name = name[1]
                entry = movie_dict[key]
                temp = entry + [first_name, last_name, item["name"]]
                res.append(temp)
    write_csv_file(output_file, res, "a+")


def write_csv_file(absolute_file_path, content_list, access_type):
    """
    This function will write post or campaign level metrics to the specified file

    Usage::

        >>> write_csv_file('Absolute_File_Path',[['valid','list'],[]],'a+')

    :param absolute_file_path:  The absolute path of output file
    :param content_list:        The metric list of list
    :param access_type:         It indicates type of access(write, append, etc.)
    :return:                    None

    """
    import csv
    try:
        with open(absolute_file_path, access_type, encoding='utf-8', newline='') as file:
            wr = csv.writer(file)

            for row in content_list:
                wr.writerow(row)

    except Exception as e:
        raise e


def main():
    input_file_directory = "[Directory Path]*.TXT"
    output_file = "all_states_data.csv"
    header = "state,sex,year,name,count\n"
    merge_text_files(input_file_directory, output_file,header)

    input_file_1 = "[Directory Path]\\tmdb_5000_movies.csv"
    input_file_2 = "[Directory Path]tmdb_5000_credits.csv"
    output_file = "movie_data.csv"

    merge_movie_files(input_file_1,input_file_2,output_file)

if __name__ == '__main__':
    main()
