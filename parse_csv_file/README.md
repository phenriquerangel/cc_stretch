## Parse CSV file

The CSV file in the files directory contains 4 fields:
* Hostname: the host name of machine
* ip: the ip on the interface to connect with the neighbor
* interface: the network interface name
* neighbor: the machine that this interface permit access

The challenge consists in read the file and for each host name save a file with
the data format above:

```
- neighbor
  interface="interface's name"
  ip="interface's ip"
- neighbor
  interface="interface's name"
  ip="interface's ip"
```

The name of the file must be the hostname with the extension .yml.

![parse_csv.ipynb](https://github.com/kanazux/cc_stretch/blob/master/parse_csv_file/files/parse_csv.ipynb)