import sqlite3

conn = sqlite3.connect('CiscoLab.db')
with conn:
    c = conn.cursor()

class Inventory:
    def __init__(self, StudNum, Rack, Switch, Router, Console, LAN, Power):
        self.StudNum = StudNum
        self.Rack = Rack
        self.Switch = Switch
        self.Router = Router
        self.Console = Console
        self.LAN = LAN
        self.Power = Power
        
    def borrowItems(self):
        c.execute("SELECT * FROM Borrowed WHERE StudentNumber = ?", (self.StudNum,))
        val = c.fetchone()
        if val is None:
            c.execute("INSERT INTO Borrowed VALUES (:StudentNumber, :Rack, :Switch, :Router, :ConsoleCable, :LANCable, :PowerCable)",
                  {'StudentNumber': self.StudNum,'Rack': self.Rack, 'Switch': self.Switch, 'Router': self.Router, 'ConsoleCable': self.Console, 'LANCable': self.LAN, 'PowerCable': self.Power})
        else:
            c.execute("UPDATE Borrowed SET Rack = ? , Switch = ? , Router = ? , ConsoleCable = ? , LANCable = ? , PowerCable = ? WHERE StudentNumber = ?", (val[1] + self.Rack, val[2] + self.Switch, val[3] + self.Router, val[4] + self.Console, val[5] + self.LAN, val[6] + self.Power, self.StudNum))
            
        c.execute("SELECT * FROM Inventory")
        dat = c.fetchall()
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[0][1] - self.Rack, dat[0][2] + self.Rack, 'Rack'))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[1][1] - self.Switch, dat[1][2] + self.Switch, 'Switch'))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[2][1] - self.Router, dat[2][2] + self.Router, 'Router'))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[3][1] - self.Console, dat[3][2] + self.Console, 'Console Cable'))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[4][1] - self.LAN, dat[4][2] + self.LAN, 'LAN Cable'))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[5][1] - self.Power, dat[5][2] + self.Power, 'Power Cable'))
        
        conn.commit()
        
    def returnItems(StudNum):
        rack = 0
        switch = 0
        router = 0
        con = 0
        lan = 0
        power = 0
        
        c.execute("SELECT * FROM Borrowed WHERE StudentNumber=:sn", {'sn':StudNum})
        x = c.fetchall()
        for row in x:
            rack = row[1]
            switch = row[2]
            router = row[3]
            con = row[4]
            lan = row[5]
            power = row[6]
        
        c.execute("DELETE FROM Borrowed WHERE StudentNumber=:sn", {'sn':StudNum})
        
        c.execute("SELECT * FROM Inventory")
        dat = c.fetchall()
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[0][1] + rack, dat[0][2] - rack, "Rack"))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[1][1] + switch, dat[1][2] - switch, "Switch"))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[2][1] + router, dat[2][2] - router, "Router"))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[3][1] + con, dat[3][2] - con, "Console Cable"))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[4][1] + lan, dat[4][2] - lan, "LAN Cable"))
        c.execute("UPDATE Inventory SET Available = ? , Borrowed = ? WHERE Equipment = ?", (dat[5][1] + power, dat[5][2] - power, "Power Cable"))
        
        conn.commit()

        
