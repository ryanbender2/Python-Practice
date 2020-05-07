from argparse import ArgumentParser
from random import randint
from random import choice
from csv import reader
from requests import post
import string

parser = ArgumentParser(description="Send a scammer's database a happy surprise. :)")
parser.add_argument('url', metavar='url', type=str, help='database to send post requests to')
parser.add_argument('username', metavar='username_identifer', type=str, help='username identifer for post request')
parser.add_argument('password', metavar='password_identifer', type=str, help='password identifer for post request')
parser.add_argument("-c", "--count", metavar='100', help="number of post requests to make (default: 100)", type=int)
args = parser.parse_args()

url = args.url
username_identifer = args.username
password_identifer = args.password
count = args.count if args.count else 100

names = [(i[0], i[1]) for i in reader(open('names.csv', 'r'))]
first_names = [name[0] for name in names]
last_names = [name[1] for name in names]
email_hosts = [
    'gmail',
    'yahoo',
    'aol',
    'hotmail',
    'amazon',
    'mozilla',
]


def gen_username():
    global first_names
    global last_names
    global email_hosts

    number = ''.join([str(randint(0, 9)) for _ in range(2)])
    u_name = "{}{}{}@{}.com" \
        .format(choice(first_names),
                choice(last_names),
                number,
                choice(email_hosts))
    return u_name


def gen_password():
    characters = string.ascii_letters + string.digits
    password =  "".join(choice(characters) for _ in range(randint(8, 16)))
    return password

print("Attacking %s" % url)
for _ in range(count):
    form_data = {
        username_identifer: gen_username(),
        password_identifer: gen_password()
    }
    post_req = post(url, data=form_data)
    status_c = post_req.status_code
    results = "%s: %s, %s" % (str(status_c),
                              form_data[username_identifer],
                              form_data[password_identifer])
    print(results)