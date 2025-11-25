#handling a xml
"""
import xml.etree.ElementTree as et
#to parse from a file
tree=et.parse("data.xml")
#to get root tag
root=tree.getroot()
print("printing root:",root)
root.set("new","20")
tree.write("data.xml")
print("printing root tag name:",root.tag)
print("printing root tag attributes:",root.attrib)
#acessing particular attribute
print("printing root tag specific attribute value:",root.attrib["new"])
print("printing root tag value:",root.text)
#to find first matching child
firstchild=root.find("a")
print("first found child 'a':",firstchild)
#to print text after element ends
print("printing text after end of this element:",firstchild.tail)
#to create and alter an attribute
firstchild.set("d","10")
#to actually alter the file in memory
tree.write("data.xml")
print("printing attributes of firstchild:",firstchild.attrib)
#to remove a attribute
del root.attrib["new"]
tree.write("data.xml")
print("printing type of firstchild:",type(firstchild))
print("printing value of firstchild:",firstchild.text)
#to find all matching child (returns list)
allfirstchild=root.findall("a")
print("printing all found 'a' in xml:",allfirstchild)
print("printing value of all in allfirstchild")
for i in allfirstchild:
    print(i.text)
#to iterate through all elements
p=root.iter()
print("value of .iter on p:",p)
print("printing index,name,value of all in p:")
for i,item in enumerate(p,start=1):
    print(i,item.tag,item.text)
#to find all matching child (returns generator)
f=root.iterfind('a')
print("printing value of iterfind on root:",f)
print("printing name,value of all in f:")
for i in f:
    print(i.tag,i.text)
#to find element but just return its text
t=root.findtext("a")
print("printing value of findtext on root:",t)
t1=root.findtext("b",default=None)
print("printing value of findtext on a element that does not exist i.e. default value:",t1)
#to loop through child(tags in root or any parent tag)
print("looping through all children/element in root:")
for child in root:
    print(child.tag,child.text)
allfirstchild=root.findall("a")
print("printing all children/element in second 'a':")
for i in range(len(allfirstchild)):
    if(i==1):
        seca=allfirstchild[i]
for k in seca:
    print(k.tag,k.text)
#creating new ele.
newelem=et.SubElement(root,"map",{"attr1":'1',"attr2":'2'},age="20")
newelem.text="india"
tree.write("data.xml")
#to remove a element
tree2=et.parse("data2.xml")
root2=tree2.getroot()
for child in root2:
    root2.remove(child)
tree2.write("data2.xml")"""

#ro parse from string
"""import xml.etree.ElementTree as et
xml_string="<root><a>10</a></root>"
root=et.fromstring(xml_string)
print("printing value of fromstring func. in elementtree",root)"""

#create element and convert and print as string
"""
import xml.etree.ElementTree as et
root=et.Element("student")
root.set("id","101")
#print(et.tostring(root).decode())
new_xml = et.tostring(root, encoding='unicode')
print(new_xml)
"""

#create element and convert and save to xml file
"""
import xml.etree.ElementTree as et
root=et.Element("student")
root.set("id","101")
tree=et.ElementTree(root)
tree.write("output.xml",encoding="utf-8",xml_declaration=True)
"""

#hackerrank question to calculate depth of tree
"""import xml.etree.ElementTree as et
tree=et.parse("depthtest.xml")
root=tree.getroot()
maxdepth=0

def finddepth(node,level):
    global maxdepth
    if(level>maxdepth):
        maxdepth=level
    for child in node:
        finddepth(child,level+1)"""
######WHY THIS WORKS-------------------------------------------
# so we increase level/depth when we go into a child and its diff.
# from brefore "maxdepth=maxdepth+1" as then it would
# increse depth when loop runs for every new sibling which was
# wrong ,and we wanted to increase depth when new deeper level
# or inner child was encountered and also we only incerase
# max depth when level of this child is deeper then before
# thats why in our example test.xml when we increased to level 5
# on fifthchild deep inside subtitle it set level to 5 and as it
# was greater then any before it updated maxdepth to 5 and also
# as 5 would be greater than any other depth inside test.xml,it
# would not allow to update maxdepth again because of
# if(level>maxdepth),also if any node has no children loop would
# not run and this version of function would end with only with
# updating if this level would be greater than before
#####WHY PREVIOUS .ITER FAILED---------------------------------
# In the previous code you used .iter() to find children.
# But .iter() returns ALL descendants (children, grandchildren, etc.)
# at once,so you were not moving one level at a time — you were
# jumping through the whole subtree.You increased maxdepth for EVERY
# child encountered,which counted the total number of nodes instead
# of how many levels exist.More siblings falsely increased depth,
# even though they were at the same level.Because .iter() was
# returning grandchildren directly from a parent, recursion was
# called multiple times on the same nodes, creating repeated visits
# and completely losing the level structure.
#####WHY THIS IS BETTER THAN USING RETRURN---------------------
# Checking the level BEFORE the for-loop is simpler because:We update
# maxdepth immediately when we go one level deeper.We do not need
# to return anything from recursion.We do not need to store or
# compare depths of every child manually.Recursion only moves depth
# downward; no value needs to travel back upward. Taking a return
# value from each recursive call and comparing it INSIDE the loop is
# more complex because,Every recursive call must return a depth
# value to its parent.The parent must receive that value, store it,
# and compare it for every child.We must track the maximum of all
# returned values inside the loop.We must return a depth again
# after finishing the loop to the previous caller.In other words,
# depth must be passed back up through every level of recursion,which
# makes the logic more complicated to write and easier to get wrong.
# So the current approach is simpler because the depth is tracked on
# the way DOWN (using 'level' and updating maxdepth immediately),
# while the alternative approach tracks depth on the way BACK UP,
# which requires extra comparisons, variables, and returns.


finddepth(root,-1)
print(maxdepth)

""""if root starts at -1 according to hackerrank"""
"""
import xml.etree.ElementTree as etree
tree=et.parse("depthtest.xml")
root=tree.getroot()
maxdepth=0

def depth(elem, level):
    global maxdepth
    level=level+1
    if(level>maxdepth):
        maxdepth=level
    for child in elem:
        depth(child,level)

if __name__ == '__main__':
    depth(tree.getroot(), -1)
    print(maxdepth)
"""