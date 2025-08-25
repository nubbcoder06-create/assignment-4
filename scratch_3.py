try:
    file1 = open('sample.txt','r')
    reading_file = file1.readlines()
    file1.close()
except FileNotFoundError:
    print('Error: file not found')

except Exception as e:
    print("Something went wrong:",e)

finally:
    print("the contents are:")
    print("Line 1:" , reading_file[0].strip())
    print("Line 2:" , reading_file[1].strip())