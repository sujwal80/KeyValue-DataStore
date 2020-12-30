import os
import datetime
import json
import ast
from new_file_name import creating_file_name, time_eval
import sys

class keyvalue:
    '''init initializes keyvalue modlue and create file if file path is not given
    or file does not exist in given path and fill with empty dictonary'''
    
    def __init__(self, file_dir=None):

        try:
            #If file name is incorrect or it does not exist then program terminate
            if file_dir != None and not os.path.isfile(file_dir):
                raise OSError('OSError: Error Occured during loading file')
            
            if file_dir == None:
                #getting current working directory
                file_dir = os.getcwd()
                
                #creating unique file name in current working directory
                file_dir = os.path.join(file_dir, creating_file_name())

            #print(file_dir)
            self.__file_dir = file_dir
            
            #creating file in current working directory if it is not available
            os.open(self.__file_dir, os.O_CREAT)

            #writing empty dictionary in file if its empty
            if os.path.getsize(self.__file_dir) == 0:
                with open(self.__file_dir, 'w') as json_file:
                    json.dump({}, json_file)

            #storing json object in self.kvalue variable
            with open(self.__file_dir, 'r') as json_file:
                self.__kvalue = json.load(json_file)

        #all type of exception and error occured during initialization are being handeled here and if so program is terminated righ away
        except Exception as exc:
            print(exc)
            sys.exit()

    def Create(self, key, value, TimeToLive=None):

        #time varaible stores current date and time
        time = time_eval()
        
        try:
            #if TimeToLive is not in integer format then KeyError is occured
            if not str(TimeToLive).isnumeric():
                raise TypeError('KeyError:{} TimeToLive must be in int format'.format(TimeToLive))

            #if key is already in self.__kvalue then it will create keyerror for same
            if str(key) in self.__kvalue:
                raise KeyError('KeyError:{} key Already exist'.format(key))

            #if length of key is greater than 32 character then if create overflow error
            if len(str(key)) > 32:
                raise OverflowError('OverflowError: key is not in range of [1, 32]')

            #if file size is greater than or equal to 1gb then it will create overflow error
            if os.path.getsize(self.__file_dir) >= 2**30:
                raise OverflowError('OverflowError: file size is greter or equal to its limit(1GB).')

            #every key will store value, TimeToLive and current time
            #current time is used to eval time passed when we are accesing it
            #if when we are accesing it and TimeToLive is passed then it will creating Error for same
            self.__kvalue[str(key)] = [value, TimeToLive, time_eval()]

            #we are saving it in the file if everthing is okay
            with open(self.__file_dir, 'w') as json_file:
                json.dump(self.__kvalue, json_file)

        #we are handeling all type of error here
        except Exception as exc:
            print(exc)


    def Read(self, key):

        #time variable stores current time while reading the key
        time = time_eval()

        try:
            #if key not in the self.__kvalue then it will create KeyError 
            if str(key) not in self.__kvalue:
                raise KeyError("KeyError: {}".format(key))

            #if TimeToLive if passed then it will create Exception
            if time-self.__kvalue[str(key)][2] > self.__kvalue[str(key)][1]*(1e6):
                raise Exception("TimeToLiveError: {} exceed its Time To Live span thus Read and Delete operations are disabled".format(key))

            #if everthing is ok then it will return key and value in the form of json object
            return {key: self.__kvalue[str(key)][0]}
        
        except Exception as exc:
            print(exc)


    def Delete(self, key):

        #time varaible stores current time while deleting it
        time = time_eval()
        
        try:
            #if key is not in self.__kvalue then it will return KeyError
            if str(key) not in self.__kvalue:
                raise KeyError('KeyError: {}'.format(key))

            #if TimeToLive if passed then it will create Exception
            if time-self.__kvalue[str(key)][2] > self.__kvalue[str(key)][1]*(1e6):
                raise Exception("TimeToLiveError: {} exceed its Time To Live span thus Read and Delete operations are disabled".format(key))

            #if everthing is ok then it will delete key from self.__kvalue
            self.__kvalue.pop(str(key))

            #after deleting we are overrighting it on the file
            with open(self.__file_dir, 'w') as json_file:
                json.dump(self.__kvalue, json_file)
                
        except Exception as exc:
            print(exc)

    
