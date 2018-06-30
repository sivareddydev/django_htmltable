from django.http import HttpResponse
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
import xml.etree.ElementTree as ET

def kpi(request):
    with open("kpi.tsv") as f:
        rows = ( line.split('\t') for line in f )
        kpi = { row[0]:row[1:] for row in rows }
        print kpi
    return render_to_response('index.html',{'kpi':kpi,},context_instance=RequestContext(request))




def kpidetails(request):
    with open("kpidetails.md") as f:
        rows = ( line.split('|') for line in f )
        details = { row[0]:row[1:] for row in rows }
        print details
    return render_to_response('index1.html',{'details':details,},context_instance=RequestContext(request))





def mstest(request):
    filename = "mstest.xml"
    full_filename= os.path.abspath(os.path.join('data',filename))
    dom = ET.parse(full_filename)
    root= dom.getroot()
    for child in root:
        mstest= (child.tag, child.attrib)
        print mstest
    return render_to_response('mstest.html',{'mstest':mstest,},context_instance=RequestContext(request))





def xunit (request):
    filename = "xunit.xml"
    full_filename= os.path.abspath(os.path.join('data',filename))
    dom = ET.parse(full_filename)
    collection_element=dom.findall("./assembly/collection")
    for elem in collection_element:
        xunit = child.attrib
        print xunit
    return render_to_response('xunit.html',{'xunit':xunit,},context_instance=RequestContext(request))

