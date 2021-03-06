from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import CommitError

dev = Device('host', user='user', password='pwd')

dev.open()

cu = Config(dev)

data = """interfaces { 
    ge-1/0/1 {
        description "MPLS interface";
        unit 0 {
            family mpls;
        }      
    } 
}
"""

cu.load(data, format='text')

print "\nconfig# show | compare"
cu.pdiff()

if cu.commit_check():
    print "\nCommiting..\n"
#   cu.commit(comment="Configuring ge-1/0/1 interfaces")
    cu.commit(sync=True)
else:
    cu.rollback()

print "cli> show configuration interfaces", dev.cli("show configuration interfaces", warning=False)

#print "Rolling back the configuration"
#cu.rollback(rb_id=1)
#cu.commit(detail=True)
#cu.commit(sync=True)

#print "cli> show configuration interfaces", dev.cli("show configuration interfaces", warning=False)

dev.close()
