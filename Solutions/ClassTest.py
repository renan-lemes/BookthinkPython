
class Time :
    ''' 
        Classe horas horas minutos e segundos
    '''
    def __init__(self, day,hours, minutes, seconds) -> None:
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def valid_time (self):
        ''' 
            Metodo que verifica a viabilidade do time.
        '''
        if self.hours < 0 or self.minutes < 0 or self.seconds < 0 :
            return False
        if self.minutes >= 60 or self.seconds >= 60 or self.hours >= 24:
            return False
        return True
    
    def increment(self, seconds):
        ''' 
            incrementar segundos na class 
        '''
        self.seconds += seconds

        # if self.seconds >= 60 :
        #     self.seconds -= 60
        #     self.minutes += 1

        # if self.minutes >= 60:
        #     self.minutes -= 60
        #     self.hours += 1
    
        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60

        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        
        while self.hours >= 24:
            self.day += 1
            self.hours -= 24

    def print_timer(self):
        print("%2d:%2d:%2d:%2d" % (self.day, self.hours, self.minutes, self.seconds))     
        
    def print_seq(self):
        print(f"Days: {self.day}")
        print(f"Hours: {self.hours}")
        print(f"Minutes: {self.minutes}")
        print(f"Seconds: {self.seconds}")

t = Time(2, 12, 24, 13)

t.print_seq()
