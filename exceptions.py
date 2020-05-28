# try:
#     f=open('simple.txt', 'w')
#     f.write('test write to simple text!')
# except #IOError:
#     print('ERROR: COULD NOT FIND FILE OR READ DATA!')
# else:
#     print('SUCCES!')
#     f.close()

# try:
#     f=open('simple.txt', 'r')
#     f.write('test write to simple text!')
# except IOError:
#     print('ERROR: COULD NOT FIND FILE OR READ DATA!')
# else:
#     print('SUCCES!')
#     f.close()
# print('hello world!')



# f=open('simple.txt', 'r')
# f.write('test write to simple text!')
# print('hello world!')

try:
    f=open('simple.txt', 'r')
    f.write('test write to simple text!')
except IOError:# if don't write IOError not work
    print('ERROR: COULD NOT FIND FILE OR READ DATA!')

finally:
  print('I ALWAYS WORK NO MATTER WHAT!')
