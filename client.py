import asm
import re



with open('out.asm', 'r') as infile:
	DATA = (infile.read().replace('\n', '').replace('\t', '').replace(' ',''))
	DATA = DATA[DATA.find('USE32') : ] # PRE-CLEANING




BF_DATA_SIZE = DATA[(DATA.find('DATAequ')+7) : (DATA.find('%macroc_s1'))]

NOJMP = True if "jmp loop" in DATA else False;
MMIO = True if "MMIO" in DATA else False;
CELL16 = True if asm.comma['cell16'] in DATA or asm.plus['cell16'] in DATA or asm.minus['cell16'] in DATA or asm.bthan['cell16'] in DATA or asm.lthan['cell16'] in DATA or asm.comma['mmcell'] in DATA or asm.plus['opcell'] in DATA or asm.minus['opcell'] in DATA or asm.lthan['opcell'] in DATA or asm.bthan['opcell'] in DATA else False

OPT = True if asm.plus['opt'] in DATA or asm.minus['opt'] in DATA or asm.lthan['opt'] in DATA or asm.bthan['opt'] in DATA or asm.plus['opcell'] in DATA or asm.minus['opcell'] in DATA or asm.lthan['opcell'] in DATA or asm.bthan['opcell'] in DATA else False


ID_PATTERN = re.escape(asm.obrack['std'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')



AT = asm.at['std'].replace('\n', '').replace('\t', '').replace(' ','')
CLOSE = asm.close['std'].replace('\n', '').replace('\t', '').replace(' ','')






INTRO = asm.intro['std'].replace('\n', '').replace('\t', '').replace(' ','')
INTRO = INTRO.format(BF_DATA_SIZE)

DOT = asm.dot['std'].replace('\n', '').replace('\t', '').replace(' ','')
COMMA = asm.comma['std'].replace('\n', '').replace('\t', '').replace(' ','')
PLUS = asm.plus['std'].replace('\n', '').replace('\t', '').replace(' ','')
MINUS = asm.minus['std'].replace('\n', '').replace('\t', '').replace(' ','')
LTHAN = asm.lthan['std'].replace('\n', '').replace('\t', '').replace(' ','')
BTHAN = asm.bthan['std'].replace('\n', '').replace('\t', '').replace(' ','')
#OBRACK = re.escape(asm.obrack['std'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')
#CBRACK = re.escape(asm.cbrack['std'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')

if MMIO: 
	MMIO_SIZE = DATA[(DATA.find('MMIO_SIZEequ')+12) : DATA.find('section.bss')]

	INTRO = asm.intro['mmio'].replace('\n', '').replace('\t', '').replace(' ','')
	INTRO = INTRO.format(BF_DATA_SIZE, MMIO_SIZE)

	DOT = asm.dot['mmio'].replace('\n', '').replace('\t', '').replace(' ','')
	COMMA = asm.comma['mmio'].replace('\n', '').replace('\t', '').replace(' ','')
	PLUS = asm.plus['std'].replace('\n', '').replace('\t', '').replace(' ','')
	MINUS = asm.minus['std'].replace('\n', '').replace('\t', '').replace(' ','')
	LTHAN = asm.lthan['std'].replace('\n', '').replace('\t', '').replace(' ','')
	BTHAN = asm.bthan['std'].replace('\n', '').replace('\t', '').replace(' ','')



if NOJMP:
	INTRO = asm.intro['nojmp'].replace('\n', '').replace('\t', '').replace(' ','')
	INTRO = INTRO.format(BF_DATA_SIZE)



if CELL16:
	COMMA = asm.comma['cell16'].replace('\n', '').replace('\t', '').replace(' ','')
	PLUS = asm.plus['cell16'].replace('\n', '').replace('\t', '').replace(' ','')
	MINUS = asm.minus['cell16'].replace('\n', '').replace('\t', '').replace(' ','')
	LTHAN = asm.lthan['cell16'].replace('\n', '').replace('\t', '').replace(' ','')
	BTHAN = asm.bthan['cell16'].replace('\n', '').replace('\t', '').replace(' ','')
	#OBRACK = re.escape(asm.obrack['cell16'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')
	#CBRACK = re.escape(asm.cbrack['cell16'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')



if OPT:
	PLUS = asm.plus['opt'].replace('\n', '').replace('\t', '').replace(' ','')
	MINUS = asm.minus['opt'].replace('\n', '').replace('\t', '').replace(' ','')
	LTHAN = asm.lthan['opt'].replace('\n', '').replace('\t', '').replace(' ','')
	BTHAN = asm.bthan['opt'].replace('\n', '').replace('\t', '').replace(' ','')



if MMIO and NOJMP:
	INTRO = asm.intro['mmjmp'].replace('\n', '').replace('\t', '').replace(' ','')
	INTRO = INTRO.format(BF_DATA_SIZE, MMIO_SIZE)



if OPT and CELL16:
	PLUS = asm.plus['opcell'].replace('\n', '').replace('\t', '').replace(' ','')
	MINUS = asm.minus['opcell'].replace('\n', '').replace('\t', '').replace(' ','')
	LTHAN = asm.lthan['opcell'].replace('\n', '').replace('\t', '').replace(' ','')
	BTHAN = asm.bthan['opcell'].replace('\n', '').replace('\t', '').replace(' ','')



if MMIO and CELL16:
	COMMA = asm.comma['mmcell'].replace('\n', '').replace('\t', '').replace(' ','')
	

print(MMIO)
print(NOJMP)
print(CELL16)
print(OPT)





if DATA[:len(INTRO)] == INTRO:
	counter = len(INTRO)
else:
	print("[!] No macros")

while counter < len(DATA):

	if data[counter:len(DOT)] == DOT:
		print('.')
		counter += DOT

	elif data[counter:len(COMMA)] == COMMA:
		print(',')
		counter += COMMA









"""
if DATA[:len(INTRO)] == INTRO:
	print(INTRO)
"""



#REGEX STUFF FOR OBRACK, CBRACK