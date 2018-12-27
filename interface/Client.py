# Chat client interface

#This is a class used as the interface to client communication
#It provides a function, send, which sends a text message
#Currently send simply prints the message to console for debugging
#Eventually, it will forward this message to the client(s) the message is intended for
class ClientInterface:

    def __init__(self,client_name,client_id):
        self.m_client_name = client_name
        self.m_client_id=client_id

    def send(self,message):
        print ("Client Name: ",self.m_client_name,"\nClient Message: ",message)


