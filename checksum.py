#MEOW TECH CHANNEL AND SKU TEST
sku=True
channel=False
base=1
core=2
pro=3
stable=100
beta=101
dev=102
dogfood=103
skus=[base,core,pro]
channels=[stable,beta,dev,dogfood]
currentsku=base
currentchannel=dogfood
def compare(mode,target):
    skus=['base','core','pro']
    chns=['stable','beta','dev','dogfood']
    global sku, channel,currentsku,currentchannel
    if mode == sku:
        if currentsku >= target:
            return True
        else:
            return False
    elif mode == channel:
        if currentchannel >= target:
            return True
        else:
            return False

def chksku(t):
    global sku
    return compare(sku,t)
def chkchn(t):
    global channel
    return compare(channel,t)
def dochecking(targetsku,targetchannel):
    if chksku(targetsku):
        if chkchn(targetchannel):
            return [True,"Placeholder 1"]
        else:
            return [False,"Channel is too small"]
    else:
        return [False,'SKU is too small.']
#TEST
def alittlefunction():
    global base,core,pro,stable,beta,dev,dogfood,currentsku,currentchannel
    targetsku=pro
    targetchannel=dogfood
    m=dochecking(targetsku,targetchannel)
    print(m[0],m[1])
alittlefunction()
