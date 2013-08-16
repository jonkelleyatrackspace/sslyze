

from nisslyze import *
target_list = ['google.com:443','www.reddit.com:443','www.example.com:443']
shared_settings = {
'certinfo':     'full',        'starttls':     None,       'resum':        None,
'resum_rate':   None,           'http_get':     None,       'xml_file':     '/tmp/xy', 
'compression':  None,           'tlsv1':        None,       'targets_in':   None, 
'cert':         None,           'https_tunnel_port': None,  'keyform':      1, 
'hsts':         None,           'sslv3':        None,       'sslv2':        None, 
'https_tunnel': None,           'sni':          None,       'https_tunnel_host': None, 
'regular':      None,           'key':          None,       'reneg':        None, 
'tlsv1_2':      None,           'tlsv1_1':      None,       'hide_rejected_ciphers': None,
'keypass':      '',             'nb_processes': 1,          'certform':     1, 
'timeout':      5,              'xmpp_to':      None}

main(target_list,shared_settings)
