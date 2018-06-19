from bitstring import Bits

class Parser:
	
	
	def __parse(self,*reg):
		if len(reg)==2:
			val = format(reg[0],"b").zfill(16)+format(reg[1],"b").zfill(16)
			return Bits(bin = val)
		elif len(reg)==1:
			val = format(reg[0],"b").zfill(16)
			return Bits(bin = val)

	def __parseBCD(self,*reg):
		if len(reg)==1:
			val = format(reg[0],"b").zfill(16)
		
		elif len(reg)==2:
			val = format(reg[0],"b").zfill(16)+format(reg[1],"b").zfill(16)
		elif len(reg)==3:
			val = format(reg[0],"b").zfill(16)+format(reg[1],"b").zfill(16)+format(reg[2],"b").zfill(16)
		
		val_list = [val[i:i+4] for i in range(0,len(val),4)]
		val_list = [int(i,2) for i in val_list]
		val = "".join(str(x) for x in val_list)
		return val
		
		
	def readFeed(self):	
		

		#read feed
		file = open("feed.txt")
		reg = file.readlines()
		reg = [int(i.split(":")[1]) for i in reg]
		file.close()
		
	
		
		
		# convert data to readable format
		flowRate = self.__parse(reg[2],reg[1]).float
		energyFlowRate = self.__parse(reg[4],reg[3]).float
		velocity = self.__parse(reg[6],reg[5]).float
		fluidSoundSpeed = self.__parse(reg[8],reg[7]).float
		positiveAccumulator = self.__parse(reg[10],reg[9]).int
		positiveDecimalFraction = self.__parse(reg[12],reg[11]).float
		negativeAccumulator = self.__parse(reg[14],reg[13]).int
		negativeDecimalFraction = self.__parse(reg[16],reg[15]).float
		positiveEnergyAccumulator = self.__parse(reg[18],reg[17]).int
		positiveEnergyDecimalFraction = self.__parse(reg[20],reg[19]).float
		negativeEnergyAccumulator = self.__parse(reg[22],reg[21]).int
		negativeEnergyDeciamlFraction = self.__parse(reg[24],reg[23]).float
		netAccumulator = self.__parse(reg[26],reg[25]).int
		netDecimalFraction = self.__parse(reg[28],reg[27]).float
		netEnergyAccumulator = self.__parse(reg[30],reg[29]).int
		netEnergyDecimalFraction = self.__parse(reg[32],reg[31]).float
		temperatureInlet = self.__parse(reg[34],reg[33]).float
		temperatureOutlet = self.__parse(reg[36],reg[35]).float
		analogInput3 = self.__parse(reg[38],reg[37]).float
		analogInput4 = self.__parse(reg[40],reg[39]).float
		analogInput5 = self.__parse(reg[42],reg[41]).float
		currentAI3 = self.__parse(reg[44],reg[43]).float
		currentAI4 = self.__parse(reg[46],reg[45]).float
		currentAI5 = self.__parse(reg[48],reg[47]).float
		systemPassword = self.__parseBCD(reg[50],reg[49])
		hardwarePassword = self.__parseBCD(reg[51])
		calendar = self.__parseBCD(reg[55],reg[54],reg[53])
		dayHourForAutoSave = self.__parseBCD(reg[56])
		keyToInput = reg[59]
		goToWindowNr = reg[60]
		LCDBackLightSec = reg[61]
		timesBeeper = reg[62]
		pulsesLeftForOCT = reg[62]	# Same reg as timesBeeper???
		
		errorCode = format(reg[72],"b").zfill(16)
		
		PT100ResistanceOfInlet = self.__parse(reg[78],reg[77]).float
		PT100ResistanceOfOutlet = self.__parse(reg[80],reg[79]).float
		totalTravelTime = self.__parse(reg[82],reg[81]).float
		deltaTravelTime = self.__parse(reg[84],reg[83]).float
		upstreamTravelTime = self.__parse(reg[86],reg[85]).float
		downstreamTravelTime = self.__parse(reg[88],reg[87]).float
		outputCurrent = self.__parse(reg[90],reg[89]).float
		
		signalQuality = format(reg[92],"b").zfill(16)
		workingStep = Bits(bin = signalQuality[:8]).uint
		signalQuality = Bits(bin = signalQuality[8:]).uint
		
		upstreamStrength = reg[93]
		downstreamStrength = reg[94]
		
		if reg[96] == 0:
			language = "English"
		elif reg[96] == 1:
			language = "Chinese"
		else:
			language = "Other"
		
		rateOfMeasuredTravelTimeByCalculatedTravelTime = self.__parse(reg[98],reg[97]).float
		reynoldsNumber = self.__parse(reg[100],reg[99]).float
		
		global data
		data = {
			"flowRate":{
				"Value": flowRate,
				"Unit": "m^3/h"
			},
			"energyFlowRate":{
				"Value": energyFlowRate,
				"Unit": "GJ/h"
			},
			"velocity":{
				"Value": velocity,
				"Unit": "m/s"
			},
			"fluidSoundSpeed":{
				"Value": fluidSoundSpeed,
				"Unit": "m/s"
			},
			"positiveAccumulator":{
				"Value": positiveAccumulator,
				"Unit": ""
			},
			"positiveDecimalFraction":{
				"Value": positiveDecimalFraction,
				"Unit": ""
			},
			"negativeAccumulator":{
				"Value": negativeAccumulator,
				"Unit": ""
			},
			"negativeDecimalFraction":{
				"Value": negativeDecimalFraction,
				"Unit": ""
			},
			"positiveEnergyAccumulator":{
				"Value": positiveEnergyAccumulator,
				"Unit": ""
			},
			"positiveEnergyDecimalFraction":{
				"Value": positiveEnergyDecimalFraction,
				"Unit": ""
			},
			"negativeEnergyAccumulator":{
				"Value": negativeEnergyAccumulator,
				"Unit": ""
			},
			"negativeEnergyDeciamlFraction":{
				"Value": negativeEnergyDeciamlFraction,
				"Unit": ""
			},
			"netAccumulator":{
				"Value": netAccumulator,
				"Unit": ""
			},
			"netDecimalFraction":{
				"Value": netDecimalFraction,
				"Unit": ""
			},
			"netEnergyAccumulator":{
				"Value": netEnergyAccumulator,
				"Unit": ""
			},
			"netEnergyDecimalFraction":{
				"Value": netEnergyDecimalFraction,
				"Unit": ""
			},
			"temperatureInlet":{
				"Value": temperatureInlet,
				"Unit": "C"
			},
			"temperatureOutlet":{
				"Value": temperatureOutlet,
				"Unit": "C"
			},
			"analogInput3":{
				"Value": analogInput3,
				"Unit": ""
			},
			"analogInput4":{
				"Value": analogInput4,
				"Unit": ""
			},
			"analogInput5":{
				"Value": analogInput5,
				"Unit": ""
			},
			"currentAI3":{
				"Value": currentAI3,
				"Unit": "mA"
			},
			"currentAI4":{
				"Value": currentAI4,
				"Unit": "mA"
			},
			"currentAI5":{
				"Value": currentAI5,
				"Unit": "mA"
			},
			"systemPassword":{
				"Value": systemPassword,
				"Unit": ""
			},
			"hardwarePassword":{
				"Value": hardwarePassword,
				"Unit": ""
			},
			"calendar":{
				"Value": calendar,
				"Unit": "YYMMDDHHMMSS"
			},
			"dayHourForAutoSave":{
				"Value": dayHourForAutoSave,
				"Unit": ""
			},
			"keyToInput":{
				"Value": keyToInput,
				"Unit": ""
			},
			"goToWindowNr":{
				"Value": goToWindowNr,
				"Unit": ""
			},
			"LCDBackLightSec":{
				"Value": LCDBackLightSec,
				"Unit": "sec"
			},
			"timesBeeper":{
				"Value": timesBeeper,
				"Unit": ""
			},
			"pulsesLeftForOCT":{
				"Value": pulsesLeftForOCT,
				"Unit": ""
			},
			"errorCode":{
				"Value": errorCode,
				"Unit": ""
			},
			"PT100ResistanceOfInlet":{
				"Value": PT100ResistanceOfInlet,
				"Unit": "Ohm"
			},
			"PT100ResistanceOfOutlet":{
				"Value": PT100ResistanceOfOutlet,
				"Unit": "Ohm"
			},
			"totalTravelTime":{
				"Value": totalTravelTime,
				"Unit": "micro-sec"
			},
			"deltaTravelTime":{
				"Value": deltaTravelTime,
				"Unit": "micro-sec"
			},
			"upstreamTravelTime":{
				"Value": upstreamTravelTime,
				"Unit": "micro-sec"
			},
			"downstreamTravelTime":{
				"Value": downstreamTravelTime,
				"Unit": "micro-sec"
			},
			"outputCurrent":{
				"Value": outputCurrent,
				"Unit": "mA"
			},
			"workingStep":{
				"Value": workingStep,
				"Unit": ""
			},
			"signalQuality":{
				"Value": signalQuality,
				"Unit": ""
			},
			"upstreamStrength":{
				"Value": upstreamStrength,
				"Unit": ""
			},
			"downstreamStrength":{
				"Value": downstreamStrength,
				"Unit": ""
			},
			"language":{
				"Value": language,
				"Unit": ""
			},
			"rateOfMeasuredTravelTimeByCalculatedTravelTime":{
				"Value": rateOfMeasuredTravelTimeByCalculatedTravelTime,
				"Unit": "Percent"
			},
			"reynoldsNumber":{
				"Value": reynoldsNumber,
				"Unit": ""
			}
		}		
	
	
	def get_data(self,keys=None):
		global data
		if keys:
			data = dict(zip(keys,map(data.get,keys)))
			return data
		else:
			return data

