from stanfordkarel import *


class ktools:
  def m(self):
    """Move"""
    move()
  
  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn around"""
    self.tl()
    self.tl()
    
  def put(self):
    put_beeper()

  def pick(self):
    pick_beeper()

  def put2(self):
    self.put()
    self.m()
    self.put()

  def pick5(self):
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H w beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    
  def main():
    """ Karel code goes here! """
    
    pass


if __name__ == "__main__":
    run_karel_program()