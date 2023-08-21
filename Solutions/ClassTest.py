
def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = time.seconds = divmod(seconds, 60)
    time.hours, time.minutes = divmod(minutes, 60)
    time.day, time.hours = divmod(time.hours, 24)
    return time

class Time :
    ''' 
        Classe horas horas minutos e segundos
    '''
    

    def __init__(self, day = 0,hours = 0, minutes = 0, seconds = 0) -> None:
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        return '%2d:%2d:%2d:%2d' % (self.day, self.hours, self.minutes, self.seconds)
    
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def time_to_int(self):
        minutes = self.hours * 60 + self.minutes + self.day * 24
        print(minutes)
        seconds = minutes * 60 + self.seconds
        return int_to_time(seconds)

    def adjust_time (self):
        
        div, self.seconds = divmod(self.seconds, 60)
        min_sum = (div * 60)
        self.minutes = self.minutes + min_sum
        div, self.minutes = divmod(self.minutes, 60)
        hour_sum = (div * 60)
        self.hours = self.hours + hour_sum
        div, self.hours = divmod(self.hours, 24)
        min_day = (div * 24)
        self.day = self.day + min_day

        

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
t2 = Time(2, 12, 24, 13)


print(t + t2)
