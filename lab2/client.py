#Client code
"""
August 1, 2021
Created by: Sebastian Loaiza Correa
"""
#Import socket library
import socket
import constants
import os
import http.client
import requests
#Variables for connection
host = constants.SERVER_ADDRESS
port = constants.PORT

def runClient():

    #Maintain connection with the server
    while True:
        #Client command
        command = input("Enter the command you want to send >> ")
        informationToSend = ""
        if command == constants.HELLO or command == constants.LIST_BUCKET:
            informationToSend = command
        elif command == constants.NEW_BUCKET:
            bucketName = input("Enter the name of the new bucket >> ")
            informationToSend = command+"/"+bucketName
        elif command == constants.DELETE_BUCKET:
            bucketName = input("Enter the name of the bucket to delete >> ")
            informationToSend = command+"/"+bucketName
        elif command == constants.UPLOAD_FILE:
            filePath = input("Enter the path where the file is >> ")
            fileName = input("Enter the name of the file to upload >> ")
            bucketName = input("Enter the name of the bucket where the file will be uploaded >> ")
            with open(filePath, "rb") as a_file:
                file_dict = {fileName: a_file}
                response = requests.post("http://localhost:8050", files=file_dict)
                print(response)
        elif command == constants.LIST_FILE:
            bucketName = input("Enter the bucket name to list the files >> ")
            informationToSend = command+"/"+bucketName
        elif(command == constants.DOWNLOAD_FILE):
            fileName = input("Enter the name of the file to download >> ")
            bucketName = input("Enter the bucket name to download the file >> ")
            clientSocket.send((command+','+fileName+','+bucketName).encode('ascii'))
            f = open(os.path.join(os.getcwd(), fileName), "wb")
            while True:
                bytes_read = clientSocket.recv(constants.BUFFER_SIZE)
                if bytes_read.decode('ascii')[-3:] == "EOF":
                    f.write(bytes_read.decode('ascii')[:-3].encode('ascii'))
                    print('terminado')
                    break
                print('received bites')
                f.write(bytes_read)
            f.close()
            print('received complete')
            clientSocket.send('OK'.encode('ascii'))
            continue
        elif(command == constants.DELETE_FILE):
            fileName = input("Enter the name of the file to delete >> ")
            bucketName = input("Enter the bucket name to delete the file >> ")
            informationToSend = command+"/"+fileName+"/"+bucketName
        elif(command == constants.EXIT):
            break
        else:
            print("Non-existent command, try again")
            continue
        #Send message
        if(informationToSend != ""):
            connection = http.client.HTTPConnection(constants.SERVER_ADDRESS, constants.PORT)
            connection.request("GET", '/' + informationToSend)
            response = connection.getresponse()
            print("Status: {} and reason: {}".format(response.status, response.reason))
            connection.close()

#Iniatialize client
runClient()
