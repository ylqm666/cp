import sys

value = sys.argv
value2 = value[1]
cnt = 0
list_red = "\033[41m"
list_end = "\033[0m"

while True:
    input_cmd = input()
    cnt += 1
    a = input_cmd.find(value2)
    if a == -1:
        continue
    else:
        list_cmd = list(input_cmd)
        b = a + len(value2)
        list_cmd.insert(a,list_red)
        list_cmd.insert(b + 1,list_end)
        result_str = ''.join(list_cmd)
        print("%d: %s" % (cnt,result_str))