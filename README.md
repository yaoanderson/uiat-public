# uiat-public
This is a showing project for one web ui automation testing framework which named "uiat" [https://github.com/yaoanderson/uiat(private)]
![image](https://github.com/yaoanderson/uiat-public/blob/master/uiat.png)

# Background
Currently the great mass of automation testing frameworks have more or less disadvantages in various aspects, for example, 
some of them do not support running testcases parallelly in remote servers, some of them do not support generating test report dynamically but not in the end ... etc.

# Purpose
1. support pure data-drive automation testing.
![image](https://github.com/yaoanderson/uiat-public/blob/master/data_content.png)
![image](https://github.com/yaoanderson/uiat-public/blob/master/data_structure.png)
2. support running testcases parallelly.
3. support running testcases in remote servers and local host.
![image](https://github.com/yaoanderson/uiat-public/blob/master/run_conf.png)
4. support running testcases in docker container.
![image](https://github.com/yaoanderson/uiat-public/blob/master/docker.png)
5. support managing case dispatching dynamically based on environment status.
6. support auto-generate automation testcase based on csv data file without writing any code.
![image](https://github.com/yaoanderson/uiat-public/blob/master/case.png)
7. support adding and updating various drive engine and test engine but not hard code.
8. support generating test report dynamically during testing.
![image](https://github.com/yaoanderson/uiat-public/blob/master/test_reports.png)
...

# Precondition
1. Please prepare docker env if you want to run testcase in remote server
2. Please use another project "atplugin" [https://github.com/yaoanderson/atplugin] to generate csv data file.

# Future
will support other much more advantage requirements from you, please leave message for me :) 
