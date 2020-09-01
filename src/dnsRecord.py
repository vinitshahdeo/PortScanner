import socket 
import dns
import dns.resolver

remoteServer = raw_input("Enter a remote host to scan: ")
print "\n\n"
print "==============================================================="
print "Fetching DNS records for host: ", remoteServer
print "==============================================================="
print "\n\n"

# --------------to fetch IPv4 and IPv6 addresses ----------------------

try:
    remoteServerIP4 = socket.gethostbyname(remoteServer) 
    remoteServerIP6 = socket.getaddrinfo(remoteServer, None, socket.AF_INET6)
    print "IPv4 Address : " , remoteServerIP4
    print "\n\n"
    print "IPv6 Address : " , remoteServerIP6[0][4][0]
    print "\n\n"
except socket.gaierror:
    print "Hostname could not be resolved. Exiting"
    print "\n\n"
except Exception:
    print "Error during dns resolution"
    print "\n\n"

# ------------to fetch CNAME record: canonical name records----------------

try:
    result = dns.resolver.query(remoteServer, 'CNAME')
    for cnameval in result:
        print "CNAME target address:", cnameval.target
    print "\n\n"
# except dns.resolver.NoAnswer as Error:
#     print Error
except Exception as Error:
    print "CNAME target address:"
    print Error
    print "\n\n"

# ------------to fetch MX record: mail exchange records----------------

try:
    result = dns.resolver.query(remoteServer, 'MX')
    print "MX Record: "
    for exdata in result:
        print exdata.exchange.text()
    print "\n\n"
except Exception as Error:
    print "MX Record: "
    print Error
    print "\n\n"

# ------------to fetch ANY record: any records----------------

try:
    result = dns.resolver.query(remoteServer, 'ANY')
    print result.__dict__
    for attr in dir(result):
        print attr, getattr(result, attr)
    print "\n\n"
except Exception as Error:
    print Error
    print "Because it would add complexity in the Answer object, \nand because ANY queries are usually not good things to do from a stub resolver; \nthe ANY query will just get anything that happens to be cached, \nnot everything that may be associated with the name."
    print "\n\n"

# ------------to fetch NAPTR record: name authority pointer records----------------

try:
    result = dns.resolver.query(remoteServerIP4, 'NAPTR')
    print "NAPTR record: "
    for rdata in result:
        print rdata.to_text()
    print "\n\n"
except Exception as Error:
    print "NAPTR record: "
    print Error
    print "\n\n"

# ------------to fetch NS record: name server records----------------

try:
    result = dns.resolver.query(remoteServer, 'NS')
    # for attr in dir(result):
    #     print attr, getattr(result, attr)
    print "NS record: "
    for rdataset in result:
        print rdataset.target
    print "\n\n"
except Exception as Error:
    print "NS record: "
    print Error
    print "\n\n"

# ------------to fetch PTR record: pointer records----------------

req = '.'.join(reversed(remoteServerIP4.split("."))) + ".in-addr.arpa"

try:
    result = dns.resolver.query(req, 'PTR')
    print "PTR record: "
    for rdata in result:
        print rdata.target
    print "\n\n"
except Exception as Error:
    print "PTR record: "
    print Error
    print "\n\n"

# ------------to fetch SOA record: start of authority records----------------

try:
    result = dns.resolver.query(remoteServer, 'SOA')
    print "SOA record: "
    for rdata in result:
        print 'Serial: ', rdata.serial
        print 'Tech: ', rdata.rname
        print 'Refresh: ', rdata.refresh
        print 'Retry: ', rdata.retry
        print 'Expire: ', rdata.expire
        print 'Minimum: ', rdata.minimum
        print 'mname: ', rdata.mname
        print "\n"
    print "\n\n"
except Exception as Error:
    print "SOA record: "
    print Error
    print "\n\n"

# ------------to fetch SRV record: service records----------------

try:
    result = dns.resolver.query('_xmpp-client._tcp.'+remoteServer, 'SRV')
    print "SRV record: "
    for srv in result:
        print "weight: ", srv.weight
        print "host: ", str(srv.target).rstrip('.')
        print "priority: ", srv.priority
        print "port: ", srv.port
        print '\n'
    print "\n\n"
except Exception as Error:
    print "SRV record: "
    print Error
    print "\n\n"

# ------------to fetch TXT record: text records----------------

try:
    result = dns.resolver.query(remoteServer, 'TXT')
    print "TXT record: "
    for rdata in result:
        for txt_string in rdata.strings:
            print " TXT: ", txt_string
    print "\n\n"
except Exception as Error:
    print "TXT record: "
    print Error
    print "\n\n"
