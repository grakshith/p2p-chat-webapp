'''
The MIT License (MIT)
Copyright (c) 2013 Dave P.
'''
import signal
import sys
import ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser
clients = []
class SimpleChat(WebSocket):

   def handleMessage(self):
      for client in clients:
         if client != self:
            client.sendMessage(str(self.address) + u' - ' + self.data)

   def handleConnected(self):
      print (self.address, 'connected')
      for client in clients:
         client.sendMessage(str(self.address) + u' - connected')
      clients.append(self)
      #updateClient(self)
      for x in clients:
         li=[]
         for y in clients:
            if(x!=y):
               li.append(str(y.address)+'\n')
         #x.sendMessage(u"Send Client Data")
         x.sendMessage(u"!@#$%^&*&^%$#@!!@#$%^&*"+u''.join(li))
         print(u"!@#$%^&*&^%$#@!!@#$%^&*"+u''.join(li))
         #x.sendMessage(u"End Cliend Data")

   def handleClose(self):
      clients.remove(self)
      print (self.address, 'closed')
      for client in clients:
         client.sendMessage(str(self.address) + u' - disconnected')
         
   """def updateClient(self):
      print "hi"
      for x in clients:
         li=[]
         for y in clients:
            if(x!=y):
               li.append(str(y)+'\n')
         
         x.sendMessage("!@#$%^&*&^%$#@!!@#$%^&*"+''.join(li))"""


if __name__ == "__main__":

   parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
   parser.add_option("--host", default='', type='string', action="store", dest="host", help="hostname (localhost)")
   parser.add_option("--port", default=8000, type='int', action="store", dest="port", help="port (8000)")
   
   (options, args) = parser.parse_args()
   cls = SimpleChat

   server = SimpleWebSocketServer(options.host, options.port, cls)

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)

   server.serveforever()
