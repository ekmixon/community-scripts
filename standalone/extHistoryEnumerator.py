"""
This script enumerates all occurrences of a text, based on a regex.
The following search example returns all soapaction names found in 
    the history, be it in the header or body.

You need to edit the 'regex' variable to whatever suits your need
"""

from org.parosproxy.paros.model import Model;
import re;
from org.parosproxy.paros.view import AbstractFrame;
from org.zaproxy.zap.utils import ZapTextArea;

sessionId = Model.getSingleton().getSession();
tbHist = Model.getSingleton().getDb().getTableHistory();

""" Change this variable to match the expression you are looking for """
regex='soapactio.+';

def search(msg):
  """ Searching inside the request """
  if match := re.search(regex,
                        msg.getRequestHeader().toString(), re.IGNORECASE):
    for header in msg.getRequestHeader().toString().split("\n"):
      if match := re.search(regex, header, re.IGNORECASE):
        yield header;
  if match := re.search(regex, msg.getRequestBody().toString(), re.IGNORECASE):
    for word in msg.getRequestBody().toString().split():
      if match := re.search(regex, word, re.IGNORECASE):
        yield word;
  """ Searching inside the response """
  if match := re.search(regex,
                        msg.getResponseHeader().toString(), re.IGNORECASE):
    for header in msg.getResponseHeader().toString().split("\n"):
      if match := re.search(regex, header, re.IGNORECASE):
        yield header;
  if match := re.search(regex,
                        msg.getResponseBody().toString(), re.IGNORECASE):
    for word in msg.getResponseBody().toString().split():
      if match := re.search(regex, word, re.IGNORECASE):
        yield word;


class OutputWindow (AbstractFrame):
    def __init__(self, text):
        self.setAlwaysOnTop(False);
        self.setSize(700, 500);
        ta = ZapTextArea(text);
        self.setContentPane(ta);
        self.setVisible(True);
    

if (tbHist != None):
  final = [];
  print("Searching History...");
  for index in tbHist.getHistoryIds(sessionId.getSessionId()):
    try:
      msg = tbHist.read(index).getHttpMessage();
      results = search(msg);
      for item in results:
        if(item not in final):
          final.append(item);
    except StopIteration:
      pass;
result = ''.join(item+"\n" for item in final);
output = OutputWindow(result);
