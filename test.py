import optparse
import xml.etree.ElementTree as ET
def ip_check_Azure(ip):
    tree = ET.parse('ip_ranges_Azure.xml')
    root = tree.getroot()
    ip_correct = 0
    for i in range (0,len(ip.split('.'))):
        if len(ip.split('.'))==4 and ip.split('.')[i].isdigit():
            ip_correct += 1
    if ip_correct==4:
        x = []
        for i in range (len(ip.split('.'))):
            x.append(ip.split('.')[i])
        for child in root:
            for child in child:
                range_azure= child.attrib['Subnet'].split('.')
                match = 0
                for j in range(len(range_azure)):
                    if x[j]==range_azure[j]:
                        match+=1
                if match >= 3:
                    return "Hoster is Microsoft Azure."            
    else:
        return "Incorrect data! Please, type again."

def ip_check_Amazon(ip):
    tree = ET.parse('ip_ranges_Amazon.xml')
    root = tree.getroot()
    ip_correct = 0
    for i in range (0,len(ip.split('.'))):
        if len(ip.split('.'))==4 and ip.split('.')[i].isdigit():
            ip_correct += 1
    if ip_correct==4:
        x = []
        for i in range (len(ip.split('.'))):
            x.append(ip.split('.')[i])
        for child in root:
            for child in child:
                for child in child:
                    if child.tag == 'ip_prefix':
                        range_amazon= child.text.split('.')
                        match = 0
                        for j in range(len(range_amazon)):
                            if x[j]==range_amazon[j]:
                                match+=1
                        if match >= 3:
                            return "Hoster is Amazon Web Services."
    else:
        return "Incorrect data! Please, type again."


                    
                            
