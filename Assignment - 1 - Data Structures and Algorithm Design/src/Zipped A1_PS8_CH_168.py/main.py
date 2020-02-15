#!/usr/bin/env python
# coding: utf-8


import os
import time


# All lambda Functions here
def initialize_hash():
    mapping_data = [
        [], # name list
        [], # phone list
        [], # member referece list
        [],  # application status list
        ['name', 'phone', 'memRef', 'status']
    ]
    return mapping_data

# Main Class
class clubHouseTracker(object):
    def __init__(self, output_file='outputPS8.txt'):
        super(clubHouseTracker).__init__()
        self.output_file = os.path.abspath(output_file)
        self._writeOutput('', 'w')
        
    def _writeOutput(self, output, mode='a'):
        with open(self.output_file, mode) as f:
            f.write(output)
            
    def _nextHashId(self):
        return len(self.data[0])
            
    def initializeHash(self):
        self.data = initialize_hash()
        
    def hashId(self, name):
        return self.data[0].index(name)
    
    def insertAppDetails(self, name, phone, memRef, status):
        hash_id = self._nextHashId()
        self.data[0].append(name)
        self.data[1].append(phone)
        self.data[2].append(memRef)
        self.data[3].append(status)
        return hash_id
    
    def updateAppDetails(self, name, phone=None, memRef=None, status=None):
        hash_id = self.hashId(name)
        if hash_id > -1:
            fields_to_update = []
            for i, (field, field_data) in enumerate(zip(self.data[-1], [name, phone, memRef, status])):
                if i > 0 and field_data is not None:
                    fields_to_update.append(field)
                    self.data[i][hash_id] = field_data
            fields_updated = ', '.join(fields_to_update)
            write_text = f"""\nUpdated details of {name}. { fields_updated } has been changed."""
            print(write_text)
            self._writeOutput(write_text)
            return True      
        else:
            return False
    
    def _memRef(self, memID):
        members = []
        for i, j in enumerate(self.data[2]):
            if j == memID:
                members.append(i)
        return members
        
    def memRef(self, memID):
        members = self._memRef(memID)
        rows = []
        for i in members:
            line = f"{self.data[0][i]} / {self.data[1][i]} / {self.data[3][1]}"
            rows.append(line)
        rows = '\n'.join(rows)
        output_text = f"""\n\n---------- Member reference by {memID} ----------\n{rows}\n-------------------------------------"""
        self._writeOutput(output_text)
        print(output_text)
        
    def appStatus(self):
        stats = [0, 0, 0]
        for status in self.data[3]:
            if status == 'Applied':
                stats[0]+=1
            elif status == 'Verified':
                stats[1]+=1
            else:
                stats[2]+=1
            
        output_text = f"""\n\n---------- Application Status ----------\nApplied: {stats[0]}\nVerified: {stats[1]}\nApproved: {stats[2]}\n-------------------------------------"""
        self._writeOutput(output_text)
        print(output_text)
    
    def destroyHash(self):
        self.initializeHash()
            
    
    



# %%
