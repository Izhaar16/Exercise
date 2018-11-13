# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 10:31:56 2018

@author: izhaa
"""

from threading import Thread, Condition, current_thread
import random,time
import array as arr

class file:
    
    ArrList = arr.array('i',[])
    
    def __init__(self,ArrList):
        self.cond = Condition()
        self.ArrList= arr.array('i',[])
        
    def ajout(self, addNum):
        if not isinstance(addNum,int):
            return
        with self.cond:
            while self.ArrList.len >= 20:
                self.cond.wait()
            self.ArrList.append(addNum)
            
    def retrait(self):
        while self.ArrList.len() ==0:
            self.cond.wait()
        top = self.ArrList.copy(0)
        self.ArrList.remove(0)
        print("L'entier a bein été supprimé "+" ",top)
        
    def getNum(self):
        with self.cond:
            return self.top
        
class ThreadProducteur(Thread):
    def __init__(self, file, tempsSommeil, entier, nom):
        Thread.__init__(self)
        self.file =file
        self.tempsSommeil = tempsSommeil
        self.entier = entier
        self.name = nom
        self.daemon = True
        
    def run(self):
        while True:
            ajoutInt =random.randint(self.entier,1)
            self.file.ajout(ajoutInt)
            time.sleep(self.tempsSommeil)
            print( "L'entier"+" "+str(ajoutInt+" "+"a bien été ajouté"))
            

class ThreadConsommateur(Thread):
    def __init__(self, file, tempsSommeil, nom):
        Thread.__init__(self)
        self.file=file
        self.tempsSommeil = tempsSommeil
        self.name = nom
        self.daemon = True
    
    def run(self):
        while True:
            self.file.retrait()
            time.sleep(self.tempsSommeil)
            

if __name__ == "__main__":
    
    random.seed()
    
    file = file(20)
    
    
    #creation of threads
    
    prod = ThreadProducteur(file, 1,100,"prod")
    cons0 =ThreadConsommateur(file,1,"cons0")
    cons1 =ThreadConsommateur(file,1,"cons1")
    
    prod.start()
    cons0.start()
    cons1.start()
    
    
    input("")
    
    
          
    
        
                
            
            
            
            
        
        
        
    
    
    
        
        
        
        
    