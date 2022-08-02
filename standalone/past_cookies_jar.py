"""
This script lists all unique cookies seen.
You may collect them based on the associated domain, you
just need to change the 'cookie_domain_regex' variable
below.
"""

from org.parosproxy.paros.model import Model;
import re;
from org.parosproxy.paros.view import AbstractFrame;
from org.zaproxy.zap.utils import ZapTextArea;
from javax.swing import JScrollPane;

""" Change this regex to match the desired domain """
cookie_domain_regex = ".+"

sessionId = Model.getSingleton().getSession();
tbHist = Model.getSingleton().getDb().getTableHistory();

def collect(msg):
  """ Collecting cookie from HttpMessage """
  return msg.getRequestHeader().getHttpCookies();

class OutputWindow (AbstractFrame):
  def __init__(self, text):
    self.setAlwaysOnTop(False);
    self.setSize(700, 500);
    ta = ZapTextArea(text);
    sp = JScrollPane(ta, 
		JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, 
		JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
    self.add(sp);
    self.setVisible(True);
    
if (tbHist != None):
  unique_cookies = [];
  print("Collecting Unique Cookies...");
  for index in tbHist.getHistoryIds(sessionId.getSessionId()):
    try:
      msg = tbHist.read(index).getHttpMessage();
      domain = msg.getRequestHeader().getURI().getHost();
      results = collect(msg);
      if results is None:
        continue;
      for item in results:
        item.setDomain(domain);
        if match := re.search(cookie_domain_regex, domain, re.IGNORECASE):
          cookie = f"{domain}: {item.getName()}" + "=\"" + item.getValue() + "\"";
          if(cookie not in unique_cookies):
            unique_cookies.append(cookie);
    except StopIteration:
      pass;
result = ''.join(cookie+"\n" for cookie in sorted(unique_cookies));
output = OutputWindow(result);
