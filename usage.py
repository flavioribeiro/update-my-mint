from Robinhood import Robinhood
import mint

def get_robinhood(login, passwd):
    my_trader = Robinhood()
    logged_in = my_trader.login(login, passwd)
    portfolio = my_trader.portfolios()
    return max(float(portfolio['equity']), float(portfolio['extended_hours_equity']))

def get_coinspring(login, passwd):
    return '200.00'

if __name__ == '__main__':
    mint_login = 'login_here'
    mint_passwd = 'passwd_here'

    my_accounts = {
        'Robinhood': {'callback': get_robinhood, 'login': 'login_here', 'password': 'password_here'},
        'Coinspring': {'callback': get_coinspring, 'login': 'login_here', 'password': 'password_here'}
    }

    mint = mint.Mint(mint_login, mint_passwd)

    for account in mint.get_accounts():
        if my_accounts.has_key(account['name']):
            print('found', account['name'])
            acc = my_accounts[account['name']]
            new_value = acc['callback'](acc['login'], acc['password'])
            print('updating', account['name'], 'with US$', new_value)
            mint.set_property_account_value(account, new_value)

    mint.driver.close()
