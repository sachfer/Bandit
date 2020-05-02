import sshlib
import getpass

host = sys.argv[1]

username = input('Username:')
password = getpass.getpass()
ss = sshlib.Ssh(host)

ss.read_until("login: ")
ss.write(username + "\n")
if password:
    ss.read_until("Password: ")
    ss.write(password + "\n")

ss.write("ls\n")
ss.write("exit\n")

print(ss.read_all())
