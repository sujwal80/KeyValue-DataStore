import datetime

def creating_file_name():
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time()).replace(':', '').replace('.', '')
        return date+'-'+time+'.json'


def time_eval():
        date = str(datetime.datetime.now().date()).replace('-', '')
        time = str(datetime.datetime.now().time()).replace(':', '').replace('.', '')
        return int(date+time)
