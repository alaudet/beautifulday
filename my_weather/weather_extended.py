'''Add the extended forecast'''

def extended_variables(soup):
    '''Get all variable to build the extended forecast'''
    extended_list = []
    x = 0
    for field in range(25):
        add_to_list = soup.select('td')[x].get_text()
        extended_list.append(add_to_list)
        x += 1

    return extended_list


def main(soup):
    '''main function'''
    rlist = extended_variables(soup)
    print('---Extended Forecast---')
    y = 0
    z = 1
    for returns in range(12):
        print('{} - {}'.format(rlist[y], rlist[z]))
        y += 2
        z += 2
