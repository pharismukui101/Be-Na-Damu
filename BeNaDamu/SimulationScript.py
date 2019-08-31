import numpy as np

class Simulation:
    def __init__(self):
        self.num_in_system=0
        self.clock=0.0
        self.t_arrival=self.generate_interarrival()
        self.t_depart=float('inf')
        
        self.num_arrivals=0
        self.num_departs=0
        self.total_wait=0.0

    def advance_time(self):
        t_event=min(self.t_arrival,self.t_depart)
        self.total_wait=self.num_in_system*(t_event-self.clock)
        self.clock=t_event

        if self.t_arrival<=self.t_depart:
            self.handle_arrival_event()
        else:
            self.handle_depart_event() 
        
    def handle_arrival_event(self):
        self.num_in_system+=1
        self.num_arrivals+=1
        if self.num_in_system<=1:
            self.t_depart=self.clock+ self.generate_service()
        self.t_arrival=self.clock + self.generate_interarrival()
        
    def handle_depart_event(self):
        self.num_in_system-=1
        self.num_departs+=1
        if self.num_in_system>0:
            self.t_depart=self.clock+self.generate_service()
        else:
            self.t_depart=float('inf')
            
    def generate_interarrival(self):
        interarrival_time=[0,7.7,2.3,1.6,2.9,2.1,1.7,4.8,5.8,4.5]
        for time in interarrival_time:
            return time
        
    def generate_service(self):
        service=[3.8,3.5,4.2,3.1,2.4,4.3,2.7,2.1,2.5,3.4]
        for serve in service:
            return serve
        

s=Simulation()
