## Pachev FTP Path Traversal POC
Pachev FTP Path Traversal POC ("Welcome to FTP Server Spring 2017")


# Introduction

A simple path traversal proof-of-concept on [PachevFTP](https://github.com/pachev/pachev_ftp),
 the exploit can allow you to enumerate directories and retrieve files within the target machine 

# Usage 

Enumerate and list folders:

```
python3 PachevTraversal.py -i <TargetIP> -p <TargetPort> -l <TargetDirectory>
```

Retrieve a file:

```
python3 PachevTraversal.py -i <TargetIP> -p <TargetPort> -r <TargetFilePath>
```

