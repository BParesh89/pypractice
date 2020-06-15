# Reference --> https://github.com/tongplw/Chat-Room-Socket-Programming-Python

import socket
import _thread
import threading
from datetime import datetime
import pymysql
import json
import secrets
import smtplib



class Server:

    def __init__(self):

        # For remembering users
        self.users_table = {}
        #self.users_email = {}
        self.sessionid = self.get_token()
        # Create a TCP/IP socket and bind it the Socket to the port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 8080)
        self.socket.bind(self.server_address)
        self.socket.setblocking(1)
        self.socket.listen(10)
        print('Starting up on {} port {}'.format(*self.server_address))
        self._wait_for_new_connections()

    def _wait_for_new_connections(self):
        while True:
            connection, _ = self.socket.accept()
            _thread.start_new_thread(self._on_new_client, (connection,))

    def _on_new_client(self, connection):
        try:
            # Declare the client's name
            client_name = connection.recv(64).decode('utf-8')
            client_email = connection.recv(64).decode('utf-8')
            self.users_table[connection] = client_name
            #self.users_email[connection] = client_email
            self.storedata((self.sessionid,'localhost', client_email, client_name), 'connections')
            print(f'{self._get_current_time()} {client_name} joined the room !!')
            #print(f'{ connection}')

            while True:
                data = connection.recv(64).decode('utf-8')
                if data != '':
                    self.multicast(data, owner=connection)
                    self.storedata((self.sessionid, client_name, data), 'chatmessage')
                else:
                    return 
        except:
            print(f'{self._get_current_time()} {client_name} left the room !!')
            self.users_table.pop(connection)
            # send mail when user left the chat
            self.sendmail(client_email,self.sessionid)
            connection.close()

    def _get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def multicast(self, message, owner=None):
        for conn in self.users_table:
            if conn!=owner:
                data = f'{self.users_table[owner]}: {message}              {self._get_current_time()}'
                conn.send(bytes(data, encoding='utf-8'))


    def get_dbconfig(self):
        with open("dbconfig.json","r") as file:
            dbconfig = json.load(file)
        host = dbconfig['dbServerName']
        user = dbconfig['dbUser']
        password = dbconfig['dbPassword']
        db = dbconfig['dbName']
        return host, user, password, db


    def storedata(self, data, table):
        """
        function to store data in mysql table
        :param data: data as set of values
        :param table: table in which data needs to be inserted
        :return:
        """
        # get mysql config from config file
        host, user, password, db = self.get_dbconfig()
        # connect to database and store data
        conn = pymysql.connect(host, user, password, db)
        cursor = conn.cursor()
        if table=='connections':
            cursor.execute("insert into connections (sessionid, ip, email, username) values (%s, %s, %s, %s);", data)
        else:
            cursor.execute("insert into chatmessage (fk_sessionid, sender, message) values (%s,%s, %s);", data)
        conn.commit()
        conn.close()

    def get_token(self):
        """
        Creates a cryptographically-secure, URL-safe string
        """
        existing_sessions = self.get_sessionids()

        while True:
            token = secrets.token_urlsafe(16)
            if token not in existing_sessions:
                return token


    def get_sessionids(self):
        host, user, password, db = self.get_dbconfig()
        # connect to database and store data
        sessionids=[]
        conn = pymysql.connect(host, user, password, db)
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT SESSIONID FROM CONNECTIONS')
        results = cursor.fetchall()
        for result in results:
            sessionids.append(result)
        return sessionids

    def sendmail(self, email_id, sessionid):
        # create and open smtp session
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        # send a hello to smtp gmail server - optional
        smtpObj.ehlo()
        # start tls server
        smtpObj.starttls()
        # get password from json file
        with open("mailpassword.json","r") as file:
            mailconfig = json.load(file)
        password = mailconfig['password']
        # login to smtp
        smtpObj.login('bhatia.paresh89@gmail.com', password)
        messages = self.get_messages(sessionid)
        # create mail body
        body=''
        for msg in messages:
            body = body + msg + '\n'
        # send email
        smtpObj.sendmail('bhatia.paresh89@gmail.com', email_id,
                         'Subject: So long.\n' + body +
                         'Sincerely, Paresh.')
        # stop smtp server
        smtpObj.quit()

    def get_messages(self,sessionid):
        host, user, password, db = self.get_dbconfig()
        # connect to database and store data
        chats=[]
        conn = pymysql.connect(host, user, password, db)
        cursor = conn.cursor()
        cursor.execute('select concat(sender,' - ',message) from chatmessage where fk_sessionid=%s',sessionid)
        results = cursor.fetchall()
        for result in results:
            chats.append(result)
        return chats

if __name__ == "__main__":
    Server()