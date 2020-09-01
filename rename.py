from time import localtime
from time import strftime
import os
import re
import urllib.request
import string
from bs4 import BeautifulSoup

# Settings
log_location = '/home/anders/binaries/rename/log/FileMove.log'

# Take input from terminal session - needs to be run interactively in shell
site = input('URL: ')
file_extension = input('Extension (without . ): ')


def download_data(url):
    response = urllib.request.urlopen(url)
    html = response.read()

    html = str(html)

    return html


def extract_data(data):
    # system variables
    c = 0
    soup = BeautifulSoup(data, "html5lib")
    find_ep_pattern = re.compile(r'S\d+, Ep\d+')

    # return variables
    show = soup.title.text.split(' - Season')[0]
    season_data_dict = dict()

    for episodes in soup.find_all('a'):
        if re.findall(pattern=find_ep_pattern, string=str(episodes)):
            c += 1

            episode_name = episodes.get(r'\ntitle')
            episode_details = re.findall(find_ep_pattern, str(episodes))

            if len(episode_details) > 1:
                raise IndexError

            else:
                episode_details = episode_details[0]

            season_number = int(re.findall('S(\d+)', episode_details)[0])
            episode_number = int(re.findall('Ep(\d+)', episode_details)[0])

            season_data_dict.update({c: {'S': season_number,
                                         'E': episode_number,
                                         'T': episode_name}})

    return season_data_dict, show


def file_operations_and_checks():
    log = []

    for file in os.listdir():
        if file[-len(file_extension):] != file_extension:
            pass

        else:
            season = int(re.findall(r'[Ss](\d+)', file)[0])
            episode = int(re.findall(r'[Ee](\d+)', file)[0])
            show = re.findall(r'(.*)[Ss]\d+', file)[0].replace('.', ' ')

            while show[-1:] == ' ':
                show = show [:len(show) - 1]

            if show.lower() != extract_show.lower():
                raise NameError('{0}: does not match show name from IMDb ({1})'.format(file, extract_show))

            for dicts in extract_dict:
                if extract_dict[dicts]['S'] == season and extract_dict[dicts]['E'] == episode:
                    new_file = '{0} S{1}E{2} - {3}.{4}'.format(extract_show,
                                                               number_conv(season),
                                                               number_conv(episode),
                                                               extract_dict[dicts]['T'],
                                                               file_extension)
                    break

            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

            for chars in new_file:
                if chars not in valid_chars:
                    new_file = new_file.replace(chars, '')

            print('Old file_name: {0}\nNew file_name: {1}\n'.format(file,
                                                                    new_file))

            log.append('{0} - Old file_name: {1} New file_name: {2}'.format(strftime('%d-%m-%Y %H:%M', localtime()),
                                                                            file,
                                                                            new_file))
            os.rename(file, new_file)

    return log


def number_conv(n):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)


extract_dict, extract_show = extract_data(download_data(site))


log_file = open(log_location, 'a')

for log_entry in file_operations_and_checks():
    log_file.writelines(log_entry)
    log_file.writelines('\n')

log_file.close()
