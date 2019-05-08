first_line = True
with open('example.csv','r') as text_file:
    for line in text_file.readlines():
        value_list = str(line).split(",")
        neighbor= value_list[3]
        hostname= value_list[0]
        interface= value_list[2]
        ip=value_list[1]
        #print(hostname)
        if first_line is False:
            with open(hostname, 'a') as txt_file:
                txt_file.write("-{} interface=\"{}\"\n ip=\"{}\"\n".format(neighbor,interface,ip))
        first_line = False