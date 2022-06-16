import re
from zipfile import ZipFile


if __name__ == '__main__':

    log_file = "archive1.zip"

    result = 0

    with ZipFile(log_file, 'r') as zip:
        zip.extractall()

    time_regex = r"23/Mar/2009:06:29:[1-5][0-9]|23/Mar/2009:06:[3-5][0-9]:|23/Mar/2009:07:[0-5][0-9]|23/Mar/2009:08:(0[0-9]|1[0-2]|13:([0-2][0-9]|3[0-2]))"
    fail_regex = r"\s[4-6]\d\d\s"

    with open("archive1.txt", 'r') as file:
        for line in file:
            time = re.findall(time_regex, line)
            if time:
                fail = re.findall(fail_regex, line)
                if fail:
                    result += 1
                    print(fail)
    print(result)
