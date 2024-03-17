
MEM_SIZE = 0x10000

class CPU:
    def __init__(self):
        self.pc = 0x0000
        self.sp = 0x0000
        # A B X Y
        self.registers = [0, 0, 0, 0]
        self.memory = [0]*MEM_SIZE
        
        self.instr = 0x00

        self.running = False

    def add_prog(self, prog, start):
        self.memory[start:len(prog)] = prog

    def cycle(self):
        #print(self.pc)
        self.instr = self.memory[self.pc]
        self.pc += 1
        
        if self.instr == 0x00: # HALT
            self.running = False
        if self.instr == 0x01: # NOP
            pass
        if self.instr == 0x02: # LDI
            p1 = self.memory[self.pc]
            self.pc += 1
            p2 = self.memory[self.pc]
            self.pc += 1
            
            self.registers[p1] = p2
        if self.instr == 0x03: # PRINT
            print(chr(self.registers[0]), end='')

    def run(self):
        self.running = True

        while self.running:
            self.cycle()

c = CPU()

c.add_prog([
    0x01, # NOP

    0x02, # LDI
    0x00, # RA
    0x48, # 'H'
    0x03, # PRINT
    
    0x02, # LDI
    0x00, # RA
    0x65, # 'e'
    0x03, # PRINT
    
    0x02, # LDI
    0x00, # RA
    0x6C, # 'l'
    0x03, # PRINT
    0x03, # PRINT
    
    0x02, # LDI
    0x00, # RA
    0x6f, # 'o'
    0x03, # PRINT
    
    0x02, # LDI
    0x00, # RA
    0x0a, # '\n'
    0x03  # PRINT
], 0x0000)

c.run()

