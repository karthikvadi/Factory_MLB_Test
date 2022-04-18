'''
This class provide 4 function to implement number, plus, minus, multiple and divide operation.
'''
'''
Power plane resistances	Check resistances to GND				Record Measurements		
DVDD_24V0_R	Check resistance to GND	TP42		--	min	max	units
DVDD_12V0_R	Check resistance to GND	TP46		--			Ohms
DVDD_5V1_R	Check resistance to GND	TP47		--			Ohms
AVDD_5V0_R	Check resistance to GND	TP44		--			Ohms
DVDD_3V3_R	Check resistance to GND	TP48		--			Ohms
AVDD_3V3_R	Check resistance to GND	TP49		--			Ohms
DVDD_3V3_SW_R		TP159					
Power up board	Set power supply to 24V current limits to 100mA						
DVDD_24V0_I_BEFORE_FLASH	Record current consumption before programming board	TP42		--	>0	?	mA
DVDD_24V0_V	Record Input Voltage	TP42		--	23.9	24.1	V
Power Rail Voltage	Measure voltages on power rails				-5%	+5%	
#DVDD_12V0_V	Record voltage across specified TP to GND	TP46		--	11.4	12.6	V
DVDD_5V1_V	Record voltage across specified TP to GND	TP47		--	4.75	5.25	V
AVDD_5V0_V	Record voltage across specified TP to GND	TP44		--	4.75	5.25	V
DVDD_3V3_V	Record voltage across specified TP to GND	TP48		--	3.135	3.465	V
AVDD_3V3_V	Record voltage across specified TP to GND	TP49		--	3.135	3.465	V
DVDD_3V3_SW_V	Record voltage across specified TP to GND	TP159			3.135	3.465	V


'''


class MLB_Test:
#DVDD_12V0_V	Record voltage across specified TP to GND	TP46		--	11.4	12.6	V
    def DVDD_12V0_V(self, min_v, max_v):
        #Add Function to read Voltage
        D_Vdd_12V = 12 #
        if min_v <= float(D_Vdd_12V) <= max_v:
            return "PASS" , D_Vdd_12V
        else:
            return "FAIL",D_Vdd_12V
#DVDD_5V1_V	Record voltage across specified TP to GND	TP47		--	4.75	5.25	V
    def DVDD_5V1_V(self, min_v, max_v):
        #Add Function to read Voltage
        D_Vdd_51_V = 5 #
        if min_v <= D_Vdd_51_V <= max_v:
            return "PASS" , D_Vdd_51_V
        else:
            return "FAIL",D_Vdd_51_V
#AVDD_5V0_V	Record voltage across specified TP to GND	TP44		--	4.75	5.25	V
    def AVDD_5V0_V(self, min_v, max_v):
        #Add Function to read Voltage
        D_Vdd_50_V = 5 #
        if min_v <= D_Vdd_50_V <= max_v:
            return "PASS" , D_Vdd_50_V
        else:
            return "FAIL",D_Vdd_50_V
#DVDD_3V3_V	Record voltage across specified TP to GND	TP48		--	3.135	3.465	V
    def DVDD_3V3_V(self, min_v, max_v):
        #Add Function to read Voltage
        D_Vdd_33_V = 3.3 #
        if min_v <= D_Vdd_33_V <= max_v:
            return "PASS" , D_Vdd_33_V
        else:
            return "FAIL",D_Vdd_33_V
#AVDD_3V3_V	Record voltage across specified TP to GND	TP49		--	3.135	3.465	V
    def AVDD_3V3_V(self, min_v, max_v):
        #Add Function to read Voltage
        A_Vdd_33_V = 3.3 #
        if min_v <= A_Vdd_33_V <= max_v:
            return "PASS" , A_Vdd_33_V
        else:
            return "FAIL",A_Vdd_33_V

#DVDD_3V3_SW_V	Record voltage across specified TP to GND	TP159			3.135	3.465	V
    def DVDD_3V3_SW_V(self, min_v, max_v):
        #Add Function to read Voltage
        D_Vdd_33_V = 3.3 #
        if min_v <= D_Vdd_33_V <= max_v:
            return "PASS" , D_Vdd_33_V
        else:
            return "FAIL",D_Vdd_33_V
