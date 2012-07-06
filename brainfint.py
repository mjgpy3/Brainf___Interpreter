#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jun 28 23:42:22 EDT 2012
# 
# 

import sys

class BrainFInt:
	def __init__(self):
		self.array = []
		for i in range(3000):
			self.array.append(0)
		self.index = 0
		self.program = []
		self.programIndex = 0

	def MoveIndex(self, direction):
		if direction == '<' and self.index != 0:
			self.index -= 1
		if direction == '>' and self.index != 2999:
			self.index += 1

	def ReadProgramFromFile(self, fileName):
		try:
			with open(fileName, 'r') as f:
				self.program = filter(lambda x: x in ['>', '<', '+', '-', '.', ',', ']', '['], list(f.read()))
				self.program.append('EOP')
		except IOError:
			print 'File "' + fileName + '" not found'	

	def IncrementPointee(self):
		if self.array[self.index] <= 127: self.array[self.index] += 1

	def DecrementPointee(self):
		if self.array[self.index] > 0: self.array[self.index] -= 1

	def BackBeforeBrace(self):
		indent = 0
		while True:
			self.programIndex -= 1
			if self.program[self.programIndex] == ']':
				indent += 1
			if self.program[self.programIndex] == '[' and indent != 0:
				indent -= 1
			elif self.program[self.programIndex] == '[' and indent == 0:
				break

	def ForwardAfterBrace(self):
		indent = 0
                while True:
                        self.programIndex += 1
                        if self.program[self.programIndex] == '[':
                                indent += 1
                        if self.program[self.programIndex] == ']' and indent != 0:
                                indent -= 1
                        elif self.program[self.programIndex] == ']' and indent == 0:
                                break

	def DotPrint(self):
		sys.stdout.write(chr(self.array[self.index]))

	def ReadChar(self):
		self.array[self.index] = ord(sys.stdin.read(1)[0])

if __name__ == '__main__':
	handler = BrainFInt()
	try:
		handler.ReadProgramFromFile(sys.argv[1])
	except:
		print "Proper use:\nbrainfint.py [fileToInterpret]"
		exit()

	while handler.program[handler.programIndex] != 'EOP':
		if handler.program[handler.programIndex] in ['>', '<']:
			handler.MoveIndex(handler.program[handler.programIndex])
		elif handler.program[handler.programIndex] == '+':
			handler.IncrementPointee()
		elif handler.program[handler.programIndex] == '-':
			handler.DecrementPointee() 
		elif handler.program[handler.programIndex] == '.':
			handler.DotPrint()
		elif handler.program[handler.programIndex] == ',':
			handler.ReadChar()

		if handler.program[handler.programIndex] == '[' and \
		handler.array[handler.index] == 0:
			handler.ForwardAfterBrace()
	
		if handler.program[handler.programIndex] == ']' and \
		handler.array[handler.index] != 0:
			handler.BackBeforeBrace()
		
		handler.programIndex += 1
