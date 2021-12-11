import threading
import time
import Wallet
import Miner
import Signatures

wallets = []
miners = []
my_ip = 'localhost'

my_pu = None
my_pr = None
my_ip = 'localhost'
wallets.append((my_ip, 5006))
miners.append((my_ip, 5005))

tMS = None
tNF = None
tWS = None

def startMiner():
    global tMS, tNF
    try:
        my_pu = Signatures.loadPublic("public.key")
    except:
        pass
    tMS = threading.Thread(target=Miner.minerServer, args=((my_ip, 5005),))
    tNF = threading.Thread(target=Miner.nonceFinder, args=(wallets, my_pu))
    tMS.start()
    tNF.start()
    #Load head_blocks
    return True

def startWallet():
    global tWS
    Wallet.my_private, Wallet.my_public = Signatures.loadKeys(
        "private.key", "public.key")
    
    tWS = threading.Thread(target=Wallet.walletServer, args=((my_ip, 5006),))
    
    #Load public and private keys
    #Load head_blocks
    return True

def stopMiner():
    Miner.stopAll()
    if tMS: tMS.join()
    if tNF: tNF.join()
    #save tx_list
    #save head_blocks
    return True

def stopWallet():
    Wallet.stopAll()
    if tWS: tWS.join()
    #Stop walletServer
    #Save head_blocks
    return True

def getBalance(pu_key):
    return 0.0

def sendCoins(pu_recv, amt, tx_fee):
    return True

def makeNewKeys():
    return None, None

if __name__ == "__main__":
    startMiner()
    startWallet()
    other_public = b'-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4fchcM3fKs9e2YKs0Dvj4T/DRAvmzTkDtGMRR+rP399lCP7BiAgkQthjbXEveYJfwdot/2EVeIzZPY56ziNhp8WT9odgpJ/qvOPNRsk048H8lP9zyRV49LjOHzc/gs783adOgLmHJk233BVOsWa0VWrGzPdIUOYmV6Jqbx2sRId37OmNMUwJsEeegBA+if4zYpKKxRxuh4i8lUiAu7/8TXPpLTQAMcsix8/xqRTS1AS+PtdI7oQoI3HOuD/nkhae8EFAwr3+pxbIQMCZ2VWpuIf7QDxt2jwtmsIbpOl7JGweAA8t+8jaDY5USiQqbjljn8g99lishkQsY7shfVnzUQIDAQAB-----END PUBLIC KEY-----'
    time.sleep(2)
    print(getBalance(Wallet.my_public))
    sendCoins(other_public, 1.0, 0.001)
    print(getBalance(other_public))
    print(getBalance(Wallet.my_public))
    
    time.sleep(1)
    stopWallet()
    stopMiner()
    