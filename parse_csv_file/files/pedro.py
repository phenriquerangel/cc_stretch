first_line = True
with open('example.csv','r') as text_file:
    for line in text_file.readlines():
        value_list = str(line).split(",")
        neighbor= value_list[3]
        interface= value_list[2]
        ip=value_list[1]
        #print(neighbor)
        if first_line is False:
            print("-{} interface=\"{}\"\n ip=\"{}\"\n".format(neighbor,interface,ip))
        first_line = False