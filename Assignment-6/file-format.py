def file_format(fn):
    fn_lis = fn.split('.')
    return fn_lis[-1]
    
file_name = input('Enter your file name:')
print(f'your file format is: {file_format(file_name)}')