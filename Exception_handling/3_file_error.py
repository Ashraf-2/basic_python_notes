import io
file_name = "file.txt"
mode = "r"

try:
    with open(file_name,mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:       # if file does not exist
    print(file_name,"not found.Please check the file name weather correct!")
except io.UnsupportedOperation:     # if the file is not readable file type.
    print("Are you sure?",file_name,"is readable?")
except Exception as e:      # if you can't assume the upcomming error, then show the error as it is.
    print(e)


